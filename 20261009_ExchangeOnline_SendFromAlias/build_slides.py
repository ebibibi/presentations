#!/usr/bin/env python3
"""Exchange Online send-from-alias GA short explainer deck."""
from pathlib import Path

from deck_parts import (BLUE, EMU, GREEN, ORANGE, PURPLE, RED, TEAL, TEXT_MAIN,
                        TEXT_MUTED, add_slide, big_statement, card, checklist,
                        header, new_deck, text, title_slide)

OUT = Path(__file__).resolve().parent / "ExchangeOnlineエイリアスから送信GA.pptx"
SRC = "https://jpmessaging.github.io/blog/sending-from-email-aliases-general-availability/"

prs = new_deck()
title_slide(prs, title="エイリアスから送信できる",
            subtitle="Exchange Online で一般提供（GA）",
            tagline="便利。でもルールとトレースが変わる",
            source_url=SRC, footer="2026年10月9日 ｜ ebisuda.net")

s = add_slide(prs)
header(s, "01", "WHAT IS ALIAS", "エイリアス＝1つのメールボックスに付いた別のアドレス")
card(s, 0.55 * EMU, 2.0 * EMU, 5.9 * EMU, 4.2 * EMU, "機能の提供前",
     "エイリアス宛てのメールは受信できた\n\n送信は常にプライマリアドレス\n\n→ 共有メールボックスや\n配布グループなどで回避していた", TEXT_MUTED)
card(s, 6.85 * EMU, 2.0 * EMU, 5.9 * EMU, 4.2 * EMU, "GA後",
     "パブリックプレビューを経て一般提供\n\nOutlook から任意のエイリアスを\n送信元に選べる\n\nエイリアス宛てに届いたメールへの\n返信は、自動でそのエイリアスから", GREEN)

s = add_slide(prs)
header(s, "02", "HOW TO ENABLE", "有効にするのは管理者（テナント単位）")
card(s, 0.55 * EMU, 2.0 * EMU, 5.9 * EMU, 2.3 * EMU, "PowerShell",
     "Set-OrganizationConfig\n-SendFromAliasEnabled $True", BLUE)
card(s, 6.85 * EMU, 2.0 * EMU, 5.9 * EMU, 2.3 * EMU, "Exchange 管理センター",
     "Settings → Mail Flow →\nSending from Aliases をオン", BLUE)
card(s, 0.55 * EMU, 4.6 * EMU, 12.2 * EMU, 2.2 * EMU, "送信させたくないドメインがあるとき",
     "そのドメインを「受信のみ」に設定する（Set-AcceptedDomain の SendingFromDomainDisabled）\n"
     "エイリアス自体は Microsoft 365 管理センターで管理する", ORANGE)

s = add_slide(prs)
header(s, "03", "USER EXPERIENCE", "利用者はどこで選ぶ？")
card(s, 0.55 * EMU, 2.0 * EMU, 3.9 * EMU, 3.6 * EMU, "Web 版（OWA）",
     "Outlook on the web\n設定 → 作成と返信で\nエイリアスを表示して選ぶ", TEAL)
card(s, 4.72 * EMU, 2.0 * EMU, 3.9 * EMU, 3.6 * EMU, "デスクトップ版",
     "Outlook（Windows / Mac）\n差出人欄のドロップダウン\nまたは手入力", TEAL)
card(s, 8.89 * EMU, 2.0 * EMU, 3.9 * EMU, 3.6 * EMU, "モバイル版",
     "Outlook モバイル\n差出人欄をタップして\nエイリアスを選ぶ", TEAL)

big_statement(prs, "04", "KNOWN LIMITATIONS 1/2", "公式の既知の制限（私が最重要と見るもの）",
              "ルールが効かないことがある",
              "スパム対策・ジャーナリング・メールフロールールが\n"
              "エイリアス送信のメールに適用されない場合がある", color=RED, main_size=56)

s = add_slide(prs)
header(s, "05", "KNOWN LIMITATIONS 2/2", "そのほかの既知の制限と動作の変更")
card(s, 0.55 * EMU, 1.95 * EMU, 5.9 * EMU, 2.35 * EMU, "メッセージトレース",
     "プライマリで検索しても\nエイリアス送信分は出ない → エイリアスで検索", ORANGE)
card(s, 6.85 * EMU, 1.95 * EMU, 5.9 * EMU, 2.35 * EMU, "共有メールボックス",
     "エイリアスから送れるのは OWA で\n「別のメールボックスを開く」ときだけ", ORANGE)
card(s, 0.55 * EMU, 4.55 * EMU, 5.9 * EMU, 2.35 * EMU, "ハイブリッド",
     "オンプレから mail.～.onmicrosoft.com 宛てに\n届いた宛先が保持され、自動応答も\nそこから出ることがある", ORANGE)
card(s, 6.85 * EMU, 4.55 * EMU, 5.9 * EMU, 2.35 * EMU, "表示の変化",
     "差出人の表示やアドレスが\nこれまでと変わることがある", ORANGE)

s = add_slide(prs)
header(s, "06", "ROADMAP", "今後の検討項目（実装の確約ではない）")
card(s, 0.55 * EMU, 2.0 * EMU, 3.9 * EMU, 1.6 * EMU, "エイリアスごとの表示名", "", PURPLE)
card(s, 4.72 * EMU, 2.0 * EMU, 3.9 * EMU, 1.6 * EMU, "フィルター・既定値の制御", "", PURPLE)
card(s, 8.89 * EMU, 2.0 * EMU, 3.9 * EMU, 1.6 * EMU, "カレンダーのサポート", "", PURPLE)
text(s, 0.55 * EMU, 4.2 * EMU, 12.2 * EMU, 1.0 * EMU,
     [{"text": "GA は基本機能。想定外のケースがあればサポートチケットを、と案内されている",
       "size": 22, "color": TEXT_MAIN}])

checklist(prs, "07", "CHECKLIST", "有効化の前に確認したいこと（私の提案）", [
    "メールフロールール・ジャーナリングがアドレスを条件にしていないか",
    "メッセージトレースの手順に「エイリアスでも検索する」を足す",
    "送信させたくないドメインを「受信のみ」にしておく",
    "共有メールボックス・ハイブリッドの制限を利用者へ伝える",
], step=1.25, height=1.1)

prs.save(OUT)
print(OUT)
