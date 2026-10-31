#!/bin/sh
set -eu

if command -v podman-compose >/dev/null 2>&1; then
	exec podman-compose \
		-f compose.yaml \
		-f compose.local.yaml \
		"$@"
elif command -v docker >/dev/null 2>&1; then
	exec docker compose \
		-f compose.yaml \
		-f compose.local.yaml \
		"$@"
else
	echo "Weder podman-compose noch docker compose wurde gefunden." >&2
	exit 127
fi
