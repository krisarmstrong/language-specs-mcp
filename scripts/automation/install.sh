#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
CRON_MARKER="# specforge-refresh"
CRON_ENTRY="0 */4 * * * cd ${ROOT_DIR} && ./scripts/automation/refresh.sh >> refresh.log 2>&1 ${CRON_MARKER}"

install_cron() {
  if ! command -v crontab >/dev/null 2>&1; then
    echo "crontab not available; skipping cron install."
    return 0
  fi
  local current
  current="$(crontab -l 2>/dev/null || true)"
  if echo "$current" | grep -q "${CRON_MARKER}"; then
    echo "Cron entry already installed."
    return 0
  fi
  printf "%s\n%s\n" "$current" "$CRON_ENTRY" | crontab -
  echo "Cron entry installed."
}

install_launchd() {
  local plist_source="${ROOT_DIR}/docs/automation/com.specforge.refresh.plist"
  local plist_target="${HOME}/Library/LaunchAgents/com.specforge.refresh.plist"
  if [[ ! -f "$plist_source" ]]; then
    echo "Launchd plist template not found: $plist_source"
    return 1
  fi
  mkdir -p "${HOME}/Library/LaunchAgents"
  sed "s|__SPECFORGE_ROOT__|${ROOT_DIR}|g" "$plist_source" > "$plist_target"
  launchctl unload "$plist_target" >/dev/null 2>&1 || true
  launchctl load "$plist_target"
  echo "Launchd agent installed."
}

case "$(uname -s)" in
  Darwin)
    install_launchd
    ;;
  *)
    install_cron
    ;;
esac
