. C:\hccjp77\demo\_demo.ps1
Write-Title "P1  本番用チェックポイントを作り直す（デモ前・リハーサル前に1回）"

Write-Host "【1】いまの状態を確認します" -ForegroundColor Cyan
$ok = $true

$asg = Invoke-OnArc { (Get-ChildItem "C:\ProgramData\GuestConfig\Configuration" -Directory).Name }
Write-Host ("  割り当て: " + ($asg -join ", ")) -ForegroundColor Gray
if ($asg -contains "AzureWindowsBaseline") {
  Write-Host "  ✗ AzureWindowsBaseline がいます。これが入ったままだとデモが詰まります。" -ForegroundColor Red
  Write-Host "    イニシアチブのパラメータ設定を確認してから、もう一度実行してください。" -ForegroundColor Red
  $ok = $false
} else {
  Write-Host "  ✓ 重い監査はいません" -ForegroundColor Green
}

$os = Invoke-OnArc {
  $p = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
  [PSCustomObject]@{ tz = (Get-TimeZone).Id; tls = (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled }
}
Write-Host ("  OS: TimeZone=" + $os.tz + " / TLS 1.2=" + $(if ($null -eq $os.tls) { "値なし" } else { $os.tls })) -ForegroundColor Gray
if ($os.tz -ne "Tokyo Standard Time" -or $os.tls -ne 1) {
  Write-Host "  ✗ OS がまだ直っていません。自己修復を待ってから実行してください。" -ForegroundColor Red
  $ok = $false
} else {
  Write-Host "  ✓ OS は正常な状態です（ここから壊します）" -ForegroundColor Green
}

if (-not $ok) { Write-Host ""; Write-Host "  中止しました。" -ForegroundColor Red; return }

Write-Host ""
Write-Host "【2】OS を意図的に壊します" -ForegroundColor Cyan
Invoke-OnArc {
  $p = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
  Set-TimeZone -Id "UTC"
  Remove-ItemProperty -Path $p -Name Enabled -Force -EA SilentlyContinue
  $t = (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled
  "  → TimeZone=" + (Get-TimeZone).Id + " / TLS 1.2=" + $(if ($null -eq $t) { "削除しました" } else { $t })
}

Write-Host ""
Write-Host "【3】停止 → チェックポイント作成 → 起動" -ForegroundColor Cyan
if (Get-VMSnapshot -VMName arcwin01 -Name "T7-demo-start" -EA SilentlyContinue) {
  Remove-VMSnapshot -VMName arcwin01 -Name "T7-demo-start" -Confirm:$false
  Write-Host "  古い T7-demo-start を削除しました" -ForegroundColor Gray
  Start-Sleep -Seconds 20
}
Stop-VM -Name arcwin01 -Force
Checkpoint-VM -Name arcwin01 -SnapshotName "T7-demo-start"
Start-VM -Name arcwin01
Get-VMSnapshot -VMName arcwin01 | Select-Object Name, ParentSnapshotName, CreationTime | Format-Table -AutoSize

Write-Host "  T7-demo-start を作り直しました。中身は「OSが壊れていて、重い監査がいない」状態です。" -ForegroundColor Green
Write-Host ""
Write-Host "  ⚠️ いま arcwin01 は壊れた状態で起動しています。" -ForegroundColor Yellow
Write-Host "     このまま放っておくと自己修復して全部グリーンに戻ります（それが本番の出発点）。" -ForegroundColor Yellow
Write-Next "D0-precheck.ps1" "全部グリーンに戻ったのを確認してから、リハーサル開始"
