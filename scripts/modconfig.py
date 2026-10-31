#!/usr/bin/env python3
"""Luanti-Modkonfiguration aus einfachen schluessel = wert Dateien."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD_CONFIG = ROOT / "config" / "mods"
BASE_CONFIG = ROOT / "config" / "base"
GENERATED = ROOT / "generated"
STATE_MODS = ROOT / "state" / "mods"

MANIFEST_KEYS = {
    "name", "enabled", "checkout", "path", "source", "git_url",
    "git_commit", "depends", "optional_depends",
}


def fail(message: str) -> None:
    raise SystemExit(f"FEHLER: {message}")


def parse_pairs(path: Path, allowed: set[str] | None = None) -> dict[str, str]:
    values: dict[str, str] = {}
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            fail(f"{path}:{number}: erwartet wird schluessel = wert")
        key, value = (part.strip() for part in line.split("=", 1))
        if not key:
            fail(f"{path}:{number}: leerer Schluessel")
        if allowed is not None and key not in allowed:
            fail(f"{path}:{number}: unbekannter Schluessel {key}")
        if key in values:
            fail(f"{path}:{number}: doppelter Schluessel {key}")
        values[key] = value
    return values


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def csv(value: str) -> list[str]:
    return [item.strip().rstrip("?") for item in value.split(",") if item.strip()]


def load_manifests() -> dict[str, dict[str, str]]:
    manifests: dict[str, dict[str, str]] = {}
    for path in sorted(MOD_CONFIG.glob("*/mod.conf")):
        data = parse_pairs(path, MANIFEST_KEYS)
        name = data.get("name", "")
        if not name:
            fail(f"{path}: name fehlt")
        if name in manifests:
            fail(f"Mod {name} ist doppelt konfiguriert")
        if data.get("enabled") not in {"true", "false"}:
            fail(f"{path}: enabled muss true oder false sein")
        manifests[name] = data
    return manifests


def validate(manifests: dict[str, dict[str, str]]) -> None:
    enabled = {name for name, data in manifests.items() if data["enabled"] == "true"}
    errors: list[str] = []
    for name, data in manifests.items():
        target = STATE_MODS / data["path"]
        if not target.exists():
            errors.append(f"{name}: Pfad fehlt: {target.relative_to(ROOT)}")
        if data["enabled"] != "true":
            continue
        for dependency in csv(data.get("depends", "")):
            if dependency in manifests and dependency not in enabled:
                errors.append(f"{name}: notwendiger Mod {dependency} ist deaktiviert")
    if errors:
        fail("\n".join(errors))


def active_settings() -> list[str]:
    result: list[str] = []
    owners: dict[str, Path] = {}
    for path in sorted(MOD_CONFIG.glob("*/settings.conf")):
        for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                fail(f"{path}:{number}: erwartet wird schluessel = wert")
            key = line.split("=", 1)[0].strip()
            if key in owners:
                fail(f"Einstellung {key} steht in {owners[key]} und {path}")
            owners[key] = path
            result.append(line)
    return result


def generate() -> None:
    manifests = load_manifests()
    validate(manifests)
    server = (BASE_CONFIG / "server.conf").read_text(encoding="utf-8").rstrip()
    settings = active_settings()
    server_output = server + "\n"
    if settings:
        server_output += "\n# Automatisch aus config/mods/*/settings.conf erzeugt.\n"
        server_output += "\n".join(settings) + "\n"

    world = (BASE_CONFIG / "world.conf").read_text(encoding="utf-8").rstrip()
    world_output = world + "\n\n# Automatisch aus config/mods/*/mod.conf erzeugt.\n"
    for name in sorted(manifests):
        data = manifests[name]
        value = f"mods/{data['path']}" if data["enabled"] == "true" else "false"
        world_output += f"load_mod_{name} = {value}\n"

    write_atomic(GENERATED / "server.conf", server_output)
    write_atomic(GENERATED / "world.mt", world_output)
    print(f"Konfiguration fuer {len(manifests)} Mods erzeugt")


def status() -> None:
    manifests = load_manifests()
    validate(manifests)
    counts = {"git": 0, "existing": 0, "enabled": 0, "disabled": 0}
    for data in manifests.values():
        counts[data.get("source", "existing")] = counts.get(data.get("source", "existing"), 0) + 1
        counts["enabled" if data["enabled"] == "true" else "disabled"] += 1
    print(f"Mods: {len(manifests)} ({counts['enabled']} aktiv, {counts['disabled']} inaktiv)")
    print(f"Quellen: {counts.get('git', 0)} Git, {counts.get('existing', 0)} noch nicht reproduzierbar")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("generate", "verify", "status"))
    args = parser.parse_args()
    if args.command == "generate":
        generate()
    elif args.command == "verify":
        validate(load_manifests())
        print("Modkonfiguration ist konsistent")
    elif args.command == "status":
        status()


if __name__ == "__main__":
    main()
