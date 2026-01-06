#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CRON_MARKER="# specforge-refresh"

remove_cron() {
  if ! command -v crontab >/dev/null 2>&1; then
    echo "crontab not available; skipping cron removal."
    return 0
  fi
  local current
  current="$(crontab -l 2>/dev/null || true)"
  if ! echo "$current" | grep -q "${CRON_MARKER}"; then
    echo "Cron entry not found."
    return 0
  fi
  echo "$current" | grep -v "${CRON_MARKER}" | crontab -
  echo "Cron entry removed."
}

remove_launchd() {
  local plist_target="${HOME}/Library/LaunchAgents/com.specforge.refresh.plist"
  if [[ ! -f "$plist_target" ]]; then
    echo "Launchd agent not found."
    return 0
  fi
  launchctl unload "$plist_target" >/dev/null 2>&1 || true
  rm -f "$plist_target"
  echo "Launchd agent removed."
}

case "$(uname -s)" in
  Darwin)
    remove_launchd
    ;;
  *)
    remove_cron
    ;;
esac
