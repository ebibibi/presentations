. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "*** ROLLING BACK arcwin01 to T7-demo-start ***" -ForegroundColor Yellow
$t = Get-Date
Invoke-OnLabHost {
  Restore-VMSnapshot -VMName arcwin01 -Name "T7-demo-start" -Confirm:$false
  Start-Sleep -Seconds 2
  if ((Get-VM arcwin01).State -ne "Running") { Start-VM arcwin01 }
  (Get-VM arcwin01).State
}
Write-Host ("DONE at {0}  (elapsed {1:N1}s)" -f (Get-Date -Format "HH:mm:ss"), ((Get-Date)-$t).TotalSeconds) -ForegroundColor Green
Write-Host ""
Write-Host "Expected: Azure stays green for ~8 min, then 3 assignments go red at 9-12 min." -ForegroundColor Cyan
Write-Host "They will NOT self-heal quickly - the queue is blocked. Run 8-recover.ps1 to unblock." -ForegroundColor Cyan
Write-Host ""

