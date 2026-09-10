. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== RECOVERY: restart the machine configuration agent ===" -ForegroundColor Yellow
Write-Host "The evaluation queue is serial. A heavy baseline audit can hold it for 40+ min," -ForegroundColor Gray
Write-Host "which looks exactly like 'auto-correct is broken'. Restarting resets the queue." -ForegroundColor Gray
Write-Host ""
Invoke-OnArcwin {
  Restart-Service gcarcservice -Force
  Start-Sleep -Seconds 5
  (Get-Service gcarcservice).Status
}
Write-Host ("Restarted at {0}. Expect everything green in 4-6 min." -f (Get-Date -Format "HH:mm:ss")) -ForegroundColor Green
Write-Host ""

