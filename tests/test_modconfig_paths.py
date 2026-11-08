#!/usr/bin/env python3
"""Regression tests for the configured deployment mod path."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "modconfig.py"
SPEC = importlib.util.spec_from_file_location("modconfig", SCRIPT)
assert SPEC and SPEC.loader
modconfig = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(modconfig)


class ConfiguredModsPathTest(unittest.TestCase):
    def test_commands_validate_configured_path(self) -> None:
        expected = Path("/srv/luanti/mods")
        seen: list[Path] = []

        def record_validation(_manifests: object, mods_path: Path) -> None:
            seen.append(mods_path)

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            base = root / "config" / "base"
            base.mkdir(parents=True)
            (base / "world.conf").write_text("gameid = minetest\n", encoding="utf-8")

            with (
                patch.object(modconfig, "BASE_CONFIG", base),
                patch.object(modconfig, "GENERATED", root / "generated"),
                patch.object(modconfig, "configured_mods_path", return_value=expected),
                patch.object(modconfig, "load_manifests", return_value={}),
                patch.object(modconfig, "server_settings", return_value=[]),
                patch.object(modconfig, "validate", side_effect=record_validation),
            ):
                modconfig.generate("production")
                modconfig.verify("production")
                modconfig.status()

        self.assertEqual(seen, [expected, expected, expected])


if __name__ == "__main__":
    unittest.main()
