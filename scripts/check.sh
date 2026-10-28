#!/usr/bin/env bash
# Lint, typecheck and test, as CI does. Run on Linux/macOS, or from Windows with:
#   wsl -e bash scripts/check.sh
# Uses $MANARA_VENV if set, else ~/.venvs/manara-home-integration (Python 3.14).
set -euo pipefail
cd "$(dirname "$0")/.."

V="${MANARA_VENV:-$HOME/.venvs/manara-home-integration}/bin"
if [ ! -x "$V/pytest" ]; then
  echo "No venv at ${V%/bin}. Create it with:" >&2
  echo "  uv venv -p 3.14 ${V%/bin} && VIRTUAL_ENV=${V%/bin} uv pip install -r requirements_test.txt" >&2
  exit 1
fi

"$V/ruff" check .
"$V/ruff" format --check .
"$V/mypy" custom_components
"$V/pytest" -q -p no:cacheprovider "$@"
