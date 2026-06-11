# -*- coding: utf-8 -*-
"""hyperv-nestlab 3層アーキテクチャ図を正確なSVGで描き、PNG化する。"""
import cairosvg

W, H = 1680, 1120
FONT = "Noto Sans CJK JP"

# ---- カラーパレット (access-guide の mermaid と整合) ----
C_HOST   = "#0a3d6b"   # L0 / L1 (Hyper-V ホスト) — 濃紺
C_HOST_F = "#eaf2fb"
C_CTRL   = "#0b5a0b"   # 制御VM — 緑
C_CTRL_F = "#e8f5e8"
C_GUEST  = "#3b1d5e"   # L2 ゲスト — 紫
C_GUEST_F= "#f1ebf8"
C_NET    = "#8a5a00"   # ネットワーク — 琥珀
C_NET_F  = "#fff6e6"
C_STORE  = "#444"
C_STORE_F= "#f3f3f3"
INK      = "#1a1a1a"
SUB      = "#555"

parts = []
def add(s): parts.append(s)

def rect(x, y, w, h, fill, stroke, rx=12, sw=2.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')

def text(x, y, s, size=22, fill=INK, weight="normal", anchor="start", family=FONT):
    add(f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')

def line(x1, y1, x2, y2, stroke, sw=2.5, dash=None, marker=True):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = ' marker-end="url(#arrow)"' if marker else ""
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
        f'stroke-width="{sw}"{d}{m}/>')

# ===== ヘッダ・defs =====
add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add('<defs>'
    '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#c0392b"/></marker>'
    '<marker id="arrowB" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
    '<path d="M0,0 L10,5 L0,10 z" fill="#1f6feb"/></marker>'
    '</defs>')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#ffffff"/>')

# ===== タイトル =====
text(40, 52, "hyperv-nestlab — Nested Hyper-V 3層アーキテクチャ", size=34, weight="bold")
text(40, 86, "既存の Hyper-V サーバー1台だけが前提。bootstrap.ps1 が制御VMを自己構築し、YAML宣言から L1 / L2 を冪等に再現する。",
     size=19, fill=SUB)

# ===== L0: 物理ホスト (最外殻) =====
L0x, L0y, L0w, L0h = 40, 110, 1600, 960
rect(L0x, L0y, L0w, L0h, "#ffffff", C_HOST, rx=16, sw=3.5)
add(f'<rect x="{L0x}" y="{L0y}" width="{L0w}" height="46" rx="16" fill="{C_HOST}"/>')
add(f'<rect x="{L0x}" y="{L0y+24}" width="{L0w}" height="22" fill="{C_HOST}"/>')
text(L0x+22, L0y+32, "L0 — 物理 Hyper-V ホスト（Windows）", size=24, fill="#fff", weight="bold")
text(L0x+L0w-22, L0y+32, "★ あなたが用意する唯一の前提", size=19, fill="#cfe3f7", anchor="end")
text(L0x+22, L0y+78, "ホスト PowerShell + PowerShell Direct（VMBus）で土台を構築 / Hyper-V マネージャーで各VMの画面へ",
     size=18, fill=SUB)

# ===== 制御VM (L0直下・左) =====
Cx, Cy, Cw, Ch = 80, 230, 360, 300
rect(Cx, Cy, Cw, Ch, C_CTRL_F, C_CTRL, sw=3)
add(f'<rect x="{Cx}" y="{Cy}" width="{Cw}" height="40" rx="12" fill="{C_CTRL}"/>')
add(f'<rect x="{Cx}" y="{Cy+20}" width="{Cw}" height="20" fill="{C_CTRL}"/>')
text(Cx+18, Cy+28, "制御 VM（Ubuntu + Ansible）", size=20, fill="#fff", weight="bold")
text(Cx+18, Cy+74,  "IP: 10.20.0.10  /  CtrlNAT", size=19, fill=INK, weight="bold")
text(Cx+18, Cy+108, "・自動化の頭脳（Ansible 内蔵）", size=17, fill=INK)
text(Cx+18, Cy+136, "・bootstrap.ps1 が自己構築", size=17, fill=INK)
text(Cx+18, Cy+164, "・ここから L1 / L2 を構成", size=17, fill=INK)
text(Cx+18, Cy+200, "踏み台:", size=17, fill=SUB, weight="bold")
text(Cx+18, Cy+226, " L2 へは制御VMからのみ", size=16, fill=SUB)
text(Cx+18, Cy+248, " IP 到達（作業PC/L0からは不可）", size=16, fill=SUB)
text(Cx+18, Cy+278, "OS: 差分ディスクで軽量", size=15, fill=SUB)

# ===== CtrlNAT バス (制御VM ⇄ L1) =====
busY = 560
add(f'<rect x="{Cx}" y="{busY-16}" width="1480" height="32" rx="16" fill="{C_NET_F}" stroke="{C_NET}" stroke-width="2"/>')
text(Cx+24, busY+7, "CtrlNAT  10.20.0.0/24   （制御VM ⇄ L1 を IP で接続）", size=18, fill=C_NET, weight="bold", anchor="start")
# 制御VM → bus
line(Cx+Cw/2, Cy+Ch, Cx+Cw/2, busY-16, C_NET, sw=2.5, marker=False)

# ===== L1: Nested ホスト VM (右・大きな入れ子) =====
L1x, L1y, L1w, L1h = 560, 200, 1050, 660
rect(L1x, L1y, L1w, L1h, C_HOST_F, C_HOST, rx=14, sw=3)
add(f'<rect x="{L1x}" y="{L1y}" width="{L1w}" height="42" rx="14" fill="{C_HOST}"/>')
add(f'<rect x="{L1x}" y="{L1y+22}" width="{L1w}" height="20" fill="{C_HOST}"/>')
text(L1x+18, L1y+30, "L1 — Nested Hyper-V ホスト VM（Windows）", size=22, fill="#fff", weight="bold")
text(L1x+L1w-18, L1y+30, "IP: 10.20.0.20", size=19, fill="#cfe3f7", anchor="end", weight="bold")
text(L1x+18, L1y+72, "ExposeVirtualizationExtensions（入れ子有効化）/ 静的メモリ / MACスプーフィング",
     size=16, fill=SUB)
text(L1x+18, L1y+96, "役割: LabNAT のルータ ＆ DHCP / L2 のホスト", size=16, fill=SUB)

# ラボストア L: (L1内・右上の帯)
Sx, Sy, Sw, Sh = L1x+660, L1y+118, 370, 96
rect(Sx, Sy, Sw, Sh, C_STORE_F, C_STORE, rx=10, sw=2)
text(Sx+14, Sy+28, "ラボストア L:（大容量・差分の置き場）", size=16, fill=INK, weight="bold")
text(Sx+14, Sy+54, "golden イメージ → L2 は差分ディスク", size=15, fill=SUB)
text(Sx+14, Sy+76, "cloud-init シードもここに集約", size=15, fill=SUB)
# bus → L1
line(L1x+200, busY-16, L1x+200, L1y+L1h+0.1, C_NET, sw=0, marker=False)  # placeholder, drawn below

# ===== LabNAT (L1の中・入れ子) =====
Nx, Ny, Nw, Nh = L1x+20, L1y+130, 620, 500
rect(Nx, Ny, Nw, Nh, C_NET_F, C_NET, rx=12, sw=2.5, dash="8 5")
text(Nx+16, Ny+30, "LabNAT  10.10.0.0/24   （GW = L1 10.10.0.1）", size=18, fill=C_NET, weight="bold")
text(Nx+16, Ny+54, "L1 の中で閉じる自己完結ネット — L2 をオフライン検証環境として隔離", size=14.5, fill=SUB)

# ===== L2 VM群 (LabNAT内・2x2) =====
def l2box(x, y, w, h, title, ip, lines):
    rect(x, y, w, h, C_GUEST_F, C_GUEST, rx=10, sw=2.5)
    add(f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="10" fill="{C_GUEST}"/>')
    add(f'<rect x="{x}" y="{y+17}" width="{w}" height="17" fill="{C_GUEST}"/>')
    text(x+12, y+24, title, size=17, fill="#fff", weight="bold")
    text(x+12, y+58, ip, size=15.5, fill=INK, weight="bold")
    yy = y+82
    for ln in lines:
        text(x+12, yy, ln, size=14, fill=SUB); yy += 21

cw2, ch2, gap = 290, 188, 20
gx, gy = Nx+16, Ny+74
l2box(gx, gy, cw2, ch2, "L2 — Windows Server 2025", "10.10.0.51 / WinRM 5985",
      ["golden の差分ディスクから", "一瞬で作成（初期 ~300MB）", "認証: Administrator / NTLM"])
l2box(gx+cw2+gap, gy, cw2, ch2, "L2 — Ubuntu 24.04", "10.10.0.50 / SSH 22",
      ["cloud image の差分 +", "cloud-init NoCloud シード", "認証: labadmin / 公開鍵"])
l2box(gx, gy+ch2+gap, cw2, ch2, "L2 — dc01（AD フォレスト）", "10.10.0.10 / AD・DC",
      ["新規フォレストに昇格", "二段 PowerShell Direct で構築", "NETBIOS\\Administrator"])
l2box(gx+cw2+gap, gy+ch2+gap, cw2, ch2, "L2 — mem01 …（メンバ）", "10.10.0.x / WinRM",
      ["ドメイン参加", "差分ディスクで台数を量産", "count / ip_from で増殖"])

# ===== 接続経路の凡例（右下） =====
Lx, Ly, Lw, Lh = L1x+660, L1y+232, 370, 398
rect(Lx, Ly, Lw, Lh, "#fafafa", "#999", rx=10, sw=1.8)
text(Lx+16, Ly+30, "接続・制御の経路", size=18, fill=INK, weight="bold")
# A 制御経路
add(f'<circle cx="{Lx+24}" cy="{Ly+60}" r="7" fill="#c0392b"/>')
text(Lx+40, Ly+66, "A. 制御（自動化）経路", size=16, fill="#c0392b", weight="bold")
text(Lx+40, Ly+90,  "制御VM → WinRM 5985 → L1", size=14.5, fill=INK)
text(Lx+40, Ly+112, "制御VM → L1ルーティング → L2 IP", size=14.5, fill=INK)
text(Lx+40, Ly+134, "Linux=SSH / Windows=WinRM", size=14.5, fill=SUB)
text(Lx+40, Ly+156, "中身を作り込むのは Ansible", size=14.5, fill=SUB)
# B コンソール経路
add(f'<circle cx="{Lx+24}" cy="{Ly+196}" r="7" fill="#1f6feb"/>')
text(Lx+40, Ly+202, "B. コンソール（画面）経路", size=16, fill="#1f6feb", weight="bold")
text(Lx+40, Ly+226, "L0 → vmconnect → L1 の画面", size=14.5, fill=INK)
text(Lx+40, Ly+248, "L1 内 Hyper-V マネージャー →", size=14.5, fill=INK)
text(Lx+40, Ly+270, "  vmconnect localhost → L2 の画面", size=14.5, fill=INK)
text(Lx+40, Ly+292, "VMBus 経由（ネットワーク非依存）", size=14.5, fill=SUB)
# 最後の砦
text(Lx+16, Ly+332, "最後の砦: PowerShell Direct", size=15.5, fill=INK, weight="bold")
text(Lx+16, Ly+356, "IPもWinRMも無いVMに VMBus で到達。", size=14, fill=SUB)
text(Lx+16, Ly+378, "L0→L1→L2 の二段で復旧できる。", size=14, fill=SUB)

# ===== 経路の矢印（A=赤, B=青） =====
# 制御VM → L1 (WinRM, A)
line(Cx+Cw, Cy+90, L1x, Cy+90, "#c0392b", sw=3)
text((Cx+Cw+L1x)/2, Cy+78, "WinRM 5985 (A)", size=15, fill="#c0392b", weight="bold", anchor="middle")
# 制御VM → L2 (制御経路A, 点線, 左マージン経由で下回り → LabNAT へ)
ay = 888
add(f'<path d="M {Cx+10} {Cy+Ch} L 62 {Cy+Ch+20} L 62 {ay} L {Nx-2} {ay} L {Nx-2} {Ny+Nh}" '
    f'fill="none" stroke="#c0392b" stroke-width="2.5" stroke-dasharray="7 5" marker-end="url(#arrow)"/>')
text(72, ay-10, "A: 制御VM →（WinRM で L1）→ L1ルーティングで L2 の IP へ到達",
     size=15, fill="#c0392b", weight="bold", anchor="start")
# L0 → L1 → L2 PowerShell Direct (B, VMBus) — L1右下から外へ
line(L1x+L1w-300, L1y+L1h+24, L1x+L1w-160, L1y+L1h-8, "#1f6feb", sw=2.5, dash="2 6", marker=False)
text(L1x+L1w-300, L1y+L1h+46, "B: L0 → L1 → L2  PowerShell Direct / コンソール（VMBus・ネットワーク非依存）",
     size=15, fill="#1f6feb", weight="bold", anchor="start")

# ===== 宣言ファイル → resolve → 確定モデル（左下のデッドスペース） =====
Dx, Dy, Dw, Dh = 80, 620, 360, 230
rect(Dx, Dy, Dw, Dh, "#fafafa", "#999", rx=10, sw=1.8)
text(Dx+16, Dy+30, "宣言（入力）→ 確定モデル", size=18, fill=INK, weight="bold")
add(f'<rect x="{Dx+20}" y="{Dy+50}" width="150" height="36" rx="6" fill="#eef4ff" stroke="#1f6feb" stroke-width="1.8"/>')
text(Dx+95, Dy+73, "l1/*.yml", size=15, fill=INK, anchor="middle")
add(f'<rect x="{Dx+20}" y="{Dy+94}" width="150" height="36" rx="6" fill="#eef4ff" stroke="#1f6feb" stroke-width="1.8"/>')
text(Dx+95, Dy+117, "l2/*.yml", size=15, fill=INK, anchor="middle")
line(Dx+175, Dy+90, Dx+205, Dy+90, "#555", sw=2)
add(f'<rect x="{Dx+205}" y="{Dy+62}" width="135" height="58" rx="6" fill="#fff6e6" stroke="{C_NET}" stroke-width="1.8"/>')
text(Dx+272, Dy+86, "tools/", size=14, fill=INK, anchor="middle")
text(Dx+272, Dy+106, "resolve.py", size=14, fill=INK, anchor="middle", weight="bold")
text(Dx+16, Dy+160, "→ build/resolved.json（名前/IP/ドメイン）", size=14.5, fill=SUB)
text(Dx+16, Dy+186, "版固定(images.yml)+SHA256 検証で", size=14, fill=SUB)
text(Dx+16, Dy+208, "どの環境でも決定論的に同じ形に収束", size=14, fill=SUB)

# ===== bootstrap.ps1 帯（下部） =====
text(40, H-22, "bootstrap.ps1 の流れ:  ①プリフライト → ②検証/解決(resolve.py) → ③イメージ整備(DISM golden / Ubuntu取得) "
     "→ ④L0→L1→制御VM→golden配送 → ⑤L1内 Hyper-V+LabNAT(Ansible)→L2作成→AD　／　再実行は冪等収束（no-change が受入条件）",
     size=14.5, fill=SUB)

add('</svg>')
svg = "\n".join(parts)
open("./images/arch.svg", "w").write(svg)
cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                 write_to="./images/arch.png",
                 output_width=W, output_height=H)
print("wrote arch.svg / arch.png", W, "x", H)
