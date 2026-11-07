#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR/.."

PROFILE=${1:-}
case "$PROFILE" in
	local|production) ;;
	*)
		echo "Aufruf: $0 local|production" >&2
		exit 2
		;;
esac

./scripts/preflight.sh "$PROFILE"
./scripts/modconfig.sh generate "$PROFILE"
./scripts/modconfig.sh verify "$PROFILE"
exec ./scripts/compose.sh "$PROFILE" up -d --force-recreate
