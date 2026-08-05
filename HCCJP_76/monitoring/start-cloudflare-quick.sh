#!/usr/bin/env bash
# Start a temporary Cloudflare Quick Tunnel for the HCCJP 76 availability-test experiment.
# This is intentionally a rehearsal helper, not the stable endpoint used on event day.
set -euo pipefail

CLOUDFLARED=/usr/local/bin/cloudflared
UNIT=hccjp76-cloudflared-quick.service

if [[ ! -x "$CLOUDFLARED" ]]; then
  curl -fsSL --retry 3 \
    -o "$CLOUDFLARED" \
    https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64
  chmod 0755 "$CLOUDFLARED"
fi

systemctl stop "$UNIT" 2>/dev/null || true
systemctl reset-failed "$UNIT" 2>/dev/null || true

systemd-run \
  --unit="${UNIT%.service}" \
  --property=Restart=on-failure \
  --property=RestartSec=5 \
  "$CLOUDFLARED" tunnel --no-autoupdate --url http://127.0.0.1:80 >/dev/null

for _ in $(seq 1 30); do
  url="$({ journalctl -u "$UNIT" --no-pager -o cat 2>/dev/null || true; } \
    | sed -n 's|.*\(https://[a-z0-9-]*\.trycloudflare\.com\).*|\1|p' \
    | tail -1)"
  if [[ -n "$url" ]]; then
    printf 'PUBLIC_URL=%s\n' "$url"
    curl -fsS -o /dev/null -w 'PUBLIC_HTTP=%{http_code}\n' "$url"
    systemctl is-active "$UNIT"
    exit 0
  fi
  sleep 2
done

journalctl -u "$UNIT" --no-pager -n 80
exit 1
