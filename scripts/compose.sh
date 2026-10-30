#!/bin/sh
set -eu

if command -v podman >/dev/null 2>&1; then
	CONTAINER_TOOL=podman
elif command -v docker >/dev/null 2>&1; then
	CONTAINER_TOOL=docker
else
	echo "Weder podman noch docker wurde gefunden." >&2
	exit 127
fi

exec "$CONTAINER_TOOL" compose \
	-f compose.yaml \
	-f compose.local.yaml \
	"$@"
