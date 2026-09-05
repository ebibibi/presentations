#!/usr/bin/env python3
"""HCCJP 第77回サムネイル合成スクリプト（再現用）

thumbnail_bg.png（GPT Image 2 生成・文字ゼロ）に、見出し・開催日・HCCJPの実ロゴを
合成して thumbnail.png を出力する。

背景に文字を描かせない方針:
    画像生成に文字を描かせると、指示していない年号・ラベル・数値が捏造される。
    背景は象徴図のみとし、日本語はすべてこのスクリプトで載せる。

背景の再生成:
    python3 ~/.claude/skills/image-gen/scripts/gpt_image.py \
        --prompt-file thumbnail_prompt.txt --size 1536x1024 --quality medium \
        --output thumbnail_bg_raw.png
    # 1536x1024 -> 1280x853 に縮小し、上下をセンタークロップして 1280x720 にする

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
DATE_TEXT = "HCCJP 第77回  2026.9.11(金) 14:00〜"

LOGO_HEIGHT = 118
CYAN = (94, 214, 255, 255)
WHITE = (255, 255, 255, 255)
DARK = (4, 10, 26, 255)


def _font(size: int, style: str = "Bold") -> ImageFont.FreeTypeFont:
    path = subprocess.run(
        ["fc-match", "-f", "%{file}", f"Noto Sans CJK JP:style={style}"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    if not path:
        raise RuntimeError("日本語フォントが見つかりません（Noto Sans CJK JP）")
    return ImageFont.truetype(path, size)


def _outlined(draw: ImageDraw.ImageDraw, xy, text, font, fill, width: int = 6) -> None:
    """濃い縁取りつきで描く。暗い背景でも図の上でも読めるようにする。"""
    x, y = xy
    for dx in range(-width, width + 1, 2):
        for dy in range(-width, width + 1, 2):
            if dx or dy:
                draw.text((x + dx, y + dy), text, font=font, fill=DARK)
    draw.text((x, y), text, font=font, fill=fill)


def build() -> Image.Image:
    base = Image.open(BG_PATH).convert("RGBA")
    width, height = base.size

    # 下半分を暗く落として文字を読みやすくする
    veil = Image.new("RGBA", base.size, (0, 0, 0, 0))
    vd = ImageDraw.Draw(veil)
    for i in range(300):
        y = height - 300 + i
        vd.line([(0, y), (width, y)], fill=(4, 10, 26, int(215 * (i / 300) ** 0.7)))
    composed = Image.alpha_composite(base, veil)
    draw = ImageDraw.Draw(composed)

    # 見出し（下部・左寄せ）
    f0 = _font(40)
    f1 = _font(58)
    f2 = _font(104)
    x = 56
    y1 = height - 250

    # テーマラベル。見出しの上に小さく置き、何の話かを一目で分かるようにする
    lw = draw.textbbox((0, 0), LABEL, font=f0)[2]
    bar = Image.new("RGBA", composed.size, (0, 0, 0, 0))
    ImageDraw.Draw(bar).rounded_rectangle(
        [x - 14, y1 - 66, x + lw + 16, y1 - 8], radius=12, fill=(12, 92, 150, 205)
    )
    composed = Image.alpha_composite(composed, bar)
    draw = ImageDraw.Draw(composed)
    _outlined(draw, (x, y1 - 60), LABEL, f0, (150, 225, 255, 255), width=3)

    _outlined(draw, (x, y1), LINE1, f1, CYAN, width=5)
    y2 = y1 + 74
    _outlined(draw, (x, y2), LINE2, f2, WHITE, width=7)

    # 開催日（右下）
    fd = _font(31)
    dw = draw.textbbox((0, 0), DATE_TEXT, font=fd)[2]
    _outlined(draw, (width - dw - 48, height - 56), DATE_TEXT, fd, WHITE, width=4)

    # ロゴ（左上）。ロゴ下部の "hybrid cloud community" は黒文字のため白バッジを敷く
    logo = Image.open(LOGO_PATH).convert("RGBA")
    logo = logo.resize(
        (round(logo.width * LOGO_HEIGHT / logo.height), LOGO_HEIGHT), Image.LANCZOS
    )
    pos = (46, 40)
    badge = Image.new("RGBA", composed.size, (0, 0, 0, 0))
    bd = ImageDraw.Draw(badge)
    box = [pos[0] - 18, pos[1] - 14, pos[0] + logo.width + 18, pos[1] + logo.height + 12]
    bd.rounded_rectangle(
        [box[0] - 3, box[1] - 3, box[2] + 3, box[3] + 3], radius=22, fill=(90, 180, 255, 90)
    )
    bd.rounded_rectangle(box, radius=20, fill=(255, 255, 255, 242))
    composed = Image.alpha_composite(composed, badge)
    composed.alpha_composite(logo, pos)

    return composed


if __name__ == "__main__":
    build().convert("RGB").save(OUT_PATH)
    print(f"saved: {OUT_PATH}")
