#!/usr/bin/env python3
"""Fetch only stale or missing specs."""

from __future__ import annotations

import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SPECS_ROOT = SCRIPT_DIR.parent / "specs"

TASKS = [
    "fetch:assembly",
    "fetch:basic",
    "fetch:bash",
    "fetch:batch",
    "fetch:c",
    "fetch:cpp",
    "fetch:csharp",
    "fetch:css",
    "fetch:go",
    "fetch:html",
    "fetch:git",
    "fetch:javascript",
    "fetch:java",
    "fetch:kotlin",
    "fetch:lua",
    "fetch:powershell",
    "fetch:python",
    "fetch:rust",
    "fetch:sql",
    "fetch:swift",
    "fetch:typescript",
    "fetch:php",
    "fetch:ruby",
    "fetch:dart",
    "fetch:r",
    "fetch:julia",
    "fetch:scala",
    "fetch:elixir",
    "fetch:clojure",
    "fetch:haskell",
    "fetch:zig",
    "fetch:ocaml",
    "fetch:markdown",
    "fetch:yaml",
    "fetch:dockerfile",
]

TASK_BY_LANGUAGE = {task.replace("fetch:", ""): task for task in TASKS}

SCOPE = os.getenv("FETCH_SCOPE", "all")
ENV_CONCURRENCY = int(os.getenv("FETCH_CONCURRENCY", "2"))
STALE_DAYS = int(os.getenv("FETCH_DELTA_DAYS", "30"))
TASK_TIMEOUT = int(os.getenv("FETCH_TASK_TIMEOUT_MS", "1200000")) / 1000
TASK_KILL_GRACE = int(os.getenv("FETCH_TASK_KILL_MS", "30000")) / 1000


def parse_max_concurrency(args: list[str]) -> int | None:
    for idx, arg in enumerate(args):
        if arg == "--max-concurrency" and idx + 1 < len(args):
            try:
                value = int(args[idx + 1])
            except ValueError:
                return None
            return value if value > 0 else None
        if arg.startswith("--max-concurrency="):
            try:
                value = int(arg.split("=", 1)[1])
            except ValueError:
                return None
            return value if value > 0 else None
    return None


def read_fetched_at(language: str) -> datetime | None:
    path = SPECS_ROOT / language / ".fetched-at"
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8").strip()
    if not content:
        return None
    try:
        return datetime.fromisoformat(content.replace("Z", "+00:00"))
    except ValueError:
        return None


def run_task(task: str) -> None:
    env = os.environ.copy()
    env["FETCH_SCOPE"] = SCOPE
    sys.stdout.write(f"Starting {task} (scope={SCOPE})...\n")
    sys.stdout.flush()

    process = subprocess.Popen(["npm", "run", task], env=env)
    start = time.monotonic()
    while True:
        code = process.poll()
        if code is not None:
            if code != 0:
                raise RuntimeError(f"{task} failed with code {code}")
            return
        if TASK_TIMEOUT > 0 and time.monotonic() - start > TASK_TIMEOUT:
            process.terminate()
            try:
                process.wait(timeout=TASK_KILL_GRACE)
            except subprocess.TimeoutExpired:
                process.kill()
            raise TimeoutError(f"{task} timed out")
        time.sleep(1)


def main() -> None:
    cutoff = datetime.now(timezone.utc) - timedelta(days=STALE_DAYS)

    languages = sorted(
        [entry.name for entry in SPECS_ROOT.iterdir() if entry.is_dir()]
    )

    stale_tasks: list[str] = []
    for language in languages:
        fetched_at = read_fetched_at(language)
        if fetched_at is None or fetched_at < cutoff:
            task = TASK_BY_LANGUAGE.get(language)
            if task:
                stale_tasks.append(task)

    if not stale_tasks:
        sys.stdout.write("All specs are fresh. No fetch required.\n")
        return

    max_concurrency = parse_max_concurrency(sys.argv[1:])
    concurrency = max_concurrency or ENV_CONCURRENCY

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {executor.submit(run_task, task): task for task in stale_tasks}
        for future in as_completed(futures):
            future.result()

    subprocess.run(["npm", "run", "stamp:versions"], check=True)


if __name__ == "__main__":
    main()
