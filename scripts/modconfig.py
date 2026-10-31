#!/usr/bin/env python3
"""Luanti-Modkonfiguration aus einfachen schluessel = wert Dateien."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import tempfile
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


def checkout_groups(
    manifests: dict[str, dict[str, str]],
) -> dict[str, list[tuple[str, dict[str, str]]]]:
    groups: dict[str, list[tuple[str, dict[str, str]]]] = {}
    errors: list[str] = []
    for name, data in manifests.items():
        source = data.get("source", "")
        checkout = data.get("checkout", "")
        mod_path = Path(data.get("path", ""))
        if source not in {"git", "existing"}:
            errors.append(f"{name}: source muss git oder existing sein")
        if not checkout or Path(checkout).is_absolute() or len(Path(checkout).parts) != 1:
            errors.append(f"{name}: ungueltiges Checkout-Verzeichnis {checkout!r}")
            continue
        if not data.get("path") or mod_path.is_absolute() or ".." in mod_path.parts:
            errors.append(f"{name}: ungueltiger Modpfad {data.get('path', '')!r}")
        elif mod_path.parts[0] != checkout:
            errors.append(f"{name}: Pfad liegt nicht im Checkout {checkout}")
        if source == "git":
            if not data.get("git_url"):
                errors.append(f"{name}: git_url fehlt")
            if not re.fullmatch(r"[0-9a-fA-F]{40}", data.get("git_commit", "")):
                errors.append(f"{name}: git_commit muss ein vollstaendiger Commit-Hash sein")
        groups.setdefault(checkout, []).append((name, data))

    for checkout, members in groups.items():
        git_specs = {
            (data.get("git_url", ""), data.get("git_commit", ""))
            for _, data in members if data.get("source") == "git"
        }
        sources = {data.get("source") for _, data in members}
        if len(git_specs) > 1:
            errors.append(f"{checkout}: widerspruechliche Git-URL oder Commits")
        if "git" in sources and "existing" in sources:
            errors.append(f"{checkout}: source ist teils git, teils existing")
    if errors:
        fail("\n".join(errors))
    return groups


def git(checkout: Path, *arguments: str, capture: bool = False) -> str:
    command = ["git", "-C", str(checkout), *arguments]
    try:
        completed = subprocess.run(
            command,
            check=True,
            text=True,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE if capture else None,
        )
    except FileNotFoundError:
        fail("git ist nicht installiert")
    except subprocess.CalledProcessError as error:
        detail = (error.stderr or "").strip()
        fail(f"Git-Befehl fehlgeschlagen: {' '.join(command)}" + (f"\n{detail}" if detail else ""))
    return completed.stdout.strip() if capture else ""


def sync(check_only: bool = False) -> None:
    manifests = load_manifests()
    groups = checkout_groups(manifests)
    git_groups: list[tuple[str, str, str]] = []
    existing = 0
    errors: list[str] = []

    # Erst alle vorhandenen Arbeitskopien pruefen, bevor irgendetwas veraendert wird.
    for checkout, members in sorted(groups.items()):
        data = members[0][1]
        if data.get("source") != "git":
            existing += 1
            continue
        url = data["git_url"]
        commit = data["git_commit"].lower()
        target = STATE_MODS / checkout
        git_groups.append((checkout, url, commit))
        if not target.exists():
            continue
        if not (target / ".git").exists():
            errors.append(f"{checkout}: vorhanden, aber kein Git-Checkout")
            continue
        dirty = git(target, "status", "--porcelain", "--untracked-files=all", capture=True)
        if dirty:
            errors.append(f"{checkout}: lokale Aenderungen vorhanden")
        origin = git(target, "remote", "get-url", "origin", capture=True)
        if origin != url:
            errors.append(f"{checkout}: origin ist {origin!r}, erwartet wird {url!r}")
    if errors:
        fail("\n".join(errors))

    if check_only:
        print(f"Sync-Pruefung bestanden: {len(git_groups)} Git-Checkouts")
        print(f"Unveraendert: {existing} Checkouts mit source = existing")
        return

    STATE_MODS.mkdir(parents=True, exist_ok=True)
    for checkout, url, commit in git_groups:
        target = STATE_MODS / checkout
        print(f"Synchronisiere {checkout} auf {commit}")
        if target.exists():
            git(target, "fetch", "--quiet", "origin")
            git(target, "cat-file", "-e", f"{commit}^{{commit}}")
            git(target, "checkout", "--quiet", "--detach", commit)
            continue

        temporary = Path(tempfile.mkdtemp(prefix=f".{checkout}.sync-", dir=STATE_MODS))
        try:
            shutil.rmtree(temporary)
            subprocess.run(
                ["git", "clone", "--quiet", "--no-checkout", url, str(temporary)],
                check=True,
            )
            git(temporary, "checkout", "--quiet", "--detach", commit)
            os.replace(temporary, target)
        except (FileNotFoundError, subprocess.CalledProcessError) as error:
            fail(f"{checkout}: Klonen fehlgeschlagen: {error}")
        finally:
            if temporary.exists():
                shutil.rmtree(temporary)

    validate(manifests)
    errors = []
    for checkout, _, commit in git_groups:
        target = STATE_MODS / checkout
        actual = git(target, "rev-parse", "HEAD", capture=True).lower()
        if actual != commit:
            errors.append(f"{checkout}: ist auf {actual}, erwartet wird {commit}")
    if errors:
        fail("\n".join(errors))
    print(f"{len(git_groups)} Git-Checkouts synchronisiert")
    print(f"{existing} Checkouts mit source = existing unveraendert")


def validate(manifests: dict[str, dict[str, str]]) -> None:
    checkout_groups(manifests)
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
    parser.add_argument("command", choices=("generate", "verify", "status", "sync"))
    parser.add_argument(
        "--check", action="store_true",
        help="bei sync nur pruefen und nichts veraendern",
    )
    args = parser.parse_args()
    if args.check and args.command != "sync":
        parser.error("--check kann nur mit sync verwendet werden")
    if args.command == "generate":
        generate()
    elif args.command == "verify":
        validate(load_manifests())
        print("Modkonfiguration ist konsistent")
    elif args.command == "status":
        status()
    elif args.command == "sync":
        sync(args.check)


if __name__ == "__main__":
    main()
