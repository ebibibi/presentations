. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== creating T7-demo-start (VM is shut down first, like a backup image) ===" -ForegroundColor Yellow
Invoke-OnLabHost {
  Stop-VM -Name arcwin01 -Force
  (Get-VM arcwin01).State
  Checkpoint-VM -Name arcwin01 -SnapshotName "T7-demo-start"
  Start-VM -Name arcwin01
  Get-VMSnapshot -VMName arcwin01 | Select-Object Name, ParentSnapshotName, CreationTime | Format-Table -AutoSize
}
Write-Host ""

