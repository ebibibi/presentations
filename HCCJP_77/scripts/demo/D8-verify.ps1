. C:\hccjp77\demo\_demo.ps1
$el = Get-Elapsed
if ($el) { Write-Title ("D8  巻き戻しから {0:N0} 分 ─ 戻ったか" -f $el.TotalMinutes) }
else     { Write-Title "D8  戻ったか" }

$r = Invoke-OnArc {
  $p = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
  $tls = (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled
  [PSCustomObject]@{ tz = (Get-TimeZone).Id; tls = $tls }
}
$tzOk  = ($r.tz -eq "Tokyo Standard Time")
$tlsOk = ($r.tls -eq 1)

Write-Host ("  タイムゾーン    : " + $r.tz) -ForegroundColor $(if ($tzOk) { "Green" } else { "Red" })
Write-Host ("  TLS 1.2 Server  : " + $(if ($null -eq $r.tls) { "値なし" } else { $r.tls })) -ForegroundColor $(if ($tlsOk) { "Green" } else { "Red" })
Write-Host ""
if ($tzOk -and $tlsOk) {
  Write-Host "  戻りました。表示が緑になっただけでなく、OS の中の値が書き戻されています。" -ForegroundColor Green
} else {
  Write-Host "  まだです。数分おきに D8 を叩き直してください。" -ForegroundColor Yellow
  Write-Host "" 
  Write-Host "  【なぜすぐ戻らないか】" -ForegroundColor Cyan
  Write-Host "  1回目の評価は Test だけです。「値が違う」ことを確認して非準拠を報告するところまで。" -ForegroundColor Gray
  Write-Host "  実際に書き戻す Set が走るのは、次の評価です。" -ForegroundColor Gray
  Write-Host "  （実機の metaconfig.json は configurationMode=ApplyAndMonitor / 間隔15分）" -ForegroundColor DarkGray
  Write-Host ""
  Write-Host "  【待たずに次の評価を呼べます】" -ForegroundColor Cyan
  Write-Host "    C:\hccjp77\demo\restart.ps1" -ForegroundColor Yellow
  Write-Host "  エージェントを再起動すると、次のサイクルに強制的に突入します。" -ForegroundColor Gray
  Write-Host "  実測では再起動から約3分で Set まで到達しました（待つ場合は約15分）。" -ForegroundColor Gray
  Write-Host "  すでに直っていれば Set はスキップされるので、何度叩いても安全です。" -ForegroundColor DarkGray
}
Write-Next "" "スライドに戻る（時間内に戻らなくても、事前実測の数字で話は完結します）"
