. C:\hccjp77\demo\_demo.ps1
Write-Title "D0  開始前チェック（セッションが始まる前に叩く）"

Write-Host "【1】arcwin01 の状態とチェックポイント" -ForegroundColor Cyan
Get-VM arcwin01 | Format-Table Name, State, Uptime -AutoSize
Get-VMSnapshot -VMName arcwin01 | Select-Object Name, ParentSnapshotName, CreationTime | Format-Table -AutoSize

Write-Host "【2】arcwin01 の中に入れるか" -ForegroundColor Cyan
try { Invoke-OnArc { "  OK: " + $env:COMPUTERNAME } } catch { Write-Host "  NG: $_" -ForegroundColor Red }

Write-Host ""
Write-Host "【3】Arc エージェントは繋がっているか" -ForegroundColor Cyan
Invoke-OnArc {
  $a = (& "$env:ProgramFiles\AzureConnectedMachineAgent\azcmagent.exe" show -j 2>$null) -join "" | ConvertFrom-Json
  [PSCustomObject]@{ '状態' = $a.status; '最終ハートビート' = $a.lastHeartbeat }
} | Format-Table '状態','最終ハートビート' -AutoSize

Write-Host "  ブラウザで開いておくもの:" -ForegroundColor Gray
Write-Host "    Azure ポータル > arcwin01 > マシン構成" -ForegroundColor Gray
Write-Host "    Hyper-V マネージャー（この L1 上）" -ForegroundColor Gray
Write-Next "D1-before.ps1" "本番開始。まず巻き戻す前の正常な姿を見せる"
