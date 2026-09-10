. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== checkpoints on arcwin01 ===" -ForegroundColor Cyan
Invoke-OnLabHost { Get-VMSnapshot -VMName arcwin01 | Select-Object Name, CreationTime } | Format-Table -AutoSize
Write-Host "=== assignments the MACHINE thinks it has ===" -ForegroundColor Cyan
Invoke-OnArcwin { (Get-ChildItem "C:\ProgramData\GuestConfig\Configuration" -Directory -EA SilentlyContinue).Name } |
  ForEach-Object { "  $_" }
Write-Host ""

