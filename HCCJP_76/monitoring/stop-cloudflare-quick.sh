#!/usr/bin/env bash
# Remove the temporary public endpoint after the availability-test experiment.
set -euo pipefail

UNIT=hccjp76-cloudflared-quick.service
systemctl stop "$UNIT" 2>/dev/null || true
systemctl reset-failed "$UNIT" 2>/dev/null || true
systemctl is-active "$UNIT" 2>/dev/null || true
