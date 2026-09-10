. C:\hccjp77\demo\_demo.ps1
Write-Title "D7  復旧 ─ machine configuration エージェントを再起動する"
Write-Host "  Restart-Service gcarcservice -Force" -ForegroundColor Yellow
Write-Host ""
Invoke-OnArc {
  Restart-Service gcarcservice -Force
  Start-Sleep -Seconds 5
  [PSCustomObject]@{ 'サービス' = 'gcarcservice'; '状態' = (Get-Service gcarcservice).Status }
} | Format-Table 'サービス','状態' -AutoSize
Write-Host ("  再起動しました: " + (Get-Date -Format "HH:mm:ss")) -ForegroundColor Green
Write-Host ""
Write-Host "  キューはリセットされます。ただし ─ これは解決策ではありません。" -ForegroundColor Yellow
Write-Host "  空になったあとの順番は制御できないので、重い監査が前に入り直せば" -ForegroundColor Gray
Write-Host "  結局その1周を待つことになります（実測: 再起動しても41分)。" -ForegroundColor Gray
Write-Host "  重い監査が先に入り直すと、その1周（実測38分41秒）を待つことになります。" -ForegroundColor Gray
Write-Host "  「直らない」のか「順番待ち」なのかは W-worker.ps1 / D6-queue.ps1 で見分けられます。" -ForegroundColor Gray
Write-Next "D8-verify.ps1" "数分おきに叩いて、OS の値が戻るのを待つ"
