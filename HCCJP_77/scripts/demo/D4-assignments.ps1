. C:\hccjp77\demo\_demo.ps1
Write-Title "D4  割り当ては、巻き戻しても消えていない"

Invoke-OnArc {
  Get-ChildItem "C:\ProgramData\GuestConfig\Configuration" -Directory | ForEach-Object {
    $mc = Join-Path $_.FullName ($_.Name + ".metaconfig.json")
    $j  = if (Test-Path $mc) { Get-Content $mc -Raw | ConvertFrom-Json } else { $null }
    [PSCustomObject]@{
      '割り当て' = $_.Name
      'モード'   = $j.configurationMode
      '評価間隔' = "$($j.configurationModeFrequencyMins) 分"
      '取得間隔' = "$($j.refreshFrequencyMins) 分"
    }
  }
} | Format-Table '割り当て','モード','評価間隔','取得間隔' -AutoSize

Write-Host "  巻き戻しで壊れたのは OS の設定であって、割り当てではありません。" -ForegroundColor Gray
Write-Host "  エージェントは 5 分ごとに Azure から割り当てを取り直し、" -ForegroundColor Gray
Write-Host "  適用型は 15 分ごと、監査型は 60 分ごとに評価します。" -ForegroundColor Gray
Write-Next "D5-timeline.ps1" "エージェントが実際に何をいつ評価したか、ログで見る"
