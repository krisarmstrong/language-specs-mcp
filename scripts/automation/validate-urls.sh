#!/bin/bash
# Weekly URL validation script for SpecForge MCP
# Validates all URLs in sources.json files and applies auto-fixes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

cd "$ROOT_DIR"

echo "=== SpecForge URL Validation Started at $(date) ==="

# Run URL validation
echo "Validating URLs..."
npm run validate:urls

# Apply auto-fixes for permanent redirects
echo "Applying auto-fixes..."
npm run fix:urls

# Regenerate health data with URL status
echo "Regenerating health data..."
npm run generate:health

echo "=== SpecForge URL Validation Completed at $(date) ==="
