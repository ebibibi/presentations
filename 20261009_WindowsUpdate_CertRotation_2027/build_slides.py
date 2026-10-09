#!/usr/bin/env python3
"""Windows Update certificate rotation (2027) short explainer deck."""
from pathlib import Path

from deck_parts import (BLUE, EMU, GREEN, ORANGE, RED, TEAL, TEXT_MAIN, TEXT_MUTED,
                        add_slide, big_statement, card, checklist, header, new_deck,
                        shrink_title, text, title_slide)

OUT = Path(__file__).resolve().parent / "WindowsUpdate証明書ローテーション2027.pptx"
SRC = ("https://techcommunity.microsoft.com/t5/windows-it-pro-blog/"
       "prepare-for-windows-update-certificate-rotation-in-2027/ba-p/4562463")

prs = new_deck()
shrink_title(title_slide(prs, title="Windows Update の証明書が期限切れに",
            subtitle="2027年5月17日・6月19日",
            tagline="証明書が古い端末は更新が届かなくなる",
            source_url=SRC, footer="2026年10月9日 ｜ ebisuda.net"))

big_statement(prs, "01", "ANSWER", "何をすればいい？",
              "最新の月例更新を当てる",
              "サポート中の Windows を最新に保てば、ほとんどの端末は対応不要\n"
              "必要な更新を当てていない端末・サポート切れの端末は\nWindows Update につながらなくなる")

s = add_slide(prs)
header(s, "02", "WHY", "なぜ「証明書」で更新が止まるのか")
card(s, 0.55 * EMU, 2.0 * EMU, 3.9 * EMU, 3.9 * EMU, "① 本物か確かめる",
     "端末は証明書で\n「本物の Windows Update\nサーバーか」を確認する", BLUE)
card(s, 4.72 * EMU, 2.0 * EMU, 3.9 * EMU, 3.9 * EMU, "② 証明書には期限",
     "安全のため有効期限がある\n期限が来たら新しい証明書へ\n交換（ローテーション）", ORANGE)
card(s, 8.89 * EMU, 2.0 * EMU, 3.9 * EMU, 3.9 * EMU, "③ 月例更新で配布",
     "多くの端末には\n通常の月例更新で届く\n手動や管理ツールでも\n入れられる", GREEN)
text(s, 0.55 * EMU, 6.2 * EMU, 12.2 * EMU, 0.6 * EMU,
     [{"text": "新しい証明書が入っていない端末は、期限後に Windows Update へ接続できない",
       "size": 22, "bold": True, "color": TEXT_MAIN}])

s = add_slide(prs)
header(s, "03", "WHAT TO INSTALL", "バージョン別：いつまでに何を当てるか（期限は2027年）")
rows = [
    ("Windows 11 25H2 以降", "対応不要", "—", GREEN),
    ("Windows 11 24H2\n/ Windows Server 2025", "2025年9月以降のセキュリティ更新", "6月19日より前", BLUE),
    ("サポート中の他の Windows 11・Windows 10\n/ Windows Server 2022", "2026年7月以降のセキュリティ更新", "6月19日より前", BLUE),
    ("Windows 10 Enterprise 2019 LTSC\n/ Windows Server 2019・2016", "2026年7月以降のセキュリティ更新", "5月17日より前", ORANGE),
    ("それ以外（サポート切れ）", "サポート中の版へアップグレード", "—", RED),
]
y = 1.9
for name, action, due, color in rows:
    text(s, 0.55 * EMU, y * EMU, 5.7 * EMU, 0.9 * EMU,
         [{"text": name, "size": 18, "bold": True, "color": color}])
    text(s, 6.3 * EMU, y * EMU, 4.0 * EMU, 0.9 * EMU,
         [{"text": action, "size": 19, "color": TEXT_MAIN}])
    text(s, 10.4 * EMU, y * EMU, 2.7 * EMU, 0.9 * EMU,
         [{"text": due, "size": 20, "bold": True, "color": color}])
    y += 1.08

s = add_slide(prs)
header(s, "04", "AFTER EXPIRATION", "期限を過ぎると、端末は3通りに分かれる")
card(s, 0.55 * EMU, 2.0 * EMU, 3.9 * EMU, 4.4 * EMU, "サポート中・最新",
     "そのまま更新が届く\n\n新しい証明書は\nすでに入っている", GREEN)
card(s, 4.72 * EMU, 2.0 * EMU, 3.9 * EMU, 4.4 * EMU, "サポート中で未適用",
     "必要な更新が未適用だと\nWindows Update に\nつながらなくなる\n\n→ 公式の更新カタログ\nから手動で入れるか、\n管理ツールで配る", ORANGE)
card(s, 8.89 * EMU, 2.0 * EMU, 3.9 * EMU, 4.4 * EMU, "サポート切れ",
     "Windows Update を\n使えなくなる\n\n→ サポート中の版へ\nアップグレード", RED)

big_statement(prs, "05", "SCOPE", "例外は？",
              "WSUS 経由の端末は対象外",
              "WSUS（社内サーバーから更新を配る仕組み）経由の端末には\n適用されない、と公式に明記\n"
              "【私の提案】Windows Update に直接つなぐ端末を先に把握する",
              color=TEAL, main_size=56)

checklist(prs, "06", "CHECKLIST", "今日確認する3項目（私の提案）", [
    "古い Windows・サポート切れの Windows がどこにあるか洗い出す",
    "サポート中の端末に月例更新を当て続ける（更新を止めている端末を探す）",
    "サポート切れの端末のアップグレード計画を、2027年5月・6月の期限より前に立てる",
])

prs.save(OUT)
print(OUT)
