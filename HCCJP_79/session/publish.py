#!/usr/bin/env python3
"""Publish slides.md to FlowAsk. create: new event and deck. update: replace the deck markdown."""
import base64, io, json, os, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path
from PIL import Image

BASE = "https://flowask.ebisuda.net/api"
HERE = Path(__file__).resolve().parent
STATE = Path.home() / "tmp/hccjplab/flowask_state.json"  # holds the admin token. Not in the vault.
NAME = "HCCJP 第79回 さよなら同期待ち — Entra Kerberosで変わるハイブリッド参加"

def api_key():
    md = (Path.home() / "obsidian/02_Contexts/個人開発/FlowAsk/AGENTS.md").read_text(encoding="utf-8")
    armor = re.search(r"-----BEGIN AGE ENCRYPTED FILE-----.*?-----END AGE ENCRYPTED FILE-----", md, re.S).group(0)
    return subprocess.run(["age", "-d", "-i", str(Path.home() / ".config/sops/age/keys.txt")], input=armor, capture_output=True, text=True, check=True).stdout.strip()

def call(method, path, body=None, **headers):
    req = urllib.request.Request(BASE + path, data=json.dumps(body).encode() if body is not None else None, method=method,
        headers={"Content-Type": "application/json", **{k.replace("_", "-"): v for k, v in headers.items()}})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            raw = r.read(); return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        sys.exit(f"{method} {path}: {e.code} {e.read()[:400].decode(errors='replace')}")

def data_uri(p):
    im = Image.open(p).convert("RGB"); im.thumbnail((1280, 720), Image.LANCZOS); buf = io.BytesIO(); im.save(buf, "WEBP", quality=55, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()

def markdown():
    md = (HERE / "slides.md").read_text(encoding="utf-8")
    for ref in sorted(set(re.findall(r"\]\(([\w./-]+\.png)\)", md))):
        md = md.replace(f"]({ref})", f"]({data_uri(HERE / ref)})")
    if len(md) > 1_000_000:
        sys.exit(f"markdown too long for FlowAsk: {len(md)} chars (limit 1,000,000)")
    return md

if sys.argv[1] == "create":
    c = call("POST", "/events", {"name": NAME}, x_api_key=api_key())
    eid, admin = c["event"]["id"], c["adminToken"]
    s = call("POST", f"/events/{eid}/slides", {"title": NAME, "markdown": markdown(), "theme": "default"}, x_admin_token=admin)
    slide = s.get("id") or s["slide"]["id"]
    STATE.write_text(json.dumps({"eventId": eid, "adminToken": admin, "slideId": slide})); os.chmod(STATE, 0o600)
    print("keys:", sorted(k for k in c if "oken" not in k), "phase:", c["event"].get("phase"))
    print(f"event={eid} slide={slide}")
else:
    st = json.loads(STATE.read_text())
    call("PATCH", f"/events/{st['eventId']}", {"name": NAME}, x_admin_token=st["adminToken"])
    call("PATCH", f"/events/{st['eventId']}/slides/{st['slideId']}", {"title": NAME, "markdown": markdown()}, x_admin_token=st["adminToken"])
    print("updated", st["eventId"], st["slideId"])
