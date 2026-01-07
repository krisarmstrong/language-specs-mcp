#!/usr/bin/env python3
"""Refresh the MCP data by running delta fetches and generation tasks.

Environment Variables:
    VALIDATE_URLS: Set to "1" to include URL validation (slower but thorough)
    SKIP_FETCH: Set to "1" to skip fetching (useful for local testing)
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

# Core refresh commands
COMMANDS = [
    ["npm", "run", "fetch:delta"],
    ["npm", "run", "update:versions"],
    ["npm", "run", "stamp:versions"],
    ["npm", "run", "generate:all"],
]

# URL validation commands (optional, slower)
URL_VALIDATION_COMMANDS = [
    ["npm", "run", "validate:urls"],
    ["npm", "run", "fix:urls"],  # Apply auto-fixes
]


def run(command: list[str]) -> None:
    print(f"Running: {' '.join(command)}", flush=True)
    subprocess.run(command, check=True, cwd=ROOT_DIR)


def main() -> int:
    skip_fetch = os.getenv("SKIP_FETCH") == "1"
    validate_urls = os.getenv("VALIDATE_URLS") == "1"

    commands = []

    if skip_fetch:
        print("Skipping fetch (SKIP_FETCH=1)")
        # Still run generation tasks
        commands = [
            ["npm", "run", "update:versions"],
            ["npm", "run", "stamp:versions"],
            ["npm", "run", "generate:all"],
        ]
    else:
        commands = COMMANDS.copy()

    # Add URL validation if requested
    if validate_urls:
        print("URL validation enabled (VALIDATE_URLS=1)")
        commands.extend(URL_VALIDATION_COMMANDS)
        # Re-run generate:health to include URL status
        commands.append(["npm", "run", "generate:health"])

    for command in commands:
        try:
            run(command)
        except subprocess.CalledProcessError as error:
            print(f"Command failed ({' '.join(command)}): {error}", file=sys.stderr)
            # URL validation failures shouldn't stop the whole refresh
            if "validate:urls" in command or "fix:urls" in command:
                print("URL validation error - continuing with refresh", file=sys.stderr)
                continue
            return error.returncode or 1

    print("Refresh completed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
