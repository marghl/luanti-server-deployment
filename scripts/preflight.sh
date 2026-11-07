#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR/.."

PROFILE=${1:-}
case "$PROFILE" in
	local)
		exit 0
		;;
	production)
		;;
	*)
		echo "Aufruf: $0 local|production" >&2
		exit 2
		;;
esac

if [ ! -s .env ]; then
	echo "FEHLER: Produktion erfordert eine nicht leere .env-Datei." >&2
	exit 1
fi

for secret in secrets/server.conf secrets/mapserver.conf secrets/lorebridge.conf; do
	if [ ! -s "$secret" ]; then
		echo "FEHLER: Produktion erfordert die nicht leere Datei $secret." >&2
		exit 1
	fi
done

for key in SERVICE_UID SERVICE_GID LUANTI_RUNTIME_PATH LUANTI_WORLD_PATH LUANTI_GAME_PATH LUANTI_MODS_PATH LUANTI_MOD_DATA_PATH MAPSERVER_DATA_PATH GRAFANA_ADMIN_PASSWORD; do
	if ! grep -Eq "^${key}=.+" .env; then
		echo "FEHLER: Produktion erfordert $key in .env." >&2
		exit 1
	fi
done

if grep -Eq '^GRAFANA_ADMIN_PASSWORD=(admin|<.*>)$' .env; then
	echo "FEHLER: Unsicheres GRAFANA_ADMIN_PASSWORD in .env." >&2
	exit 1
fi
