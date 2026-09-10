. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== evicting the ghost assignment ===" -ForegroundColor Yellow
Invoke-OnArcwin {
  "before: " + ((Get-ChildItem "C:\ProgramData\GuestConfig\Configuration" -Directory).Name -join ", ")
  Stop-Service gcarcservice -Force
  Start-Sleep -Seconds 4
  $t = "C:\ProgramData\GuestConfig\Configuration\AzureWindowsBaseline"
  if (Test-Path $t) { Remove-Item $t -Recurse -Force; "removed AzureWindowsBaseline" } else { "already absent" }
  Start-Service gcarcservice
  Start-Sleep -Seconds 10
  "after:  " + ((Get-ChildItem "C:\ProgramData\GuestConfig\Configuration" -Directory).Name -join ", ")
}
Write-Host "Queue is free. SetSecureProtocol should go Compliant in about 4-5 min." -ForegroundColor Green
Write-Host ""

