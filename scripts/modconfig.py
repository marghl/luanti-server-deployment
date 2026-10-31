#!/usr/bin/env python3
"""Luanti-Modkonfiguration aus einfachen schluessel = wert Dateien."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD_CONFIG = ROOT / "config" / "mods"
BASE_CONFIG = ROOT / "config" / "base"
GENERATED = ROOT / "generated"
STATE_MODS = ROOT / "state" / "mods"
SOURCE_SERVER = ROOT / "config" / "luanti" / "server.conf.test"
SOURCE_WORLD = ROOT / "config" / "luanti" / "world.mt.test"

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


def parse_luanti(path: Path) -> tuple[list[str], dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    values: dict[str, str] = {}
    for raw in lines:
        line = raw.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = (part.strip() for part in line.split("=", 1))
            values[key] = value
    return lines, values


def write_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def mod_metadata(path: Path) -> dict[str, str]:
    metadata: dict[str, str] = {}
    if not path.exists():
        return metadata
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = (part.strip() for part in line.split("=", 1))
        metadata[key] = value
    return metadata


def csv(value: str) -> list[str]:
    return [item.strip().rstrip("?") for item in value.split(",") if item.strip()]


def git_value(checkout: Path, args: list[str]) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(checkout), *args], text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def discover_mods(world_values: dict[str, str]) -> dict[str, dict[str, object]]:
    discovered: dict[str, dict[str, object]] = {}
    for mod_conf in sorted(STATE_MODS.rglob("mod.conf")):
        if ".git" in mod_conf.parts:
            continue
        metadata = mod_metadata(mod_conf)
        name = metadata.get("name", mod_conf.parent.name)
        relative = mod_conf.parent.relative_to(STATE_MODS)
        checkout = relative.parts[0]
        if name in discovered:
            selected = world_values.get(f"load_mod_{name}", "")
            selected = selected.removeprefix("mods/")
            if selected == relative.as_posix():
                pass
            elif selected == str(discovered[name]["path"]):
                continue
            else:
                print(
                    f"WARNUNG: Modname {name} kommt mehrfach vor; "
                    f"verwende {discovered[name]['path']}", file=sys.stderr,
                )
                continue
        required = csv(metadata.get("depends", ""))
        optional = csv(metadata.get("optional_depends", ""))
        legacy = mod_conf.parent / "depends.txt"
        if legacy.exists():
            for raw in legacy.read_text(encoding="utf-8", errors="replace").splitlines():
                item = raw.strip()
                if not item or item.startswith("#"):
                    continue
                if item.endswith("?"):
                    optional.append(item[:-1])
                else:
                    required.append(item)
        discovered[name] = {
            "name": name,
            "path": relative.as_posix(),
            "checkout": checkout,
            "depends": sorted(set(required)),
            "optional_depends": sorted(set(optional)),
            "dir": mod_conf.parent,
        }
    for key, value in world_values.items():
        if not key.startswith("load_mod_"):
            continue
        name = key.removeprefix("load_mod_")
        if name in discovered or value.lower() in {"", "false", "nil", "0"}:
            continue
        if value == "true":
            print(
                f"WARNUNG: {key} verwendet true und konnte keinem mod.conf-Namen "
                "zugeordnet werden", file=sys.stderr,
            )
            continue
        relative = Path(value.removeprefix("mods/"))
        target = STATE_MODS / relative
        metadata = mod_metadata(target / "mod.conf")
        discovered[name] = {
            "name": name,
            "path": relative.as_posix(),
            "checkout": relative.parts[0],
            "depends": sorted(set(csv(metadata.get("depends", "")))),
            "optional_depends": sorted(set(csv(metadata.get("optional_depends", "")))),
            "dir": target,
        }
    return discovered


SETTING_RE = re.compile(
    r"^([A-Za-z0-9_.-]+)\s+\([^)]*\)\s+\S+(?:\s+(\S.*))?$"
)


def setting_defaults(mod_dir: Path, include_checkout: bool = False) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    candidates = [mod_dir / "settingtypes.txt"]
    checkout_root = STATE_MODS / mod_dir.relative_to(STATE_MODS).parts[0]
    if include_checkout and checkout_root / "settingtypes.txt" not in candidates:
        candidates.append(checkout_root / "settingtypes.txt")
    seen: set[str] = set()
    for source in candidates:
        if not source.exists():
            continue
        for raw in source.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            match = SETTING_RE.match(line)
            if not match or match.group(1) in seen:
                continue
            name = match.group(1)
            tail = (match.group(2) or "").split()
            default = tail[0] if tail else ""
            result.append((name, default))
            seen.add(name)
    return result


def manifest_path(name: str) -> Path:
    return MOD_CONFIG / name / "mod.conf"


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


def migrate() -> None:
    server_lines, server_values = parse_luanti(SOURCE_SERVER)
    _, world_values = parse_luanti(SOURCE_WORLD)
    mods = discover_mods(world_values)
    checkout_owners: dict[str, str] = {}
    for mod_name, info in sorted(mods.items()):
        checkout_owners.setdefault(str(info["checkout"]), mod_name)

    known_settings: set[str] = set()
    for name, info in mods.items():
        defaults = setting_defaults(
            info["dir"], checkout_owners[str(info["checkout"])] == name
        )
        known_settings.update(key for key, _ in defaults)
        checkout_dir = STATE_MODS / str(info["checkout"])
        is_checkout = (checkout_dir / ".git").exists()
        url = git_value(checkout_dir, ["remote", "get-url", "origin"]) if is_checkout else ""
        commit = git_value(checkout_dir, ["rev-parse", "HEAD"]) if is_checkout else ""
        source = "git" if url and commit else "existing"
        load_value = world_values.get(f"load_mod_{name}", "false")
        enabled = load_value.lower() not in {"", "false", "nil", "0"}
        content = [
            f"# Mod {name}",
            f"name = {name}",
            f"enabled = {'true' if enabled else 'false'}",
            "",
            f"checkout = {info['checkout']}",
            f"path = {info['path']}",
            f"source = {source}",
            f"git_url = {url}",
            f"git_commit = {commit}",
            "",
            f"depends = {','.join(info['depends'])}",
            f"optional_depends = {','.join(info['optional_depends'])}",
            "",
        ]
        write_atomic(manifest_path(name), "\n".join(content))

        settings = [f"# Einstellungen fuer {name}"]
        if not defaults:
            settings.append("# Keine settingtypes.txt-Eintraege gefunden.")
        for key, default in defaults:
            if key in server_values:
                settings.append(f"{key} = {server_values[key]}")
            elif default:
                settings.append(f"# {key} = {default}")
            else:
                settings.append(f"# {key} =")
        settings.append("")
        write_atomic(MOD_CONFIG / name / "settings.conf", "\n".join(settings))

    base_server: list[str] = []
    for raw in server_lines:
        line = raw.strip()
        if line and not line.startswith("#") and "=" in line:
            key = line.split("=", 1)[0].strip()
            if key in known_settings:
                continue
        base_server.append(raw)
    while base_server and not base_server[-1].strip():
        base_server.pop()
    write_atomic(BASE_CONFIG / "server.conf", "\n".join(base_server) + "\n")

    world_lines, _ = parse_luanti(SOURCE_WORLD)
    base_world = [line for line in world_lines if not line.strip().startswith("load_mod_")]
    while base_world and not base_world[-1].strip():
        base_world.pop()
    write_atomic(BASE_CONFIG / "world.conf", "\n".join(base_world) + "\n")
    generate()
    print(f"{len(mods)} Mod-Manifeste erzeugt")


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
    parser.add_argument("command", choices=("migrate", "generate", "verify", "status"))
    args = parser.parse_args()
    if args.command == "migrate":
        migrate()
    elif args.command == "generate":
        generate()
    elif args.command == "verify":
        validate(load_manifests())
        print("Modkonfiguration ist konsistent")
    elif args.command == "status":
        status()


if __name__ == "__main__":
    main()
