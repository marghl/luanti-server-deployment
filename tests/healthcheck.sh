#!/bin/sh
set -eu

curl --fail --silent --show-error "http://localhost:${HTTP_PORT:-8080}/health"
