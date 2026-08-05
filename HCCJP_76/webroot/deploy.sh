#!/usr/bin/env bash
# HCCJP 第76回デモ用の 1 枚ペラを、Azure Arc の Run Command 経由で両サーバーへ配る。
#
# 配布に SSH も RDP も使わない。Azure の Run Command だけで完結する
# (＝当日デモで見せる「誰もログインせずに直す」経路を、そのまま準備にも使っている)。
#
# ペイロード (deploy-windows.ps1 / deploy-linux.sh) は別ファイルにして、置換するのは
# HTML の base64 だけにしている。シェルの変数展開でスクリプトが壊れるのを避けるため。
#
# 使い方:
#   ./deploy.sh            # 両方へ配る
#   ./deploy.sh windows    # Windows だけ
#   ./deploy.sh linux      # Linux だけ
set -euo pipefail

SUB="${ARC_SUBSCRIPTION_ID:-b0f2ddcb-c22b-4728-89b3-26e90a494ae4}"
RG="${ARC_RESOURCE_GROUP:-rg-hccjp76-arc}"
LOC="${ARC_LOCATION:-japaneast}"
WIN_VM="${ARC_WINDOWS_MACHINE:-arcwin01}"
LNX_VM="${ARC_LINUX_MACHINE:-arclnx01}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ペイロードの __HTML_B64__ を実際の base64 に差し替えて Run Command へ渡す。
build_script() {
  local payload="$1" html="$2" b64
  b64="$(base64 -w0 "$html")"
  python3 - "$payload" "$b64" <<'PY'
import sys, pathlib
payload, b64 = sys.argv[1], sys.argv[2]
sys.stdout.write(pathlib.Path(payload).read_text(encoding="utf-8").replace("__HTML_B64__", b64))
PY
}

run_command() {
  local machine="$1" script="$2" name="hccjp76-deploy-web"
  # create は PUT (upsert) なので、同名が残っていてもそのまま上書きできる。
  # 先に delete すると、削除完了前に create のポーリングが走って ResourceNotFound で落ちる。
  az connectedmachine run-command create --name "$name" --machine-name "$machine" \
      --resource-group "$RG" --subscription "$SUB" --location "$LOC" \
      --script "$script" \
      --query "{state:instanceView.executionState,exit:instanceView.exitCode,out:instanceView.output,err:instanceView.error}" -o json
}

deploy_windows() {
  echo "==> $WIN_VM (IIS) へ配布"
  run_command "$WIN_VM" "$(build_script "$HERE/deploy-windows.ps1" "$HERE/windows.html")"
}

deploy_linux() {
  echo "==> $LNX_VM (nginx) へ配布"
  run_command "$LNX_VM" "$(build_script "$HERE/deploy-linux.sh" "$HERE/linux.html")"
}

case "${1:-all}" in
  windows) deploy_windows ;;
  linux)   deploy_linux ;;
  all)     deploy_windows; deploy_linux ;;
  *) echo "使い方: $0 [all|windows|linux]" >&2; exit 2 ;;
esac
