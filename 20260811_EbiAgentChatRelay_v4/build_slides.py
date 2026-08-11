#!/usr/bin/env python3
"""Generate the non-technical Ebi Agent Chat Relay v4 YouTube deck."""

import sys
from pathlib import Path

sys.path.insert(0, "/home/ebi/.claude/skills/youtube-slide/scripts")

from pptx.enum.text import MSO_ANCHOR, PP_ALIGN

from slide_helpers import (
    BG,
    BLUE,
    CARD_BORDER,
    CARD_FILL,
    EMU,
    ORANGE,
    TEXT_MAIN,
    TEXT_MUTED,
    add_slide,
    box,
    header,
    new_deck,
    text,
    title_slide,
)


OUT_DIR = Path("/home/ebi/wt-1534221229802782934-presentations-v4/20260811_EbiAgentChatRelay_v4")
OUT_FILE = OUT_DIR / "Ebi Agent Chat Relay v4 - DiscordとTeamsから複数AIを使う.pptx"

# Keep the deck visually calm: one primary blue and one occasional orange highlight.
ACCENT = BLUE
HIGHLIGHT = ORANGE


def card(slide, x, y, w, h, title, body, *, accent=ACCENT, title_size=25, body_size=20):
    box(slide, x, y, w, h, fill=CARD_FILL, border=CARD_BORDER, bw=1.1)
    box(slide, x, y, 0.07 * EMU, h, fill=accent, border=accent, radius=0.01)
    text(
        slide,
        x + 0.25 * EMU,
        y + 0.22 * EMU,
        w - 0.48 * EMU,
        0.7 * EMU,
        [{"text": title, "size": title_size, "bold": True, "color": accent}],
    )
    text(
        slide,
        x + 0.25 * EMU,
        y + 1.0 * EMU,
        w - 0.48 * EMU,
        h - 1.15 * EMU,
        [{"text": body, "size": body_size, "color": TEXT_MAIN}],
    )


def statement(prs, number, label, top, main, sub, *, color=ACCENT, main_size=60):
    slide = add_slide(prs)
    header(slide, number, label, top)
    text(
        slide,
        0.65 * EMU,
        2.0 * EMU,
        12.0 * EMU,
        1.55 * EMU,
        [{"text": main, "size": main_size, "bold": True, "color": color}],
        align=PP_ALIGN.CENTER,
        anchor=MSO_ANCHOR.MIDDLE,
    )
    text(
        slide,
        1.25 * EMU,
        4.25 * EMU,
        10.8 * EMU,
        1.25 * EMU,
        [{"text": sub, "size": 25, "color": TEXT_MAIN}],
        align=PP_ALIGN.CENTER,
    )
    return slide


def arrow(slide, x, y, symbol="→"):
    text(
        slide,
        x,
        y,
        0.7 * EMU,
        0.7 * EMU,
        [{"text": symbol, "size": 34, "bold": True, "color": TEXT_MUTED}],
        align=PP_ALIGN.CENTER,
        anchor=MSO_ANCHOR.MIDDLE,
    )


prs = new_deck()

title_slide(
    prs,
    title="AIを、いつものチャットから",
    subtitle="Ebi Agent Chat Relay v4.0.0｜DiscordとTeamsに対応",
    tagline="月額プラン × 選べるAI × Discord／Teams",
    source_url="https://github.com/ebibibi/ebi-agent-chat-relay/releases/tag/v4.0.0",
    footer="2026年8月11日 ｜ ebisuda.net",
)

statement(
    prs,
    "01",
    "WHAT WE BUILT",
    "何ができるものを作ったのか？",
    "チャットから、AIに仕事を頼む",
    "DiscordやTeamsと、別の環境で動くClaude CodeやCodexをつなぎます。依頼も結果も、いつものチャットです。",
    main_size=50,
)

s = add_slide(prs)
header(s, "02", "VALUE 1", "使った量に応じて料金が増える方式だけではない")
text(
    s,
    0.65 * EMU,
    1.55 * EMU,
    12.0 * EMU,
    0.95 * EMU,
    [{"text": "月額サブスクリプションを活かす", "size": 44, "bold": True, "color": HIGHLIGHT}],
    align=PP_ALIGN.CENTER,
)
card(s, 0.75 * EMU, 2.85 * EMU, 5.55 * EMU, 2.8 * EMU, "Claude Code", "Claude Pro／Maxの契約で利用\nPC上でAIに作業させる公式ツール", accent=ACCENT)
card(s, 7.05 * EMU, 2.85 * EMU, 5.55 * EMU, 2.8 * EMU, "OpenAI Codex", "ChatGPT Plus／Pro／Businessで利用\nPC上でAIに作業させる公式ツール", accent=ACCENT)
text(
    s,
    0.8 * EMU,
    6.15 * EMU,
    11.7 * EMU,
    0.55 * EMU,
    [{"text": "各プランの利用条件・上限の範囲で使える", "size": 24, "bold": True, "color": TEXT_MAIN}],
    align=PP_ALIGN.CENTER,
)

statement(
    prs,
    "03",
    "VALUE 2",
    "どちらか一つに決めなくていい",
    "Discordなら、会話の途中でClaude Code ⇄ Codex",
    "仕事を担当するツールを交代。会話履歴の一部をテキストで渡すので、手作業の要約やコピー＆ペーストは不要です。",
    main_size=53,
)

s = add_slide(prs)
header(s, "04", "MULTIPLE BACKENDS", "仕事を担当するAIツールを選べる")
card(s, 0.75 * EMU, 2.0 * EMU, 5.55 * EMU, 3.6 * EMU, "Claude Code", "この会話を担当\n月額プランを活用", accent=ACCENT, title_size=30, body_size=24)
card(s, 7.05 * EMU, 2.0 * EMU, 5.55 * EMU, 3.6 * EMU, "Codex", "途中から交代も可能\n月額プランを活用", accent=ACCENT, title_size=30, body_size=24)
text(
    s,
    0.8 * EMU,
    6.15 * EMU,
    11.7 * EMU,
    0.55 * EMU,
    [{"text": "Discordでは会話ごとに切替可能。ほかのAIへつなぐ拡張性もあります", "size": 23, "bold": True, "color": TEXT_MAIN}],
    align=PP_ALIGN.CENTER,
)

s = add_slide(prs)
header(s, "05", "VALUE 3", "話しかける場所も選べる")
card(s, 0.75 * EMU, 2.0 * EMU, 5.55 * EMU, 3.75 * EMU, "Discord", "個人開発・コミュニティ\nスマホから気軽に依頼\n会話ごとにスレッドを分ける", accent=ACCENT, title_size=32, body_size=22)
card(s, 7.05 * EMU, 2.0 * EMU, 5.55 * EMU, 3.75 * EMU, "Microsoft Teams", "組織で普段使うチャット\n仕事の会話からそのまま依頼\n普段のチャットから文字で頼める", accent=ACCENT, title_size=32, body_size=22)
text(
    s,
    0.8 * EMU,
    6.15 * EMU,
    11.7 * EMU,
    0.55 * EMU,
    [{"text": "自分や組織が、普段いる場所から使える", "size": 27, "bold": True, "color": TEXT_MAIN}],
    align=PP_ALIGN.CENTER,
)

s = add_slide(prs)
header(s, "06", "FROM CHAT TO RESULT", "チャットで頼めること")
steps = [
    ("1", "依頼する", "スマホやPCから\nやってほしいことを書く"),
    ("2", "AIが作業", "ファイルを調べる\n実装・調査・レビュー"),
    ("3", "途中で確認", "必要に応じて\n追加の指示を送る"),
    ("4", "結果を受け取る", "完了報告と結果が\n同じ会話へ戻る"),
]
for i, (number, title_, body) in enumerate(steps):
    x = (0.45 + i * 3.2) * EMU
    card(s, x, 2.15 * EMU, 2.75 * EMU, 3.65 * EMU, f"{number}  {title_}", body, accent=ACCENT, title_size=21, body_size=19)
    if i < 3:
        arrow(s, (3.12 + i * 3.2) * EMU, 3.55 * EMU)
text(
    s,
    0.8 * EMU,
    6.25 * EMU,
    11.7 * EMU,
    0.45 * EMU,
    [{"text": "Discordでは、複数のスレッドで複数の仕事を同時に進められます", "size": 23, "bold": True, "color": TEXT_MAIN}],
    align=PP_ALIGN.CENTER,
)

s = add_slide(prs)
header(s, "07", "PROVEN ON REAL TEAMS", "実際のTeamsとCodexをつないで検証")
card(s, 0.8 * EMU, 2.35 * EMU, 3.0 * EMU, 2.7 * EMU, "Microsoft Teams", "実際のチャットから依頼", accent=ACCENT, title_size=25, body_size=20)
arrow(s, 3.95 * EMU, 3.25 * EMU)
card(s, 4.75 * EMU, 2.35 * EMU, 3.8 * EMU, 2.7 * EMU, "Ebi Agent Chat Relay", "依頼を選んだAIへ届ける", accent=ACCENT, title_size=23, body_size=20)
arrow(s, 8.7 * EMU, 3.25 * EMU)
card(s, 9.5 * EMU, 2.35 * EMU, 3.0 * EMU, 2.7 * EMU, "Codex", "実際のCodexが依頼を処理しTeamsへ返信", accent=ACCENT, title_size=25, body_size=19)
text(
    s,
    0.8 * EMU,
    5.8 * EMU,
    11.7 * EMU,
    0.75 * EMU,
    [{"text": "Discordを動かしたまま、Teams → Codex → Teamsの往復を確認", "size": 24, "bold": True, "color": TEXT_MAIN}],
    align=PP_ALIGN.CENTER,
)

s = add_slide(prs)
header(s, "08", "TEAMS SETUP", "Teams版は、組織側で導入設定が必要")
card(s, 0.75 * EMU, 2.05 * EMU, 3.7 * EMU, 3.65 * EMU, "Teams管理者", "組織のアプリとして登録\n利用者へ配布できる状態にする", accent=ACCENT, title_size=23, body_size=20)
card(s, 4.8 * EMU, 2.05 * EMU, 3.7 * EMU, 3.65 * EMU, "中継環境", "TeamsとAIを安全につなぐ\nAIを動かす環境とは分けて置く", accent=ACCENT, title_size=23, body_size=20)
card(s, 8.85 * EMU, 2.05 * EMU, 3.7 * EMU, 3.65 * EMU, "利用者", "セットアップ後は\nいつものTeamsから話すだけ", accent=ACCENT, title_size=23, body_size=20)
text(
    s,
    0.8 * EMU,
    6.18 * EMU,
    11.7 * EMU,
    0.55 * EMU,
    [{"text": "詳しい導入手順はnote記事と公式Teams Setup Guideで解説", "size": 24, "bold": True, "color": HIGHLIGHT}],
    align=PP_ALIGN.CENTER,
)

statement(
    prs,
    "09",
    "V4.0.0",
    "Ebi Agent Chat Relay v4で実現したこと",
    "選べるAIツール。選べるチャット。",
    "月額プランを活用。Discordは会話ごとに担当ツールを切替。Teamsは組織設定のツールを、普段のチャットから使う。",
    color=HIGHLIGHT,
    main_size=47,
)

OUT_DIR.mkdir(parents=True, exist_ok=True)
prs.save(OUT_FILE)
print(OUT_FILE)
