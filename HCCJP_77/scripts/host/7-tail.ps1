. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== gc_agent.log : what the agent is doing right now ===" -ForegroundColor Cyan
Invoke-OnArcwin {
  $log = "C:\ProgramData\GuestConfig\arc_policy_logs\gc_agent.log"
  if (-not (Test-Path $log)) { "no log yet"; return }
  Get-Content $log -Tail 120 |
    Where-Object { $_ -match "consistency|Compliant|timer trigger|next trigger|ERROR|WARN" } |
    Select-Object -Last 30
}
Write-Host ""

