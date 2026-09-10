. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "*** RESTORING arcwin01 to T6-demo-ready (post-session cleanup) ***" -ForegroundColor Yellow
Invoke-OnLabHost {
  Restore-VMSnapshot -VMName arcwin01 -Name "T6-demo-ready" -Confirm:$false
  Start-Sleep -Seconds 2
  if ((Get-VM arcwin01).State -ne "Running") { Start-VM arcwin01 }
  (Get-VM arcwin01).State
}
Write-Host "Restored. Give it ~10 min, then all four assignments should read Compliant." -ForegroundColor Green
Write-Host ""

