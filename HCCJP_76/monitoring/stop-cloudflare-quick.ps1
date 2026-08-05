# Remove the temporary Windows public endpoint after the availability-test experiment.
param(
    [switch]$Purge
)

$ErrorActionPreference = 'Stop'
$taskName = 'HCCJP76CloudflaredQuick'

Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
"TASK_EXISTS=$([bool](Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue))"

if ($Purge) {
    Remove-Item 'C:\ProgramData\HCCJP76' -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item 'C:\Program Files\cloudflared' -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item 'C:\Windows\Temp\hccjp76-cloudflare-quick.ps1' -Force -ErrorAction SilentlyContinue
    'PURGED=true'
}
