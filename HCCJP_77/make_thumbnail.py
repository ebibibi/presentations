#!/usr/bin/env python3
"""HCCJP 第77回サムネイル合成スクリプト（再現用）

thumbnail_bg.png（GPT Image 2 生成・文字ゼロ）の左側の余白へ、見出し・開催日・
HCCJPの実ロゴを合成して thumbnail.png を出力する。

設計:
  - 背景は「左45%を空ける」ことを条件に生成し、文字は図に一切重ねない
  - 画像生成に文字を描かせると年号やラベルが捏造されるため、日本語はすべてここで載せる
  - ロゴもAIに描かせず実ファイル（Images/hcc-logo02f.png）を合成する

背景の再生成:
    python3 ~/.claude/skills/image-gen/scripts/gpt_image.py \
        --prompt-file thumbnail_prompt.txt --size 1536x1024 --quality high \
        --output thumbnail_bg_raw.png
    python3 -c "from PIL import Image; im=Image.open('thumbnail_bg_raw.png').resize((1280,853), Image.LANCZOS); im.crop((0,66,1280,786)).save('thumbnail_bg.png')"

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

LABEL = "Azure Arc"
LINE1 = "便利なのはわかった。"
LINE2 = "で、壊れたら？"
DATE_TEXT = "HCCJP 第77回   2026.9.11(金) 14:00〜"

MARGIN_X = 52          # 左マージン
TEXT_ZONE_RIGHT = 610  # ここより右は図。文字を絶対にはみ出させない
LOGO_HEIGHT = 96

AZURE_BLUE = (0, 120, 212, 255)
CYAN = (110, 220, 255, 255)
WHITE = (255, 255, 255, 255)
DARK = (3, 8, 20, 255)


def _font(size: int) -> ImageFont.FreeTypeFont:
    path = subprocess.run(
        ["fc-match", "-f", "%{file}", "Noto Sans CJK JP:style=Bold"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    if not path:
        raise RuntimeError("日本語太字フォントが見つかりません（Noto Sans CJK JP）")
    return ImageFont.truetype(path, size)


def _fit(text: str, start: int, limit: int) -> ImageFont.FreeTypeFont:
    """テキストゾーンに収まる最大サイズのフォントを返す。"""
    probe = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    size = start
    while size > 12:
        font = _font(size)
        if probe.textbbox((0, 0), text, font=font)[2] <= limit:
            return font
        size -= 2
    return _font(12)


def _outlined(draw, xy, text, font, fill, width: int = 5) -> None:
    x, y = xy
    for dx in range(-width, width + 1, 2):
        for dy in range(-width, width + 1, 2):
            if dx or dy:
                draw.text((x + dx, y + dy), text, font=font, fill=DARK)
    draw.text((x, y), text, font=font, fill=fill)


def build() -> Image.Image:
    base = Image.open(BG_PATH).convert("RGBA")
    width, height = base.size
    zone = TEXT_ZONE_RIGHT - MARGIN_X

    # 左のテキストゾーンだけを軽く沈める（図には掛けない）
    veil = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ImageDraw.Draw(veil).rectangle([0, 0, TEXT_ZONE_RIGHT + 60, height], fill=(3, 8, 20, 96))
    composed = Image.alpha_composite(base, veil)
    draw = ImageDraw.Draw(composed)

    f_label = _fit(LABEL, 66, zone - 60)
    f1 = _fit(LINE1, 54, zone)
    f2 = _fit(LINE2, 86, zone)

    y_label = 250
    lw = draw.textbbox((0, 0), LABEL, font=f_label)[2]
    lh = draw.textbbox((0, 0), LABEL, font=f_label)[3]
    bar = Image.new("RGBA", composed.size, (0, 0, 0, 0))
    ImageDraw.Draw(bar).rounded_rectangle(
        [MARGIN_X - 22, y_label - 16, MARGIN_X + lw + 26, y_label + lh + 20],
        radius=16, fill=AZURE_BLUE,
    )
    composed = Image.alpha_composite(composed, bar)
    draw = ImageDraw.Draw(composed)
    _outlined(draw, (MARGIN_X, y_label), LABEL, f_label, WHITE, width=3)

    y1 = y_label + lh + 58
    _outlined(draw, (MARGIN_X, y1), LINE1, f1, CYAN, width=4)

    y2 = y1 + draw.textbbox((0, 0), LINE1, font=f1)[3] + 26
    _outlined(draw, (MARGIN_X, y2), LINE2, f2, WHITE, width=6)

    # 開催日は最下部。テキストゾーンの中に収める
    fd = _fit(DATE_TEXT, 30, zone)
    _outlined(draw, (MARGIN_X, height - 62), DATE_TEXT, fd, (200, 225, 250, 255), width=3)

    # ロゴは左上。下部の "hybrid cloud community" が黒文字のため白バッジを敷く
    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo = logo.resize(
        (round(logo.width * LOGO_HEIGHT / logo.height), LOGO_HEIGHT), Image.LANCZOS
    )
    pos = (MARGIN_X + 4, 62)
    badge = Image.new("RGBA", composed.size, (0, 0, 0, 0))
    bd = ImageDraw.Draw(badge)
    box = [pos[0] - 16, pos[1] - 12, pos[0] + logo.width + 16, pos[1] + logo.height + 10]
    bd.rounded_rectangle(box, radius=18, fill=(255, 255, 255, 240))
    composed = Image.alpha_composite(composed, badge)
    composed.alpha_composite(logo, pos)

    return composed


if __name__ == "__main__":
    build().convert("RGB").save(OUT_PATH)
    print(f"saved: {OUT_PATH}")
