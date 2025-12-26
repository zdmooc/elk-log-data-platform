#!/usr/bin/env bash
set -euo pipefail

ES="${ES:-http://localhost:9200}"

echo "[INFO] Apply ILM policy"
curl -sS -X PUT "$ES/_ilm/policy/logs-hot-warm-cold" -H 'Content-Type: application/json'   --data-binary @elastic/ilm/ilm-hot-warm-cold.json | jq .

echo "[INFO] Apply index templates"
for f in elastic/index-templates/*.json; do
  name="$(basename "$f" .json)"
  curl -sS -X PUT "$ES/_index_template/$name" -H 'Content-Type: application/json'     --data-binary @"$f" | jq .
done

echo "[INFO] Kibana assets are provided as NDJSON exports (import manually for local demo)."
