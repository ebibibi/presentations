. C:\hccjp77\demo\_demo.ps1
Write-Title "D1  いまの arcwin01 ─ 巻き戻す前の、正常な姿"

Write-Host "【1】OS の中の実際の値" -ForegroundColor Cyan
Show-OsTruth

Write-Host "【2】このマシンが持っている machine configuration の割り当て" -ForegroundColor Cyan
Write-Host "     C:\ProgramData\GuestConfig\Configuration\" -ForegroundColor DarkGray
Write-Host ""
Invoke-OnArc {
  Get-ChildItem "C:\ProgramData\GuestConfig\Configuration" -Directory | ForEach-Object {
    $mc = Join-Path $_.FullName ($_.Name + ".metaconfig.json")
    $j  = if (Test-Path $mc) { Get-Content $mc -Raw | ConvertFrom-Json } else { $null }
    [PSCustomObject]@{
      '割り当て' = $_.Name
      'モード'   = $j.configurationMode
      '評価間隔' = "$($j.configurationModeFrequencyMins) 分"
      '直すか'   = if ($j.configurationMode -eq 'ApplyAndMonitor') { '直す' } else { '直さない' }
    }
  }
} | Format-Table '割り当て','モード','評価間隔','直すか' -AutoSize

Write-Host "  ※ 拡張機能ではありません。Connected Machine agent の中に入っています" -ForegroundColor DarkGray
Write-Host "  ※ 評価間隔は推定ではなく metaconfig.json に書いてある設定値です" -ForegroundColor DarkGray
Write-Host "  ※ 準備中はここに5つ目（AzureWindowsBaseline）がいました。テナント既定の" -ForegroundColor DarkGray
Write-Host "     「Azure セキュリティ ベンチマーク」が入れたものです。評価キューを占有して" -ForegroundColor DarkGray
Write-Host "     全部を止めるので、今日のデモに限って一時的に無効にしてあります" -ForegroundColor DarkGray
Write-Host "     （デモの都合です。本番で外すものではありません）" -ForegroundColor DarkGray

Write-Next "D2-mark.ps1  ← 「実行中」を確認してから叩く" "Hyper-V マネージャーで巻き戻す" @(
  "1. 中央の一覧で  arcwin01  を選ぶ",
  "2. 下の［チェックポイント］で  T7-demo-start  を右クリック →［適用］",
  "3. ダイアログは［適用］を選ぶ",
  "   （［チェックポイントの作成と適用］は選ばない）",
  "4. ⚠️ ここで VM の状態が「オフ」になります。適用しただけでは起動しません",
  "5. arcwin01 を右クリック →［起動］",
  "6. 状態が「実行中」になったのを確認する"
)
