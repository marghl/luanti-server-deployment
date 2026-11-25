#!/usr/bin/env python3
"""Regression tests for shared checkout manifest consistency."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "modconfig.py"
SPEC = importlib.util.spec_from_file_location("modconfig_consistency", SCRIPT)
assert SPEC and SPEC.loader
modconfig = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(modconfig)


def manifest(name: str, commit: str) -> dict[str, str]:
    return {
        "name": name,
        "enabled": "true",
        "checkout": "shared",
        "path": f"shared/{name}",
        "source": "git",
        "git_url": "https://github.com/example/shared.git",
        "git_commit": commit,
    }


class CheckoutConsistencyTest(unittest.TestCase):
    def test_shared_checkout_accepts_identical_revision(self) -> None:
        commit = "a" * 40
        groups = modconfig.checkout_groups({
            "one": manifest("one", commit),
            "two": manifest("two", commit),
        })
        self.assertEqual(set(groups), {"shared"})

    def test_shared_checkout_reports_every_conflicting_revision(self) -> None:
        with self.assertRaises(SystemExit) as raised:
            modconfig.checkout_groups({
                "one": manifest("one", "a" * 40),
                "two": manifest("two", "b" * 40),
            })
        message = str(raised.exception)
        self.assertIn("widerspruechliche Git-URL oder Commits", message)
        self.assertIn("one=https://github.com/example/shared.git@" + "a" * 40, message)
        self.assertIn("two=https://github.com/example/shared.git@" + "b" * 40, message)


if __name__ == "__main__":
    unittest.main()
