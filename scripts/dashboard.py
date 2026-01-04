#!/usr/bin/env python3
"""Serve the static docs/site health dashboard."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT_DIR / "docs" / "site"
GENERATE_HEALTH = ROOT_DIR / "scripts" / "generate-health.py"


class _DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, directory: str | Path = SITE_DIR, **kwargs):
        super().__init__(*args, directory=str(directory), **kwargs)

    def log_message(self, format: str, *args) -> None:
        sys.stdout.write(f"{self.address_string()} - {format % args}\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the MCP health dashboard.")
    parser.add_argument("--port", type=int, default=int(os.getenv("DASHBOARD_PORT", "9000")))
    args = parser.parse_args()

    subprocess.run([sys.executable, str(GENERATE_HEALTH)], check=True)

    server = ThreadingHTTPServer(("0.0.0.0", args.port), partial(_DashboardHandler))
    print(f"Serving MCP dashboard at http://localhost:{args.port}/health.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down dashboard.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
