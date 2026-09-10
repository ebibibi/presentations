. C:\hccjp77\_lab.ps1
Write-Host ""
Write-Host "=== breaking arcwin01 on purpose (T7 seed) ===" -ForegroundColor Yellow
Invoke-OnArcwin {
  $p = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
  "before: tz=" + (Get-TimeZone).Id + " tls12=" + (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled

  Set-TimeZone -Id "UTC"
  Remove-ItemProperty -Path $p -Name Enabled -Force -EA SilentlyContinue

  $tls = (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled
  "after:  tz=" + (Get-TimeZone).Id + " tls12=" + $(if ($null -eq $tls) { "(deleted)" } else { $tls })
}
Write-Host ""
Write-Host "Two assignments now see a broken machine:" -ForegroundColor Cyan
Write-Host "  AuditSecureProtocol (Audit)            -> will report NonCompliant, will NOT fix" -ForegroundColor Gray
Write-Host "  SetSecureProtocol   (ApplyAndAutoCorrect) -> will report NonCompliant, then fix it" -ForegroundColor Gray
Write-Host "  SetWindowsTimeZone  (ApplyAndAutoCorrect) -> will put Tokyo back" -ForegroundColor Gray
Write-Host ""

