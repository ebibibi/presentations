#!/usr/bin/env python3
"""HCCJP 第78回の FlowAsk イベントを作成／更新する。

  作成:  python3 flowask/publish.py create
  更新:  python3 flowask/publish.py update            # slides.md を FlowAsk へ反映
  公開:  python3 flowask/publish.py phase live        # 当日 14:00 前に。終了後は post

state.json（eventId と adminToken）はこのディレクトリに置くが git には含めない。
APIキーは Obsidian の 02_Contexts/個人開発/FlowAsk/AGENTS.md に age 暗号化で置いてある。

FlowAsk 側の制約（reference_flowask_slide_doc_constraints）:
  - markdown は最大 1,000,000 文字
  - 画像は data-URI のみ（CSP で外部ホスト不可）
"""

from __future__ import annotations

import base64
import io
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

from PIL import Image

BASE = "https://flowask.ebisuda.net/api"
HERE = Path(__file__).resolve().parent
DECK = HERE.parent
STATE = HERE / "state.json"

EVENT_NAME = "HCCJP 第78回 — プライベートパス構成で読み解くAzure Localのネットワーク"
EVENT_DESC = (
    "2026年10月9日（金）14:00〜15:30。松本 秀太 氏（三井情報）のAzure Localネットワークの回と、"
    "高添 修 氏（日本マイクロソフト）の Adaptive Cloud 最新動向。質問はここからどうぞ。"
)

WEBP_WIDTH = 1920
WEBP_QUALITY = 82

# QUESTIONS は「デッキに出てくる順」に並べる。この順が参加者ページの並び順にもなる。
QUESTIONS = [
    {
        "key": "azlocal",
        "title": "Azure Local、どこまで触ったことがありますか？",
        "description": "開始前にどうぞ。今日の話をどの目線で聞くかの目安にします。",
        "type": "choice",
        "visibleIn": ["pre", "live"],
        "choices": [
            {"label": "本番で運用している"},
            {"label": "検証・PoCをしたことがある"},
            {"label": "導入を検討中"},
            {"label": "名前は知っている"},
            {"label": "今日はじめて知った"},
        ],
        "singleResponse": True,
    },
    {
        "key": "egress",
        "title": "オンプレ（Azure Local / Arc）からAzureへの通信、いまどう出していますか？",
        "type": "choice",
        "visibleIn": ["pre", "live"],
        "choices": [
            {"label": "インターネットへ直接"},
            {"label": "プロキシ経由"},
            {"label": "ExpressRoute / VPN（プライベート経路）"},
            {"label": "これから決める"},
            {"label": "該当する環境が無い"},
        ],
        "singleResponse": True,
    },
    {
        "key": "satisfaction",
        "title": "今日の勉強会、いかがでしたか？",
        "type": "rating",
        "visibleIn": ["live", "post"],
        "ratingMax": 5,
        "ratingLowLabel": "いまひとつ",
        "ratingHighLabel": "とても良かった",
    },
    {
        "key": "next",
        "title": "HCCJPで次に聞きたいテーマ・話してみたいことを教えてください",
        "description": "登壇のご希望や「うちの事例を話したい」も大歓迎です。",
        "type": "text",
        "visibleIn": ["pre", "live", "post"],
    },
]


def api_key() -> str:
    key = os.environ.get("FLOWASK_API_KEY")
    if key:
        return key
    md = Path.home() / "obsidian/02_Contexts/個人開発/FlowAsk/AGENTS.md"
    m = re.search(
        r"-----BEGIN AGE ENCRYPTED FILE-----.*?-----END AGE ENCRYPTED FILE-----",
        md.read_text(encoding="utf-8"),
        re.S,
    )
    if not m:
        sys.exit("APIキーの暗号文が見つからない")
    out = subprocess.run(
        ["age", "-d", "-i", str(Path.home() / ".config/sops/age/keys.txt")],
        input=m.group(0),
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        sys.exit(f"age 復号に失敗: {out.stderr.strip()}")
    return out.stdout.strip()


def call(method: str, path: str, body: dict | None = None, **headers) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{BASE}{path}", data=data, method=method)
    req.add_header("Content-Type", "application/json")
    for k, v in headers.items():
        req.add_header(k.replace("_", "-"), v)
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.loads(r.read() or "{}")
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path} → {e.code}: {e.read().decode()[:500]}")


def load_state() -> dict:
    if not STATE.exists():
        sys.exit("state.json が無い。先に `publish.py create` を実行する")
    return json.loads(STATE.read_text())


def data_uri(png: Path) -> str:
    im = Image.open(png).convert("RGB")
    if im.width > WEBP_WIDTH:
        im = im.resize((WEBP_WIDTH, round(im.height * WEBP_WIDTH / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=WEBP_QUALITY, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def build_markdown(event_id: str) -> str:
    """slides.md を FlowAsk に載せられる形にする（画像を data-URI へ、URLを実値へ）。"""
    md = (DECK / "slides.md").read_text(encoding="utf-8").replace("__EVENT_ID__", event_id)
    for ref in sorted(set(re.findall(r"\]\(([\w.-]+\.png)\)", md))):
        md = md.replace(f"]({ref})", f"]({data_uri(DECK / ref)})")
    if len(md) > 1_000_000:
        sys.exit(f"markdown が長すぎる: {len(md)} 文字（上限 1,000,000）")
    return md


def page_index(md: str, heading_fragment: str, nth: int = 0) -> int:
    """見出しの一部から 0 始まりのページ番号を引く。nth 番目の一致を返す。"""
    pages = re.split(r"^---$", md, flags=re.M)[2:]   # 先頭の空要素と frontmatter を落とす
    hits = [i for i, page in enumerate(pages) if heading_fragment in page]
    if len(hits) <= nth:
        sys.exit(f"ページが見つからない: {heading_fragment} ({nth})")
    return hits[nth]


def build_sequence(md: str, qids: dict[str, str]) -> list[dict]:
    total = len(re.split(r"^---$", md, flags=re.M)) - 2
    # 「このページを出し終わったら、このフレームを挟む」の対応表。
    after = {
        page_index(md, "# 今日のリンク"): ["azlocal", "egress"],
        page_index(md, "# Q&A", 0): ["__qa__"],
        page_index(md, "# Q&A", 1): ["__qa__"],
        page_index(md, "# ご参加ありがとうございました"): ["satisfaction", "next"],
    }
    seq: list[dict] = []
    for i in range(total):
        seq.append({"type": "page", "pageIndex": i})
        for key in after.get(i, []):
            if key == "__qa__":
                seq.append({"type": "qa"})
            else:
                seq.append({"type": "question", "questionId": qids[key]})
    return seq


def cmd_create() -> None:
    if STATE.exists():
        sys.exit(f"すでに {STATE} がある。作り直すなら手で消す")

    created = call("POST", "/events", {"name": EVENT_NAME, "description": EVENT_DESC},
                   x_api_key=api_key())
    event_id, admin = created["event"]["id"], created["adminToken"]
    if not created["event"].get("ownerId"):
        sys.exit("ownerId が空。APIキー認証に失敗している")
    print(f"event {event_id} / owner {created['event']['ownerId']}")

    qids = {}
    for order, q in enumerate(QUESTIONS):
        payload = {k: v for k, v in q.items() if k != "key"}
        payload["sortOrder"] = order
        payload.setdefault("anonymousAllowed", True)
        res = call("POST", f"/events/{event_id}/questions", payload, x_admin_token=admin)
        qids[q["key"]] = res["id"]
        print(f"  question {q['key']} → {res['id']}")

    md = build_markdown(event_id)
    slide = call(
        "POST",
        f"/events/{event_id}/slides",
        {"title": "HCCJP 第78回 進行スライド", "markdown": md, "theme": "default",
         "sequence": build_sequence(md, qids)},
        x_admin_token=admin,
    )
    STATE.write_text(json.dumps(
        {"eventId": event_id, "adminToken": admin, "slideId": slide["id"], "questionIds": qids},
        ensure_ascii=False, indent=2))
    call("PATCH", f"/events/{event_id}", {"phase": "pre"}, x_admin_token=admin)
    print(f"done: https://flowask.ebisuda.net/e/{event_id}  (markdown {len(md)} 文字)")


def cmd_update() -> None:
    st = load_state()
    md = build_markdown(st["eventId"])
    call(
        "PATCH",
        f"/events/{st['eventId']}/slides/{st['slideId']}",
        {"markdown": md, "sequence": build_sequence(md, st["questionIds"])},
        x_admin_token=st["adminToken"],
    )
    print(f"updated ({len(md)} 文字): https://flowask.ebisuda.net/e/{st['eventId']}")


def cmd_phase(phase: str) -> None:
    st = load_state()
    call("PATCH", f"/events/{st['eventId']}", {"phase": phase}, x_admin_token=st["adminToken"])
    print(f"phase → {phase}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "create":
        cmd_create()
    elif cmd == "update":
        cmd_update()
    elif cmd == "phase" and len(sys.argv) > 2:
        cmd_phase(sys.argv[2])
    else:
        sys.exit(__doc__)
