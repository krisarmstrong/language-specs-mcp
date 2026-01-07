#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

# Cron markers
CRON_MARKER_REFRESH="# specforge-refresh"
CRON_MARKER_URLS="# specforge-validate-urls"

# Cron entries (refresh every 4 hours, URL validation weekly on Sundays at 3 AM)
CRON_ENTRY_REFRESH="0 */4 * * * cd ${ROOT_DIR} && ./scripts/automation/refresh.sh >> refresh.log 2>&1 ${CRON_MARKER_REFRESH}"
CRON_ENTRY_URLS="0 3 * * 0 cd ${ROOT_DIR} && ./scripts/automation/validate-urls.sh >> validate-urls.log 2>&1 ${CRON_MARKER_URLS}"

install_cron_entry() {
  local marker="$1"
  local entry="$2"
  local name="$3"

  if ! command -v crontab >/dev/null 2>&1; then
    echo "crontab not available; skipping cron install for $name."
    return 0
  fi
  local current
  current="$(crontab -l 2>/dev/null || true)"
  if echo "$current" | grep -q "${marker}"; then
    echo "Cron entry for $name already installed."
    return 0
  fi
  printf "%s\n%s\n" "$current" "$entry" | crontab -
  echo "Cron entry for $name installed."
}

install_cron() {
  install_cron_entry "$CRON_MARKER_REFRESH" "$CRON_ENTRY_REFRESH" "refresh"
  install_cron_entry "$CRON_MARKER_URLS" "$CRON_ENTRY_URLS" "url-validation"
}

install_launchd_plist() {
  local plist_name="$1"
  local plist_source="${ROOT_DIR}/docs/automation/${plist_name}.plist"
  local plist_target="${HOME}/Library/LaunchAgents/${plist_name}.plist"

  if [[ ! -f "$plist_source" ]]; then
    echo "Launchd plist template not found: $plist_source"
    return 1
  fi
  mkdir -p "${HOME}/Library/LaunchAgents"
  sed "s|__SPECFORGE_ROOT__|${ROOT_DIR}|g" "$plist_source" > "$plist_target"
  launchctl unload "$plist_target" >/dev/null 2>&1 || true
  launchctl load "$plist_target"
  echo "Launchd agent ${plist_name} installed."
}

install_launchd() {
  # Install main refresh agent (every 4 hours)
  install_launchd_plist "com.specforge.refresh"

  # Install URL validation agent (weekly)
  install_launchd_plist "com.specforge.validate-urls"
}

# Make scripts executable
chmod +x "${ROOT_DIR}/scripts/automation/refresh.sh"
chmod +x "${ROOT_DIR}/scripts/automation/validate-urls.sh"

case "$(uname -s)" in
  Darwin)
    install_launchd
    ;;
  *)
    install_cron
    ;;
esac

echo ""
echo "Installed schedulers:"
echo "  - Refresh: Every 4 hours (delta fetch + generation)"
echo "  - URL Validation: Weekly on Sundays at 3 AM"
