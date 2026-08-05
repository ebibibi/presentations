# Start a temporary Cloudflare Quick Tunnel for the HCCJP 76 Windows availability experiment.
# This is intentionally a rehearsal helper, not the stable endpoint used on event day.
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$root = 'C:\ProgramData\HCCJP76'
$cloudflaredDir = 'C:\Program Files\cloudflared'
$cloudflared = Join-Path $cloudflaredDir 'cloudflared.exe'
$launcher = Join-Path $root 'start-cloudflared.cmd'
$log = Join-Path $root 'cloudflared-quick.log'
$taskName = 'HCCJP76CloudflaredQuick'

New-Item -ItemType Directory -Path $root -Force | Out-Null
New-Item -ItemType Directory -Path $cloudflaredDir -Force | Out-Null

if (-not (Test-Path $cloudflared)) {
    Invoke-WebRequest `
        -Uri 'https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe' `
        -OutFile $cloudflared `
        -UseBasicParsing
}

Stop-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue
Remove-Item $log -Force -ErrorAction SilentlyContinue

$launcherContent = @"
@echo off
"$cloudflared" tunnel --no-autoupdate --url http://127.0.0.1:80 > "$log" 2>&1
"@
Set-Content -Path $launcher -Value $launcherContent -Encoding ASCII

$action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument "/c `"$launcher`""
$trigger = New-ScheduledTaskTrigger -AtStartup
$principal = New-ScheduledTaskPrincipal -UserId 'SYSTEM' -LogonType ServiceAccount -RunLevel Highest
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal -Force | Out-Null
Start-ScheduledTask -TaskName $taskName

for ($attempt = 0; $attempt -lt 30; $attempt++) {
    Start-Sleep -Seconds 2
    if (Test-Path $log) {
        $text = Get-Content -Path $log -Raw -ErrorAction SilentlyContinue
        $match = [regex]::Match($text, 'https://[a-z0-9-]+\.trycloudflare\.com')
        if ($match.Success) {
            $url = $match.Value
            $response = Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 20
            "PUBLIC_URL=$url"
            "PUBLIC_HTTP=$($response.StatusCode)"
            "TASK_STATE=$((Get-ScheduledTask -TaskName $taskName).State)"
            exit 0
        }
    }
}

if (Test-Path $log) {
    Get-Content -Path $log -Tail 80
}
throw 'Cloudflare Quick Tunnel URL was not created within 60 seconds.'
