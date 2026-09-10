. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== arcwin01 : the OS truth (out-of-band, PowerShell Direct) ===" -ForegroundColor Cyan
Invoke-OnArcwin {
  $tzPath = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
  $tls12  = (Get-ItemProperty $tzPath -Name Enabled -EA SilentlyContinue).Enabled
  $crypto = (Get-ItemProperty "HKLM:\SOFTWARE\WOW6432Node\Microsoft\.NETFramework\v4.0.30319" -Name SchUseStrongCrypto -EA SilentlyContinue).SchUseStrongCrypto
  $mp = Get-MpPreference -EA SilentlyContinue
  $agent = (& "$env:ProgramFiles\AzureConnectedMachineAgent\azcmagent.exe" show -j 2>$null) -join "" | ConvertFrom-Json
  [PSCustomObject]@{
    TimeZone       = (Get-TimeZone).Id
    'TLS12_Server' = $(if ($null -eq $tls12) { "(no value)" } else { $tls12 })
    StrongCrypto   = $(if ($null -eq $crypto) { "(no value)" } else { $crypto })
    CFA            = $mp.EnableControlledFolderAccess
    ASR_Rules      = ($mp.AttackSurfaceReductionRules_Ids | Measure-Object).Count
    AgentStatus    = $agent.status
    LastHeartbeat  = $agent.lastHeartbeat
    LastBoot       = (Get-CimInstance Win32_OperatingSystem).LastBootUpTime
  } | Format-List
}
Write-Host ""

