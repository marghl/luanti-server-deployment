#!/bin/sh
set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$SCRIPT_DIR/.."

./scripts/modconfig.sh generate local
./scripts/modconfig.sh generate production
./scripts/modconfig.sh verify local
./scripts/modconfig.sh verify production

grep -q '^server_announce = false$' generated/local/server.conf
grep -q '^creative_mode = true$' generated/local/server.conf
grep -q '^lore.wiki_public_url = http://localhost:8082$' generated/local/server.conf

grep -q '^server_announce = true$' generated/production/server.conf
grep -q '^creative_mode = false$' generated/production/server.conf
grep -q '^disallow_empty_password = true$' generated/production/server.conf
grep -q '^lore.wiki_public_url = https://wiki.marghl.de$' generated/production/server.conf

if grep -qi 'lokale Wiederherstellung' generated/production/server.conf; then
	echo 'Lokale Serverbezeichnung ist in die Produktionskonfiguration gelangt.' >&2
	exit 1
fi

cmp generated/local/world.mt generated/production/world.mt
