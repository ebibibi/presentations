#!/usr/bin/env python3
"""Publish HCCJP slides using uploaded, stable FlowAsk image URLs."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ORIGIN = "https://flowask.ebisuda.net"
BASE = ORIGIN + "/api"
HERE = Path(__file__).resolve().parent
STATE = Path.home() / "tmp/hccjplab/flowask_state.json"
IMAGE_CACHE = STATE.with_name("flowask_image_cache.json")
NAME = "HCCJP 第79回 さよなら同期待ち — Entra Kerberosで変わるハイブリッド参加"
LOCAL_IMAGE = re.compile(r"\]\(([\w./-]+\.png)\)")


def private_json(path: Path, value: dict[str, Any]) -> None:
    """Persist progress without writing credentials into the repository."""
    temporary = path.with_suffix(".tmp")
    fd = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as output:
        json.dump(value, output, ensure_ascii=False)
    os.replace(temporary, path)


def api_key() -> str:
    note = (Path.home() / "obsidian/02_Contexts/個人開発/FlowAsk/AGENTS.md").read_text(
        encoding="utf-8"
    )
    match = re.search(
        r"-----BEGIN AGE ENCRYPTED FILE-----.*?-----END AGE ENCRYPTED FILE-----",
        note,
        re.S,
    )
    if not match:
        raise ValueError("FlowAsk API key not found")
    result = subprocess.run(
        ["age", "-d", "-i", str(Path.home() / ".config/sops/age/keys.txt")],
        input=match.group(0),
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout.strip()


def api(
    method: str,
    path: str,
    *,
    admin_token: str | None = None,
    key: str | None = None,
    body: dict[str, Any] | None = None,
    raw: bytes | None = None,
    content_type: str = "application/json",
) -> dict[str, Any]:
    headers = {"Content-Type": content_type}
    if admin_token:
        headers["x-admin-token"] = admin_token
    if key:
        headers["x-api-key"] = key
    data = json.dumps(body).encode() if body is not None else raw
    request = urllib.request.Request(
        BASE + path, data=data, method=method, headers=headers
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        result = response.read()
    return json.loads(result) if result else {}


def download_image(url: str) -> bytes:
    """Check the same public image URL the rendered deck will use."""
    with urllib.request.urlopen(url, timeout=60) as response:
        if response.headers.get_content_type() != "image/png":
            raise ValueError("Uploaded image has an unexpected content type")
        return response.read()


def image_url(
    event_id: str, admin_token: str, path: Path, images: dict[str, str]
) -> str:
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    url = images.get(digest)
    prefix = f"{ORIGIN}/api/events/{event_id}/images/"
    if url and not url.startswith(prefix):
        raise ValueError("Cached image URL does not belong to this event")
    if url:
        try:
            if hashlib.sha256(download_image(url)).hexdigest() != digest:
                raise ValueError(f"Cached image checksum mismatch: {path.name}")
            return url
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise
    uploaded = api(
        "POST",
        f"/events/{event_id}/slides/images",
        admin_token=admin_token,
        raw=data,
        content_type="image/png",
    )
    relative = uploaded.get("url", "")
    if not re.fullmatch(
        rf"/api/events/{re.escape(event_id)}/images/[0-9a-f-]+\.png", relative
    ):
        raise ValueError("Unexpected uploaded image URL")
    url = ORIGIN + relative
    if hashlib.sha256(download_image(url)).hexdigest() != digest:
        raise ValueError(f"Uploaded image checksum mismatch: {path.name}")
    images[digest] = url
    return url


def render_markdown(
    event_id: str,
    admin_token: str,
    source: Path = HERE / "slides.md",
    cache_file: Path = IMAGE_CACHE,
) -> str:
    markdown = source.read_text(encoding="utf-8")
    if "data:image/" in markdown:
        raise ValueError("Use local images or uploaded URLs, not data:image content")
    refs = sorted(set(LOCAL_IMAGE.findall(markdown)))
    # Validate every file before uploading or changing the deck.
    for ref in refs:
        path = (source.parent / ref).resolve()
        if not path.is_relative_to(source.parent.resolve()) or not path.is_file():
            raise ValueError(f"Invalid local image: {ref}")
        if not 0 < path.stat().st_size <= 5 * 1024 * 1024:
            raise ValueError(f"Image must be between 1 byte and 5 MB: {ref}")
    cache = json.loads(cache_file.read_text()) if cache_file.exists() else {}
    images = dict(cache.get("images", {})) if cache.get("eventId") == event_id else {}
    for ref in refs:
        url = image_url(event_id, admin_token, source.parent / ref, images)
        private_json(cache_file, {"eventId": event_id, "images": images})
        markdown = markdown.replace(f"]({ref})", f"]({url})")
    if len(markdown) > 1_000_000:
        raise ValueError("Markdown exceeds the FlowAsk character limit")
    return markdown


def update(state_file: Path = STATE) -> None:
    state = json.loads(state_file.read_text())
    event_id, token = str(state["eventId"]), state["adminToken"]
    path = f"/events/{event_id}/slides/{state['slideId']}"
    before = api("GET", path, admin_token=token)
    markdown = render_markdown(event_id, token)
    current = api("GET", path, admin_token=token)
    if current["markdown"] != before["markdown"]:
        raise RuntimeError(
            "FlowAsk content changed during image publication; update stopped"
        )
    api("PATCH", path, admin_token=token, body={"markdown": markdown})
    saved = api("GET", path, admin_token=token)
    if saved["markdown"] != markdown:
        raise RuntimeError("Published content does not match the source")
    print("updated", event_id, state["slideId"], "characters:", len(markdown))


def create() -> None:
    result = api("POST", "/events", key=api_key(), body={"name": NAME})
    event_id, token = str(result["event"]["id"]), result["adminToken"]
    markdown = render_markdown(event_id, token)
    slide = api(
        "POST",
        f"/events/{event_id}/slides",
        admin_token=token,
        body={"title": NAME, "markdown": markdown, "theme": "default"},
    )
    slide_id = slide.get("id") or slide["slide"]["id"]
    private_json(STATE, {"eventId": event_id, "adminToken": token, "slideId": slide_id})
    print("created", event_id, slide_id)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("create", "update"))
    action = parser.parse_args().action
    if action == "create":
        create()
    else:
        update()


if __name__ == "__main__":
    main()
