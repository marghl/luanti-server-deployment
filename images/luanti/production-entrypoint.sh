#!/bin/sh
set -eu

world_mt=/var/lib/minetest/.minetest/worlds/marghl/world.mt
overrides=/etc/minetest/world.production.mt
tmp_world_mt="${world_mt}.tmp"

if [ ! -f "$world_mt" ]; then
	printf 'Produktive world.mt fehlt: %s\n' "$world_mt" >&2
	exit 1
fi

awk '
	NR == FNR {
		if ($0 ~ /^[[:space:]]*(#|$)/) next
		key = $0
		sub(/[[:space:]]*=.*/, "", key)
		managed[key] = 1
		override[++count] = $0
		next
	}
	{
		key = $0
		sub(/[[:space:]]*=.*/, "", key)
		if (!(key in managed)) print
	}
	END {
		for (i = 1; i <= count; i++) print override[i]
	}
' "$overrides" "$world_mt" > "$tmp_world_mt"

chmod --reference="$world_mt" "$tmp_world_mt"
mv "$tmp_world_mt" "$world_mt"

exec /usr/local/bin/entrypoint.sh "$@"
