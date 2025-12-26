#!/usr/bin/env bash
set -euo pipefail

BOOTSTRAP="${BOOTSTRAP:-localhost:9092}"

echo "[INFO] Creating topics on $BOOTSTRAP"
# Using rpk via docker (no local install)
docker run --rm --network host redpandadata/redpanda:latest   rpk topic create logs.app.demo logs.system.demo logs.security.demo --brokers "$BOOTSTRAP" || true
