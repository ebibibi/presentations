#!/usr/bin/env python3
"""HCCJP 第76回サムネイル合成スクリプト（再現用）

thumbnail_bg.png（GPT Image 2 生成）に、HCCJPの実ロゴと開催日を合成して
thumbnail.png を出力する。ロゴはAIに描かせず、必ず実ファイルを合成する。

背景の再生成:
    python3 ~/.claude/skills/image-gen/scripts/gpt_image.py \
        --prompt-file thumbnail_prompt.txt --size 1280x720 --quality medium \
        --output thumbnail_bg.png

使い方:
    python3 make_thumbnail.py
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BG_PATH = HERE / "thumbnail_bg.png"
LOGO_PATH = HERE.parent / "Images" / "hcc-logo02f.png"
OUT_PATH = HERE / "thumbnail.png"

LOGO_HEIGHT = 132
DATE_TEXT = "HCCJP 第76回  2026.8.14(金) 14:00〜"
DATE_FONT_SIZE = 34


def _bold_jp_font(size: int) -> ImageFont.FreeTypeFont:
    path = subprocess.run(
        ["fc-match", "-f", "%{file}", "Noto Sans CJK JP:style=Bold"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    if not path:
        raise RuntimeError("日本語太字フォントが見つかりません（Noto Sans CJK JP）")
    return ImageFont.truetype(path, size)


def build() -> Image.Image:
    base = Image.open(BG_PATH).convert("RGBA")
    width, height = base.size

    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo = logo.resize(
        (round(logo.width * LOGO_HEIGHT / logo.height), LOGO_HEIGHT), Image.LANCZOS
    )
    pos = (width - logo.width - 40, 38)

    # ロゴ下部の "hybrid cloud community" は黒文字。暗い背景では消えるため白いバッジを敷く
    badge = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw_badge = ImageDraw.Draw(badge)
    box = [pos[0] - 20, pos[1] - 16, pos[0] + logo.width + 20, pos[1] + logo.height + 14]
    draw_badge.rounded_rectangle(
        [box[0] - 3, box[1] - 3, box[2] + 3, box[3] + 3], radius=24, fill=(90, 180, 255, 90)
    )
    draw_badge.rounded_rectangle(box, radius=22, fill=(255, 255, 255, 242))

    composed = Image.alpha_composite(base, badge)
    composed.alpha_composite(logo, pos)

    # 開催日は左上へ。下辺には「オンプレミス」「AIエージェント」のラベルがあるため重ねない
    draw = ImageDraw.Draw(composed)
    font = _bold_jp_font(DATE_FONT_SIZE)
    x, y = 40, 40
    for dx in (-3, 0, 3):
        for dy in (-3, 0, 3):
            draw.text((x + dx, y + dy), DATE_TEXT, font=font, fill=(4, 10, 26, 255))
    draw.text((x, y), DATE_TEXT, font=font, fill=(255, 255, 255, 255))

    return composed


if __name__ == "__main__":
    build().convert("RGB").save(OUT_PATH)
    print(f"saved: {OUT_PATH}")
