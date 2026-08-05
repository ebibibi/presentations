# arclnx01 (nginx) へデモ用の 1 枚ペラを配置する。Azure Arc の Run Command から実行される。
# __HTML_B64__ は deploy.sh が linux.html の base64 に置換する。
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive

# nginx が無ければ入れる (冪等)
if ! command -v nginx >/dev/null 2>&1; then
  apt-get update -qq
  apt-get install -y -qq nginx
fi

echo '__HTML_B64__' | base64 -d > /var/www/html/index.html
rm -f /var/www/html/index.nginx-debian.html

systemctl enable --now nginx
systemctl reload nginx

# ufw が有効なら 80 を開ける (既定は inactive なので通常は no-op)
if command -v ufw >/dev/null 2>&1 && ufw status | grep -q '^Status: active'; then
  ufw allow 80/tcp >/dev/null
fi

code=$(curl -s -o /dev/null -w '%{http_code}' http://localhost)
title=$(curl -s http://localhost | grep -o '<title>[^<]*' | sed 's/<title>//')
echo "status=$code title=$title"
