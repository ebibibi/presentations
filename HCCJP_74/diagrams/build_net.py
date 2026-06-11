# -*- coding: utf-8 -*-
"""hyperv-nestlab ネットワーク構成図（バス型）。
横線=ネットワーク(サブネット)、各ホストが足を出して接続。
L1 は CtrlNAT と LabNAT の両方に足を出すルータ(デュアルホーム)。"""
import cairosvg

W, H = 1680, 1020
FONT = "Noto Sans CJK JP"

C_HOST   = "#0a3d6b"; C_HOST_F = "#eaf2fb"   # Hyper-V ホスト(青)
C_CTRL   = "#0b5a0b"; C_CTRL_F = "#e8f5e8"   # 制御VM(緑)
C_GUEST  = "#3b1d5e"; C_GUEST_F= "#f1ebf8"   # L2 ゲスト(紫)
C_NET    = "#8a5a00"                          # ネットワーク(琥珀)
C_LAB    = "#7a4a00"
INK = "#1a1a1a"; SUB = "#555"

P = []
def add(s): P.append(s)
def rect(x,y,w,h,fill,stroke,rx=12,sw=2.5,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def text(x,y,s,size=22,fill=INK,weight="normal",anchor="start"):
    add(f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{s}</text>')
def line(x1,y1,x2,y2,stroke,sw=2.5,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
def dot(x,y,fill,r=7):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
add(f'<rect x="0" y="0" width="{W}" height="{H}" fill="#fff"/>')

# ---- タイトル ----
text(40,52,"hyperv-nestlab — ネットワーク構成（2つの NAT を L1 がルーティング）",size=33,weight="bold")
text(40,84,"横線 = ネットワーク（サブネット）。各ホストは足を出して接続。L1 は両ネットに足を出すルータ（デュアルホーム）。",size=18,fill=SUB)

# ---- L0 外殻（物理ホスト = NAT を持つ親）----
rect(30,104,1620,850,"#ffffff",C_HOST,rx=16,sw=3)
add(f'<rect x="30" y="104" width="1620" height="40" rx="16" fill="{C_HOST}"/>')
add(f'<rect x="30" y="124" width="1620" height="20" fill="{C_HOST}"/>')
text(52,132,"L0 — 物理 Hyper-V ホスト（Windows）：仮想スイッチ＋NAT を提供する親",size=21,fill="#fff",weight="bold")

# ============ CtrlNAT バス ============
busC_y = 320
busC_x1, busC_x2 = 210, 1460
def host_box(cx, top, w, h, title, sub_ip, fill, stroke, ipnet, leg_to, leg_dir, dotcol):
    """ホスト箱を描き、バスへ足を出す。leg_dir: 'down' or 'up'。"""
    x = cx - w/2
    rect(x, top, w, h, fill, stroke, rx=10, sw=2.5)
    add(f'<rect x="{x}" y="{top}" width="{w}" height="30" rx="10" fill="{stroke}"/>')
    add(f'<rect x="{x}" y="{top+15}" width="{w}" height="15" fill="{stroke}"/>')
    text(cx, top+22, title, size=16.5, fill="#fff", weight="bold", anchor="middle")
    text(cx, top+56, sub_ip, size=15, fill=SUB, anchor="middle")
    # 足
    if leg_dir=='down':
        ly0 = top+h
    else:
        ly0 = top
    line(cx, ly0, cx, leg_to, stroke, sw=3)
    dot(cx, leg_to, dotcol)
    # IP ラベル（足の脇）
    return cx

# CtrlNAT 上側ホスト（足は下へ）
host_box(360,150,300,110,"L0 物理ホスト（NAT/GW）","Hyper-V 仮想スイッチ", C_HOST_F,C_HOST,"ctrl",busC_y,'down',C_NET)
text(372,busC_y-12,"10.20.0.1",size=15,fill=C_NET,weight="bold")
host_box(760,150,300,110,"制御 VM（Ubuntu+Ansible）","自動化の頭脳・踏み台", C_CTRL_F,C_CTRL,"ctrl",busC_y,'down',C_NET)
text(772,busC_y-12,"10.20.0.10",size=15,fill=C_NET,weight="bold")

# バス線 CtrlNAT
add(f'<rect x="{busC_x1}" y="{busC_y-5}" width="{busC_x2-busC_x1}" height="10" rx="5" fill="{C_NET}"/>')
text(busC_x1, busC_y+32, "CtrlNAT  10.20.0.0/24", size=20, fill=C_NET, weight="bold")
text(busC_x2, busC_y+32, "制御プレーン（L0・制御VM・L1 が同一セグメント）", size=15, fill=SUB, anchor="end")

# ---- L1 ルータ箱（CtrlNAT と LabNAT の両方に足）----
L1cx = 1300
L1x, L1y, L1w, L1h = L1cx-170, 380, 340, 150
rect(L1x,L1y,L1w,L1h,C_HOST_F,C_HOST,rx=10,sw=3)
add(f'<rect x="{L1x}" y="{L1y}" width="{L1w}" height="32" rx="10" fill="{C_HOST}"/>')
add(f'<rect x="{L1x}" y="{L1y+16}" width="{L1w}" height="16" fill="{C_HOST}"/>')
text(L1cx,L1y+23,"L1 — Nested ホスト VM ＝ ルータ",size=17,fill="#fff",weight="bold",anchor="middle")
text(L1cx,L1y+60,"Windows / Hyper-V / NAT 中継",size=15,fill=SUB,anchor="middle")
text(L1cx,L1y+88,"2 つの NIC を持ち両ネットを橋渡し",size=14.5,fill=SUB,anchor="middle")
text(L1cx,L1y+114,"ExposeVirtualizationExt / 静的メモリ",size=13.5,fill="#888",anchor="middle")
# L1 上の足 → CtrlNAT
line(L1cx, L1y, L1cx, busC_y, C_HOST, sw=3)
dot(L1cx, busC_y, C_NET)
text(L1cx+14, busC_y-12, "10.20.0.20", size=15, fill=C_NET, weight="bold")
# L1 下の足 → LabNAT (GW)。足とラベルは入れ子ボックス/バスの後に重ねる(後勝ち回避)
busL_y = 620

# ---- 入れ子境界（L1 の内側＝LabNAT 自己完結）----
rect(120, 560, 1200, 380, "#fffaf0", C_LAB, rx=14, sw=2, dash="9 6")
text(140, 590, "L1 Nested ホスト VM の内側 — LabNAT は L1 の中で閉じる（L2 を隔離）", size=17, fill=C_LAB, weight="bold")

# ============ LabNAT バス ============
busL_x1, busL_x2 = 200, 1340
add(f'<rect x="{busL_x1}" y="{busL_y-5}" width="{busL_x2-busL_x1}" height="10" rx="5" fill="{C_LAB}"/>')
text(busL_x1, busL_y-12, "LabNAT  10.10.0.0/24　（GW = L1 10.10.0.1）", size=20, fill=C_LAB, weight="bold")

# L1 GW 足（最前面）
line(L1cx, L1y+L1h, L1cx, busL_y, C_HOST, sw=3)
dot(L1cx, busL_y, C_LAB)
text(L1cx-22, busL_y+30, "10.10.0.1 (GW)", size=15, fill=C_LAB, weight="bold", anchor="end")

# LabNAT 下側ホスト（足は上へ）
def l2(cx, title, ip, lines):
    top=680; w=250; h=210
    x=cx-w/2
    rect(x,top,w,h,C_GUEST_F,C_GUEST,rx=10,sw=2.5)
    add(f'<rect x="{x}" y="{top}" width="{w}" height="30" rx="10" fill="{C_GUEST}"/>')
    add(f'<rect x="{x}" y="{top+15}" width="{w}" height="15" fill="{C_GUEST}"/>')
    text(cx,top+22,title,size=15.5,fill="#fff",weight="bold",anchor="middle")
    yy=top+54
    text(cx,yy,ip,size=15,fill=INK,weight="bold",anchor="middle"); yy+=28
    for ln in lines:
        text(cx,yy,ln,size=13.5,fill=SUB,anchor="middle"); yy+=23
    # 足 → LabNAT
    line(cx, top, cx, busL_y, C_GUEST, sw=3)
    dot(cx, busL_y, C_LAB)

l2(330,"L2 — Windows Server 2025","10.10.0.51 / WinRM",["golden の差分ディスク","認証: Administrator","NTLM"])
l2(620,"L2 — Ubuntu 24.04","10.10.0.50 / SSH",["cloud-init NoCloud","認証: labadmin","公開鍵"])
l2(880,"L2 — dc01（AD/DC）","10.10.0.10",["新規フォレスト昇格","二段 PS Direct で構築","NETBIOS\\Administrator"])
l2(1140,"L2 — mem01 …（メンバ）","10.10.0.x / WinRM",["ドメイン参加","count / ip_from で","台数を量産"])

# ---- 経路・到達性の注記（右下）----
nx,ny,nw,nh = 1350,640,290,290
rect(nx,ny,nw,nh,"#fafafa","#999",rx=10,sw=1.8)
text(nx+16,ny+30,"到達性のルール",size=17,fill=INK,weight="bold")
add(f'<circle cx="{nx+24}" cy="{ny+58}" r="6" fill="#c0392b"/>')
text(nx+38,ny+63,"制御 VM → L1（WinRM）",size=14,fill=INK)
text(nx+38,ny+85,"→ L1 がルーティング →",size=14,fill=INK)
text(nx+38,ny+107,"L2 の IP に到達",size=14,fill=INK)
text(nx+16,ny+140,"✕ 作業PC / L0 から L2 へは",size=14,fill="#b00",weight="bold")
text(nx+16,ny+162,"  直接届かない（隔離）",size=14,fill="#b00")
text(nx+16,ny+196,"PowerShell Direct は VMBus",size=13.5,fill=SUB)
text(nx+16,ny+216,"経由でこの図の線に依存しない",size=13.5,fill=SUB)
text(nx+16,ny+238,"（IP/NIC が無いVMにも到達）",size=13.5,fill=SUB)
text(nx+16,ny+268,"NAT 上り: L1→CtrlNAT→L0→外",size=13.5,fill=SUB)

# ---- 凡例（L0 の箱の外・下）----
text(40,990,"■ 同じ横線に足を出す＝同一サブネットで直接通信可　／　別ネット間はルータ(L1)を必ず経由",size=15,fill=SUB)

add('</svg>')
svg="\n".join(P)
open("./images/net.svg","w").write(svg)
cairosvg.svg2png(bytestring=svg.encode("utf-8"),
                 write_to="./images/net.png",
                 output_width=W, output_height=H)
print("wrote net.png", W,"x",H)
