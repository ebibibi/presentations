. C:\hccjp77\demo\_demo.ps1
Write-Title "D2  巻き戻せたか確認して、評価を再開させます"

# The two mistakes this catches: applying the checkpoint but forgetting to start
# the VM (it comes back Off), and marking T0 without having rolled back at all.
$vm = Get-VM arcwin01
Write-Host ("  VM の状態: " + $vm.State) -ForegroundColor $(if ($vm.State -eq 'Running') { 'Green' } else { 'Red' })
if ($vm.State -ne 'Running') {
  Write-Host ""
  Write-Host "  ✗ まだ起動していません。" -ForegroundColor Red
  Write-Host "    チェックポイントを［適用］すると VM は「オフ」になります。" -ForegroundColor Yellow
  Write-Host "    Hyper-V マネージャーで arcwin01 を右クリック →［起動］してから、もう一度 D2 を叩いてください。" -ForegroundColor Yellow
  Write-Host ""
  return
}

$os = Invoke-OnArc {
  $p = "HKLM:\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.2\Server"
  [PSCustomObject]@{ tz = (Get-TimeZone).Id; tls = (Get-ItemProperty $p -Name Enabled -EA SilentlyContinue).Enabled }
}
$broken = ($os.tz -ne "Tokyo Standard Time") -or ($null -eq $os.tls)
Write-Host ("  OS の値  : TimeZone=" + $os.tz + " / TLS 1.2=" + $(if ($null -eq $os.tls) { "値なし" } else { $os.tls })) -ForegroundColor Gray

if (-not $broken) {
  Write-Host ""
  Write-Host "  ✗ OS が壊れていません。巻き戻せていない可能性があります。" -ForegroundColor Red
  Write-Host "    T7-demo-start を［適用］したか、確認してください。" -ForegroundColor Yellow
  Write-Host "    （別のチェックポイントを適用した／適用せずに起動しただけ、のときにこうなります）" -ForegroundColor Yellow
  Write-Host ""
  Write-Host "  それでも進めるなら: C:\hccjp77\demo\D2-mark.ps1 -Force" -ForegroundColor DarkGray
  if (-not ($args -contains '-Force')) { return }
}

Write-Host "  ✓ 壊れた状態で起動しています。巻き戻し成功です" -ForegroundColor Green
Write-Host ""

# Rolling back also rolls back the agent's timers, so the next evaluation can be
# up to a full interval away with no way to tell how much of it already elapsed.
# Restarting resets the timers, which makes the wait predictable for a live demo.
Write-Host "【評価を再開させます】" -ForegroundColor Cyan
Write-Host "  巻き戻すと、エージェントのタイマーも巻き戻ります。次の評価がいつ来るか読めないので、" -ForegroundColor Gray
Write-Host "  サービスを再起動してタイマーをリセットします（Restart-Service gcarcservice）。" -ForegroundColor Gray
Write-Host "  ※ 実運用では不要です。待てば来ます。これは待ち時間を読めるようにするためのデモの都合です。" -ForegroundColor DarkGray
Write-Host ""
Invoke-OnArc {
  Restart-Service gcarcservice -Force
  Start-Sleep -Seconds 5
  "  gcarcservice: " + (Get-Service gcarcservice).Status
}

$now = Get-Date
$now.ToString("o") | Set-Content "C:\hccjp77\demo\T0.txt" -Encoding UTF8
Write-Host ""
Write-Host ("  T0 = " + $now.ToString("HH:mm:ss") + "  （ここから測ります）") -ForegroundColor Green
Write-Host ""
Write-Host "  見どころ: ここから数分で Azure 側が赤くなり始めます。" -ForegroundColor Gray
Write-Host "  1件あたり1分弱で順番に評価されるので、赤が階段状に増えていきます。" -ForegroundColor Gray
Write-Next "D3-status.ps1" "起動直後の状態を見る（Azure ポータルも並べて開く）"
