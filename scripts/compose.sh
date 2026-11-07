#!/bin/sh
set -eu

PROFILE=${1:-}
case "$PROFILE" in
	local|production) ;;
	*)
		echo "Aufruf: $0 local|production <compose-argumente>" >&2
		exit 2
		;;
esac
shift

OVERRIDE="compose.$PROFILE.yaml"

if command -v podman-compose >/dev/null 2>&1; then
	exec podman-compose \
		-f compose.yaml \
		-f "$OVERRIDE" \
		"$@"
elif command -v docker >/dev/null 2>&1; then
	exec docker compose \
		-f compose.yaml \
		-f "$OVERRIDE" \
		"$@"
else
	echo "Weder podman-compose noch docker compose wurde gefunden." >&2
	exit 127
fi
