#!/usr/bin/env python3
"""HCCJP 第76回の FlowAsk イベントを作成／更新する。

  作成:  python3 flowask/publish.py create
  更新:  python3 flowask/publish.py update            # slides.md と links.json を FlowAsk へ反映
  出力:  python3 flowask/publish.py render            # PDF書き出し用に slides.local.md を作る
  公開:  python3 flowask/publish.py phase live

state.json（eventId と adminToken）はこのディレクトリに置くが git には含めない。
APIキーは Obsidian の 02_Contexts/個人開発/FlowAsk/CLAUDE.md に age 暗号化で置いてある。

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

EVENT_NAME = "HCCJP 第76回 — オンプレのサーバー壊します。直すのはAIです。"
EVENT_DESC = (
    "Azure Arc × AIエージェントによる無人障害復旧のライブ実験。"
    "どの障害を起こすかは参加者の投票で決めます。"
)

# 画像の webp 変換設定。線画図なので q82 で文字まで判読できる。
WEBP_WIDTH = 1920
WEBP_QUALITY = 82

QUESTIONS = [
    {
        "key": "scenario",
        "title": "どの障害を起こしますか？",
        "description": "いちばん厄介そうなものをどうぞ。#3 と #5 は症状と原因が一致しないタイプです。",
        "type": "choice",
        "visibleIn": ["live"],
        "choices": [
            {"label": "1. Webサービスを止める"},
            {"label": "2. 設定ファイルを壊して起動不能にする"},
            {"label": "3. ファイアウォールで塞ぐ（サービスは正常なのに繋がらない）"},
            {"label": "4. ログ肥大でディスクを満杯にする"},
            {"label": "5. サービスアカウントのパスワードを変える"},
        ],
        "singleResponse": True,
    },
    {
        "key": "os",
        "title": "壊す対象はどちらにしますか？",
        "type": "choice",
        "visibleIn": ["live"],
        "choices": [
            {"label": "Windows Server 2025（arcwin01 / IIS）"},
            {"label": "Ubuntu 24.04（arclnx01 / nginx）"},
            {"label": "おまかせ"},
        ],
        "singleResponse": True,
    },
    {
        "key": "freeform",
        "title": "AIに試してほしいことを自由に書いてください",
        "description": (
            "選択肢の5つ以外でもOKです。AIへの指示そのものを書いてもらえれば、"
            "そのまま打ち込みます。時間の許すかぎり拾います。"
        ),
        "type": "text",
        "visibleIn": ["pre", "live", "post"],
    },
    {
        "key": "trust",
        "title": "今日の動きを見て、AIに運用を任せられそうだと思いましたか？",
        "type": "rating",
        "visibleIn": ["live", "post"],
        "ratingMax": 5,
        "ratingLowLabel": "まだ任せられない",
        "ratingHighLabel": "任せられる",
    },
]


# ── helpers ────────────────────────────────────────────────────────────────


def api_key() -> str:
    key = os.environ.get("FLOWASK_API_KEY")
    if key:
        return key
    md = Path.home() / "obsidian/02_Contexts/個人開発/FlowAsk/CLAUDE.md"
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


def apply_links(md: str, event_id: str) -> str:
    """slides.md のプレースホルダ URL を links.json の実値へ置き換える。"""
    links = json.loads((DECK / "links.json").read_text(encoding="utf-8"))
    md = md.replace("__EVENT_ID__", event_id)
    md = md.replace("__DEMO_WIN__", links["demo_windows"])
    md = md.replace("__DEMO_LNX__", links["demo_linux"])
    md = md.replace("__AVAILABILITY__", links["portal_availability"])
    return md


def build_markdown(event_id: str) -> str:
    """slides.md を FlowAsk に載せられる形にする（画像を data-URI へ、URLを実値へ）。"""
    md = apply_links((DECK / "slides.md").read_text(encoding="utf-8"), event_id)

    for ref in sorted(set(re.findall(r"images/([\w.-]+\.png)", md))):
        md = md.replace(f"images/{ref}", data_uri(DECK / "images" / ref))

    if len(md) > 1_000_000:
        sys.exit(f"markdown が長すぎる: {len(md)} 文字（上限 1,000,000）")
    return md


def page_index(md: str, heading_fragment: str) -> int:
    """見出しの一部から 0 始まりのページ番号を引く。"""
    pages = re.split(r"^---$", md, flags=re.M)
    # frontmatter を落とす（先頭の空要素 + frontmatter 本体）
    pages = pages[2:]
    for i, page in enumerate(pages):
        if heading_fragment in page:
            return i
    sys.exit(f"ページが見つからない: {heading_fragment}")


def build_sequence(md: str, qids: dict[str, str]) -> list[dict]:
    total = len(re.split(r"^---$", md, flags=re.M)) - 2
    after = {
        page_index(md, "# 障害シナリオ"): ["scenario", "os"],
        page_index(md, "# 壊し方以外も"): ["freeform"],
        page_index(md, "# まとめ"): ["trust"],
        page_index(md, "# Q&A"): ["__qa__"],
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


# ── commands ───────────────────────────────────────────────────────────────


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
        {"title": "HCCJP 第76回 進行スライド", "markdown": md, "theme": "default",
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


def cmd_render() -> None:
    """PDF/PPTX 書き出し用に、リンクだけ実値へ置換した markdown を吐く（画像はローカルパスのまま）。"""
    st = json.loads(STATE.read_text()) if STATE.exists() else {"eventId": "__EVENT_ID__"}
    out = DECK / "slides.local.md"   # 画像の相対パスを保つためデッキ直下に置く
    out.write_text(apply_links((DECK / "slides.md").read_text(encoding="utf-8"), st["eventId"]),
                   encoding="utf-8")
    print(out)


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
    elif cmd == "render":
        cmd_render()
    elif cmd == "phase" and len(sys.argv) > 2:
        cmd_phase(sys.argv[2])
    else:
        sys.exit(__doc__)
