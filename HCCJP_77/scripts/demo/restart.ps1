. C:\hccjp77\demo\_demo.ps1
# Just restarts the agent. No commentary - this is the one you type repeatedly
# during the demo to nudge the next evaluation instead of waiting out the timer.
$el = Get-Elapsed
if ($el) { Write-Title ("gcarcservice を再起動します　（巻き戻しから {0:N0} 分）" -f $el.TotalMinutes) }
else     { Write-Title "gcarcservice を再起動します" }

Invoke-OnArc {
  Restart-Service gcarcservice -Force
  Start-Sleep -Seconds 5
  "  gcarcservice: " + (Get-Service gcarcservice).Status
}
Write-Host ("  " + (Get-Date -Format "HH:mm:ss") + "  再起動しました") -ForegroundColor Green
Write-Host ""
Write-Host "  次の評価がすぐ始まります。1件あたり1分弱で順番に回ります。" -ForegroundColor Gray
Write-Host ""
