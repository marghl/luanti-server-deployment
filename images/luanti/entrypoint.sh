#!/bin/sh
set -eu

cat /etc/minetest/minetest.conf \
	/run/secrets/mapserver.conf \
	/run/secrets/lorebridge.conf > /tmp/minetest.conf

exec /usr/local/bin/luantiserver "$@"
