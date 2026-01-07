#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Cron markers
CRON_MARKER_REFRESH="# specforge-refresh"
CRON_MARKER_URLS="# specforge-validate-urls"

remove_cron_entry() {
  local marker="$1"
  local name="$2"

  if ! command -v crontab >/dev/null 2>&1; then
    echo "crontab not available; skipping cron removal for $name."
    return 0
  fi
  local current
  current="$(crontab -l 2>/dev/null || true)"
  if ! echo "$current" | grep -q "${marker}"; then
    echo "Cron entry for $name not found."
    return 0
  fi
  echo "$current" | grep -v "${marker}" | crontab -
  echo "Cron entry for $name removed."
}

remove_cron() {
  remove_cron_entry "$CRON_MARKER_REFRESH" "refresh"
  remove_cron_entry "$CRON_MARKER_URLS" "url-validation"
}

remove_launchd_plist() {
  local plist_name="$1"
  local plist_target="${HOME}/Library/LaunchAgents/${plist_name}.plist"

  if [[ ! -f "$plist_target" ]]; then
    echo "Launchd agent ${plist_name} not found."
    return 0
  fi
  launchctl unload "$plist_target" >/dev/null 2>&1 || true
  rm -f "$plist_target"
  echo "Launchd agent ${plist_name} removed."
}

remove_launchd() {
  remove_launchd_plist "com.specforge.refresh"
  remove_launchd_plist "com.specforge.validate-urls"
}

case "$(uname -s)" in
  Darwin)
    remove_launchd
    ;;
  *)
    remove_cron
    ;;
esac

echo ""
echo "All SpecForge schedulers have been removed."
