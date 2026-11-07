#!/usr/bin/env python3
"""Export reproducibility and translation inventory metrics to Pushgateway."""

from __future__ import annotations

import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path


CONFIG_MODS = Path(os.environ.get("CONFIG_MODS_PATH", "/workspace/config/mods"))
MODS = Path(os.environ.get("MODS_PATH", "/workspace/mods"))
PUSHGATEWAY = os.environ.get("PUSHGATEWAY_URL", "http://pushgateway:9091").rstrip("/")
INSTANCE = os.environ.get("METRICS_INSTANCE", "marghl")
LANGUAGE = os.environ.get("TRANSLATION_LANGUAGE", "de")


def parse_settings(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip()
    return values


def parse_tr(path: Path) -> tuple[int, int]:
    total = translated = 0
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        _, value = line.split("=", 1)
        total += 1
        if value.strip():
            translated += 1
    return total, translated


def parse_po(path: Path) -> tuple[int, int]:
    total = translated = 0
    current_id: list[str] = []
    current_str: list[str] = []
    field: str | None = None
    fuzzy = False

    def finish() -> None:
        nonlocal total, translated, current_id, current_str, field, fuzzy
        msgid = "".join(current_id)
        if msgid:
            total += 1
            if "".join(current_str) and not fuzzy:
                translated += 1
        current_id = []
        current_str = []
        field = None
        fuzzy = False

    quoted = re.compile(r'^"(.*)"$')
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line:
            finish()
            continue
        if line.startswith("#,") and "fuzzy" in line:
            fuzzy = True
        elif line.startswith("msgid "):
            current_id = [line[6:].strip().strip('"')]
            field = "id"
        elif line.startswith("msgstr "):
            current_str = [line[7:].strip().strip('"')]
            field = "str"
        else:
            match = quoted.match(line)
            if match and field == "id":
                current_id.append(match.group(1))
            elif match and field == "str":
                current_str.append(match.group(1))
    finish()
    return total, translated


def translation_counts(mod_path: Path, language: str) -> tuple[int, int]:
    locale = mod_path / "locale"
    if not locale.is_dir():
        return 0, 0

    templates = sorted(locale.glob("*.pot"))
    templates += [p for p in (locale / "template.txt", locale / f"{mod_path.name}.pot") if p.is_file()]
    source_total = 0
    for path in templates:
        total, _ = parse_po(path) if path.suffix == ".pot" else parse_tr(path)
        source_total = max(source_total, total)

    candidates = sorted(locale.glob(f"{language}.po"))
    candidates += sorted(locale.glob(f"*.{language}.po"))
    candidates += sorted(locale.glob(f"{language}.tr"))
    candidates += sorted(locale.glob(f"*.{language}.tr"))

    translated_total = translation_total = 0
    for path in dict.fromkeys(candidates):
        total, translated = parse_po(path) if path.suffix == ".po" else parse_tr(path)
        if total > translation_total:
            translation_total = total
            translated_total = translated

    source_total = max(source_total, translation_total)
    return source_total, min(translated_total, source_total)


def escape_label(value: str) -> str:
    return value.replace("\\", "\\\\").replace("\n", "\\n").replace('"', '\\"')


def metric(name: str, value: int | float, labels: dict[str, str] | None = None) -> str:
    label_text = ""
    if labels:
        pairs = [f'{key}="{escape_label(val)}"' for key, val in sorted(labels.items())]
        label_text = "{" + ",".join(pairs) + "}"
    return f"{name}{label_text} {value}"


def collect() -> str:
    manifests: list[tuple[str, dict[str, str]]] = []
    for manifest in sorted(CONFIG_MODS.glob("*/mod.conf")):
        manifests.append((manifest.parent.name, parse_settings(manifest)))

    enabled = Counter()
    sources = Counter()
    checkout_sources: dict[str, str] = {}
    translation_states = Counter()
    translation_source = translation_done = 0
    lines = [
        "# HELP luanti_project_inventory_last_success_unixtime Last successful inventory generation.",
        "# TYPE luanti_project_inventory_last_success_unixtime gauge",
        metric("luanti_project_inventory_last_success_unixtime", int(time.time())),
        "# HELP luanti_project_mods Number of configured mods.",
        "# TYPE luanti_project_mods gauge",
        metric("luanti_project_mods", len(manifests)),
    ]

    for name, data in manifests:
        is_enabled = data.get("enabled", "false").lower() == "true"
        source = data.get("source", "unknown")
        checkout = data.get("checkout", name)
        enabled[str(is_enabled).lower()] += 1
        sources[source] += 1
        checkout_sources[checkout] = source

        mod_path = MODS / data.get("path", name)
        total, translated = translation_counts(mod_path, LANGUAGE) if mod_path.is_dir() else (0, 0)
        if total == 0:
            state = "not_translatable"
        elif translated >= total:
            state = "complete"
        else:
            state = "incomplete"
        translation_states[state] += 1
        translation_source += total
        translation_done += translated
        ratio = translated / total if total else 0
        lines.append(metric("luanti_project_mod_translation_ratio", ratio, {
            "language": LANGUAGE,
            "mod": name,
            "state": state,
        }))

    lines += [
        "# HELP luanti_project_mods_by_enabled Configured mods by enabled state.",
        "# TYPE luanti_project_mods_by_enabled gauge",
    ]
    for state, count in sorted(enabled.items()):
        lines.append(metric("luanti_project_mods_by_enabled", count, {"enabled": state}))

    lines += [
        "# HELP luanti_project_mods_by_source Configured mod manifests by source type.",
        "# TYPE luanti_project_mods_by_source gauge",
    ]
    for source, count in sorted(sources.items()):
        lines.append(metric("luanti_project_mods_by_source", count, {"source": source}))

    checkout_counts = Counter(checkout_sources.values())
    lines += [
        "# HELP luanti_project_checkouts_by_source Unique checkouts by source type.",
        "# TYPE luanti_project_checkouts_by_source gauge",
    ]
    for source, count in sorted(checkout_counts.items()):
        lines.append(metric("luanti_project_checkouts_by_source", count, {"source": source}))

    lines += [
        "# HELP luanti_project_translation_mods Mods by translation state.",
        "# TYPE luanti_project_translation_mods gauge",
    ]
    for state in ("complete", "incomplete", "not_translatable"):
        lines.append(metric("luanti_project_translation_mods", translation_states[state], {
            "language": LANGUAGE,
            "state": state,
        }))
    lines += [
        "# HELP luanti_project_translation_strings Translation strings by state.",
        "# TYPE luanti_project_translation_strings gauge",
        metric("luanti_project_translation_strings", translation_source, {
            "language": LANGUAGE, "state": "total",
        }),
        metric("luanti_project_translation_strings", translation_done, {
            "language": LANGUAGE, "state": "translated",
        }),
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    payload = collect().encode("utf-8")
    url = f"{PUSHGATEWAY}/metrics/job/project_inventory/instance/{INSTANCE}"
    request = urllib.request.Request(url, data=payload, method="PUT", headers={
        "Content-Type": "text/plain; version=0.0.4; charset=utf-8",
    })
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            if response.status >= 300:
                raise RuntimeError(f"Pushgateway returned HTTP {response.status}")
    except (OSError, urllib.error.URLError, RuntimeError) as error:
        print(f"project-metrics: push failed: {error}", file=sys.stderr)
        return 1
    print(f"project-metrics: pushed inventory for {INSTANCE} ({LANGUAGE})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
