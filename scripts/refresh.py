#!/usr/bin/env python3
"""Refresh the MCP data by running delta fetches and generation tasks."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
COMMANDS = [
    ["npm", "run", "fetch:delta"],
    ["npm", "run", "generate:all"],
]


def run(command: list[str]) -> None:
    print(f"Running: {' '.join(command)}", flush=True)
    subprocess.run(command, check=True, cwd=ROOT_DIR)


def main() -> int:
    for command in COMMANDS:
        try:
            run(command)
        except subprocess.CalledProcessError as error:
            print(f"Command failed ({' '.join(command)}): {error}", file=sys.stderr)
            return error.returncode or 1
    print("Refresh completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
