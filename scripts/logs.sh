#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR/.."
PROFILE=${1:-}
if [ "$#" -gt 0 ]; then
	shift
fi
exec ./scripts/compose.sh "$PROFILE" logs "$@"
