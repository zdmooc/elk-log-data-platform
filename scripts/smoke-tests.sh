#!/usr/bin/env bash
set -euo pipefail

ES="${ES:-http://localhost:9200}"

echo "[INFO] Checking Elasticsearch"
curl -sS "$ES" | jq . > /dev/null

echo "[INFO] Listing indices"
curl -sS "$ES/_cat/indices?v" | head -n 20
