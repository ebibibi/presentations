. C:\hccjp77\demo\_demo.ps1
$el = Get-Elapsed
if ($el) { Write-Title ("D3  巻き戻しから {0:N0} 分 {1:N0} 秒" -f $el.TotalMinutes, $el.Seconds) }
else     { Write-Title "D3  いまの OS の中身" }

Write-Host "【OS の中の実際の値】" -ForegroundColor Cyan
Show-OsTruth
Write-Host "  ポータル側は？ → arcwin01 / マシン構成 を更新してみてください" -ForegroundColor Yellow
Write-Host ""
Write-Host "  0〜8分   : ポータルは全部グリーン。でも上の値はもう壊れている" -ForegroundColor DarkGray
Write-Host "  9〜12分  : 3つが順番に赤くなる" -ForegroundColor DarkGray
Write-Host "  それ以降 : 赤いまま。なぜ直らないのかを D5 / D6 で見ます" -ForegroundColor DarkGray
Write-Next "D4-assignments.ps1" "巻き戻しで割り当て自体は変わっていないことを確認する"
