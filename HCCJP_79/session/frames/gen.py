#!/usr/bin/env python3
"""Generate step-by-step Hybrid Join diagrams (one PNG per step) for the HCCJP 79 deck."""
import html, subprocess, sys
from pathlib import Path

OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
CHROME = "/home/ebi/chrome-for-testing/chrome-linux64/chrome"
W, H = 1600, 900

# zones: (x, y, w, h, label, kind)
ZONES_OLD = [
    (20, 20, 470, 640, "Windows クライアント（pc01）", "pc"),
    (520, 20, 1060, 300, "Microsoft Entra（クラウド）", "cloud"),
    (520, 360, 1060, 300, "オンプレミス", "onp"),
]
M = '<span class="mono">'
# boxes: id -> (x, y, w, h, title, sub)
BOX_CLIENT = {
    "task": (45, 60, 420, 120, "タスク スケジューラ", M + "\\Microsoft\\Windows\\Workplace Join\\</span><br>Automatic-Device-Join（SYSTEM）"),
    "dsreg": (45, 205, 420, 90, "dsregcmd.exe", "登録処理の本体"),
    "tpm": (45, 325, 200, 100, "TPM", "鍵を守る"),
    "store": (265, 325, 200, 100, "証明書ストア", M + "LocalMachine\\My</span>"),
}
BOX_OLD = dict(BOX_CLIENT,
    login=(545, 70, 320, 120, "Entra の認証", "login.microsoftonline.com<br>トークンを出す"),
    drs=(895, 70, 320, 120, "DRS", "enterpriseregistration<br>.windows.net"),
    entra=(1245, 70, 310, 120, "Entra ID", "デバイスオブジェクト"),
    scp=(545, 410, 320, 120, "AD: SCP", "構成パーティションの案内板"),
    comp=(895, 410, 320, 120, "AD: コンピューター pc01", M + "userCertificate</span> 属性"),
    sync=(1245, 410, 310, 120, "Entra Connect Sync", "ADSync（既定 30 分周期）"))
BOX_NEW = dict(BOX_CLIENT,
    lsa=(45, 455, 420, 90, "LSA（Kerberos）", "チケットを取る"),
    ekdc=(545, 70, 320, 120, "Entra Kerberos（KDC）", "login.microsoftonline.com<br>/&lt;テナント&gt;/kerberos"),
    drs=(895, 70, 320, 120, "DRS", "enterpriseregistration<br>.windows.net"),
    entra=(1245, 70, 310, 120, "Entra ID", "デバイスオブジェクト"),
    kdc=(545, 410, 320, 120, "DC（WS2025）の KDC", "TDO: KERBEROS.<br>MICROSOFTONLINE.COM"),
    scp=(895, 410, 320, 120, "AD: SCP", "構成パーティションの案内板"),
    comp=(1245, 410, 310, 120, "AD: コンピューター pc01", M + "userCertificate</span> 属性"))

def anchor(box, side):
    x, y, w, h = box[:4]
    return {"l": (x, y + h / 2), "r": (x + w, y + h / 2), "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[side]

def render(name, zones, boxes, steps, upto, title):
    active = steps[upto]
    lit = set()
    for s in steps[: upto + 1]:
        lit |= set(s.get("lit", []))
    parts = [f'<div class="zone {k}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><span>{l}</span></div>' for x, y, w, h, l, k in zones]
    for bid, (x, y, w, h, t, sub) in boxes.items():
        cls = "box"
        if bid in active.get("lit", []): cls += " now"
        elif bid in lit: cls += " done"
        if bid in active.get("bad", []): cls += " bad"
        if bid in active.get("good", []): cls += " good"
        badge = active.get("badge", {}).get(bid, "")
        badge_html = f'<em>{badge}</em>' if badge else ""
        parts.append(f'<div class="{cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><b>{t}</b><small>{sub}</small>{badge_html}</div>')
    svg = [f'<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0">',
           '<defs>' + "".join(f'<marker id="m{c}" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="{col}"/></marker>' for c, col in (("a", "#0b6bcb"), ("d", "#b8c2d0"), ("r", "#c62828"))) + '</defs>']
    for i, s in enumerate(steps[: upto + 1]):
        for a in s.get("arrows", []):
            src, ss, dst, ds = a[:4]
            label = a[4] if len(a) > 4 else ""
            bad = len(a) > 5 and a[5] == "bad"
            (x1, y1), (x2, y2) = anchor(boxes[src], ss), anchor(boxes[dst], ds)
            now = i == upto
            col = "#c62828" if (now and bad) else ("#0b6bcb" if now else "#b8c2d0")
            mk = "r" if (now and bad) else ("a" if now else "d")
            wdt = 6 if now else 3
            dash = ' stroke-dasharray="12,8"' if bad else ""
            svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{wdt}"{dash} marker-end="url(#m{mk})"/>')
            if now and label:
                mx, my = (x1 + x2) / 2, (y1 + y2) / 2
                svg.append(f'<foreignObject x="{mx - 170}" y="{my - 24}" width="340" height="60"><div class="lbl{" badl" if bad else ""}">{label}</div></foreignObject>')
    svg.append("</svg>")
    n = active["n"]
    cap = f'<div class="cap"><div class="num">{n}</div><div><div class="ct">{active["title"]}</div><div class="cd">{active["desc"]}</div></div></div>'
    head = f'<div class="head">{title}<span>{upto + 1} / {len(steps)}</span></div>'
    doc = f"""<html><head><meta charset="utf-8"><style>
    *{{box-sizing:border-box}} body{{margin:0;width:{W}px;height:{H}px;background:#fff;position:relative;font-family:"Meiryo UI","Meiryo",sans-serif;color:#17233a;overflow:hidden}}
    .zone{{position:absolute;border:3px dashed #a9b6c8;border-radius:16px}} .zone span{{position:absolute;left:14px;top:-17px;background:#fff;padding:0 8px;font-size:22px;font-weight:700;color:#50627c}}
    .zone.pc{{background:#fafbfd}} .zone.cloud{{background:#f5f9ff}} .zone.onp{{background:#fffaf2}}
    .box{{position:absolute;border:3px solid #c9d2de;border-radius:12px;background:#fff;padding:8px 12px;color:#9aa6b6;text-align:center}}
    .mono{{font-family:"DejaVu Sans Mono",Consolas,monospace;font-size:15px}} .box b{{display:block;font-size:24px}} .box small{{display:block;font-size:17px;margin-top:3px;line-height:1.25}}
    .box.done{{border-color:#8fa3bd;color:#4a5b73}} .box.now{{border-color:#0b6bcb;background:#e8f2ff;color:#0b2a4a;box-shadow:0 0 0 5px rgba(11,107,203,.18)}}
    .box.bad{{border-color:#c62828;background:#ffecec;color:#7a1010;box-shadow:0 0 0 5px rgba(198,40,40,.15)}} .box.good{{border-color:#1b8a3a;background:#e9f8ee;color:#0d4a20;box-shadow:0 0 0 5px rgba(27,138,58,.15)}}
    .box em{{position:absolute;right:-12px;top:-16px;background:#17233a;color:#fff;font-style:normal;font-size:16px;border-radius:10px;padding:3px 9px;white-space:nowrap}}
    .box.bad em{{background:#c62828}} .box.good em{{background:#1b8a3a}}
    .lbl{{background:#0b6bcb;color:#fff;font-size:19px;border-radius:10px;padding:5px 10px;text-align:center;line-height:1.25;display:inline-block}} .lbl.badl{{background:#c62828}}
    foreignObject div{{margin:0 auto}} foreignObject{{text-align:center}}
    .head{{position:absolute;left:0;right:0;top:-100px}}
    .cap{{position:absolute;left:20px;right:20px;top:690px;height:190px;border-radius:16px;background:#17233a;color:#fff;display:flex;gap:22px;padding:22px 28px;align-items:flex-start}}
    .num{{min-width:64px;height:64px;border-radius:50%;background:#ffcc00;color:#17233a;font-size:34px;font-weight:800;display:flex;align-items:center;justify-content:center}}
    .ct{{font-size:32px;font-weight:700;margin-bottom:8px}} .cd{{font-size:23px;line-height:1.45;color:#dfe7f2}}
    .cd code{{background:#2d3d57;border-radius:6px;padding:1px 7px;font-family:Consolas,monospace;font-size:21px}}
    </style></head><body>{"".join(parts)}{"".join(svg)}{cap}</body></html>"""
    p = OUT / f"{name}.html"; p.write_text(doc, encoding="utf-8")

OLD = [
    {"n": "0", "title": "登場人物と、どこで動くか", "desc": "クライアントでは<b>タスク スケジューラ</b>が <code>dsregcmd.exe</code> を動かす。オンプレには AD と同期サーバー、クラウドには認証・登録の窓口がある", "lit": []},
    {"n": "1", "title": "タスクが起動する", "desc": "<code>Automatic-Device-Join</code> は SYSTEM で動く。きっかけは<b>サインインの1分後</b>、<b>登録イベント 4096</b>、以後<b>1時間ごと</b>。中身は <code>dsregcmd.exe</code>",
     "lit": ["task", "dsreg"], "arrows": [("task", "b", "dsreg", "t", "起動")]},
    {"n": "2", "title": "SCP を読んで、登録先を知る", "desc": "LDAP で AD の構成パーティションにある SCP を読む。<code>azureADName</code> / <code>azureADId</code> から、どのテナントに登録するかが分かる",
     "lit": ["dsreg", "scp"], "arrows": [("dsreg", "r", "scp", "t", "LDAP で読む")]},
    {"n": "3", "title": "仮の身分証（自己署名証明書）を作って AD に置く", "desc": "<b>鍵は TPM で作る</b>。その鍵で自己署名証明書を作り、<b>証明書ストアには入れず</b> AD の <code>userCertificate</code> にだけ書く。証明書の名前がそのままデバイス ID になる（実機で確認）",
     "lit": ["dsreg", "tpm", "comp"], "badge": {"comp": "仮の身分証"}, "arrows": [("dsreg", "b", "tpm", "r"), ("dsreg", "r", "comp", "t", "LDAP で書く")]},
    {"n": "4", "title": "まだ認証できない", "desc": "証明書で Entra に認証しようとしても、Entra にはまだこの PC がいない。<b>「デバイスが見つからない」で失敗</b>し、次のきっかけ（最長1時間後）を待つ",
     "lit": ["dsreg", "login"], "bad": ["login"], "badge": {"login": "見つからない"}, "arrows": [("dsreg", "r", "login", "b", "証明書で認証", "bad")]},
    {"n": "5", "title": "同期サーバーが変更を拾う", "desc": "Entra Connect Sync が、次の同期サイクル（<b>既定 30 分周期</b>）で <code>userCertificate</code> の付いたコンピューターを読み取る",
     "lit": ["comp", "sync"], "arrows": [("comp", "r", "sync", "l", "差分を読む")]},
    {"n": "6", "title": "Entra にデバイスができる", "desc": "同期サーバーが証明書・objectGUID・SID を送り、Entra に<b>デバイス オブジェクト</b>ができる。ここまでが「同期待ち」",
     "lit": ["sync", "entra"], "badge": {"entra": "pc01（保留）"}, "arrows": [("sync", "t", "entra", "b", "デバイスを同期")]},
    {"n": "7", "title": "次のタスク実行で、やっと認証できる", "desc": "サインインか1時間ごとの実行で、タスクがもう一度動く。今度は Entra に自分がいるので、証明書の秘密鍵で認証して <b>ID トークン</b>をもらえる",
     "lit": ["task", "dsreg", "login"], "good": ["login"], "badge": {"login": "ID トークン"}, "arrows": [("task", "b", "dsreg", "t"), ("dsreg", "r", "login", "b", "証明書で認証")]},
    {"n": "8", "title": "TPM で鍵を作り、DRS に登録する", "desc": "TPM で<b>新しい鍵（デバイス鍵）</b>と転送鍵を作り、証明書の要求と ID トークンを DRS に送る。正式な身分証をもらう手続き",
     "lit": ["tpm", "dsreg", "drs"], "arrows": [("dsreg", "b", "tpm", "r", "鍵"), ("dsreg", "r", "drs", "b", "登録の要求")]},
    {"n": "9", "title": "正式な身分証（デバイス証明書）を受け取って完了", "desc": "DRS がデバイス証明書（発行者 <code>MS-Organization-Access</code>）を返し、<b>こちらは証明書ストアに入る</b>。<code>dsregcmd /status</code> が <b>AzureAdJoined : YES</b> になる",
     "lit": ["drs", "store", "entra"], "good": ["store", "entra"], "badge": {"store": "デバイス証明書", "entra": "pc01（登録済み）"}, "arrows": [("drs", "b", "store", "r", "証明書を返す")]},
]
NEW = [
    {"n": "0", "title": "新しい方式の登場人物", "desc": "同期サーバーの代わりに、<b>WS2025 の DC の KDC</b> と <b>Entra の Kerberos</b> が登場する。PC 側の入口は同じタスク スケジューラ", "lit": []},
    {"n": "1", "title": "タスクが起動し、SCP を読む", "desc": "ここまでは従来と同じ。<code>Automatic-Device-Join</code> が <code>dsregcmd.exe</code> を動かし、SCP から登録先のテナントを知る",
     "lit": ["task", "dsreg", "scp"], "arrows": [("task", "b", "dsreg", "t"), ("dsreg", "r", "scp", "t", "LDAP で読む")]},
    {"n": "2", "title": "新方式を試す: DEVICE_AUTO_KERB", "desc": "ビルドが新しい Windows 11 は、まず Kerberos での参加を試す。<b>本人確認を Kerberos チケットで行う</b>。クライアントに追加の設定は要らない。仮の身分証も従来どおり AD に書かれる（実機で確認）",
     "lit": ["dsreg", "lsa", "comp"], "badge": {"comp": "証明書あり"}, "arrows": [("dsreg", "b", "lsa", "t", "チケットを要求"), ("dsreg", "r", "comp", "t")]},
    {"n": "3", "title": "DC から TGT と「紹介状」をもらう", "desc": "PC のコンピューター アカウントで DC から TGT を取り、<b>TDO があるので</b> Entra 宛ての紹介チケット <code>krbtgt/KERBEROS.MICROSOFTONLINE.COM</code> ももらう",
     "lit": ["lsa", "kdc"], "badge": {"kdc": "紹介状を発行"}, "arrows": [("lsa", "r", "kdc", "l", "Kerberos")]},
    {"n": "4", "title": "Entra の KDC からチケットをもらう", "desc": "紹介状を HTTPS で Entra の Kerberos に出し、<b>DRS 宛てのサービス チケット</b> <code>adrs/enterpriseregistration.windows.net</code> をもらう",
     "lit": ["lsa", "ekdc"], "good": ["ekdc"], "arrows": [("lsa", "r", "ekdc", "b", "KDC プロキシ（HTTPS）")]},
    {"n": "5", "title": "チケットを身分証にして DRS に登録", "desc": "チケットを DRS に出す。DRS はタグ <code>KerberosPolicy:ExchangeForJwt</code> によってチケットを受け付け、Entra にデバイスがいなくても PC を確認できる",
     "lit": ["dsreg", "drs", "tpm"], "arrows": [("dsreg", "b", "tpm", "r", "鍵"), ("dsreg", "r", "drs", "b", "チケット＋登録の要求")]},
    {"n": "6", "title": "その場で完了", "desc": "DRS がデバイスを作ってデバイス証明書を返す。<b>同期を待つ工程が無い</b>。デモ環境では 16〜18 秒で終わった",
     "lit": ["drs", "store", "entra"], "good": ["store", "entra"], "badge": {"store": "デバイス証明書", "entra": "pc01（登録済み）"}, "arrows": [("drs", "r", "entra", "l", "作成"), ("drs", "b", "store", "r", "証明書を返す")]},
]
for i in range(len(OLD)): render(f"hj_old_{i:02d}", ZONES_OLD, BOX_OLD, OLD, i, "従来")
for i in range(len(NEW)): render(f"hj_new_{i:02d}", ZONES_OLD, BOX_NEW, NEW, i, "新方式")
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path=CHROME, args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": W, "height": H})
    for f in sorted(OUT.glob("hj_*.html")):
        pg.goto(f.as_uri()); pg.wait_for_timeout(150); pg.screenshot(path=str(f.with_suffix(".png")))
    b.close()
print("ok", len(OLD), len(NEW))
