"""Check image publication and safe updates without contacting FlowAsk."""

import importlib.util
import json
from pathlib import Path
from unittest.mock import patch

import pytest

SPEC = importlib.util.spec_from_file_location(
    "hccjp_publisher", Path(__file__).with_name("publish.py")
)
publisher = importlib.util.module_from_spec(SPEC)
with patch(
    "urllib.request.urlopen", side_effect=AssertionError("Import must not publish")
):
    SPEC.loader.exec_module(publisher)


@pytest.fixture
def images(tmp_path, monkeypatch):
    source = tmp_path / "slides.md"
    source.write_text("# Title\n\n![bg contain](figure.png)\n", encoding="utf-8")
    (tmp_path / "figure.png").write_bytes(b"original-png")
    uploads = []
    content = {}

    def api(method, path, **kwargs):
        assert method == "POST"
        assert path == "/events/434629/slides/images"
        assert kwargs["content_type"] == "image/png"
        url = f"/api/events/434629/images/{len(uploads) + 1:032x}.png"
        uploads.append(kwargs["raw"])
        content[publisher.ORIGIN + url] = kwargs["raw"]
        return {"url": url}

    monkeypatch.setattr(publisher, "api", api)
    monkeypatch.setattr(publisher, "download_image", lambda url: content[url])
    return source, tmp_path / "cache.json", uploads


def test_uploaded_url_preserves_markdown(images):
    source, cache, uploads = images
    result = publisher.render_markdown("434629", "secret", source, cache)
    assert (
        "![bg contain](https://flowask.ebisuda.net/api/events/434629/images/" in result
    )
    assert "data:image" not in result
    assert result.startswith("# Title\n")
    assert uploads == [b"original-png"]
    assert "secret" not in cache.read_text()


def test_reuses_unchanged_image_and_uploads_changed_image(images):
    source, cache, uploads = images
    first = publisher.render_markdown("434629", "secret", source, cache)
    assert publisher.render_markdown("434629", "secret", source, cache) == first
    assert len(uploads) == 1
    (source.parent / "figure.png").write_bytes(b"changed-png")
    assert publisher.render_markdown("434629", "secret", source, cache) != first
    assert len(uploads) == 2


def test_rejects_cross_origin_upload_url(images, monkeypatch):
    source, cache, _ = images
    monkeypatch.setattr(
        publisher, "api", lambda *a, **k: {"url": "https://example.com/image.png"}
    )
    with pytest.raises(ValueError, match="image URL"):
        publisher.render_markdown("434629", "secret", source, cache)


def test_rejects_corrupted_image(images, monkeypatch):
    source, cache, _ = images
    monkeypatch.setattr(publisher, "download_image", lambda url: b"wrong-content")
    with pytest.raises(ValueError, match="checksum"):
        publisher.render_markdown("434629", "secret", source, cache)


def test_upload_failure_does_not_patch_deck(tmp_path, monkeypatch):
    state = tmp_path / "state.json"
    state.write_text(
        json.dumps({"eventId": "434629", "slideId": "deck", "adminToken": "secret"})
    )
    calls = []

    def api(method, path, **kwargs):
        calls.append(method)
        return {"markdown": "current"}

    def fail(*args, **kwargs):
        raise OSError("Upload failed")

    monkeypatch.setattr(publisher, "api", api)
    monkeypatch.setattr(publisher, "render_markdown", fail)
    with pytest.raises(OSError):
        publisher.update(state)
    assert calls == ["GET"]


def test_concurrent_edit_does_not_get_overwritten(tmp_path, monkeypatch):
    state = tmp_path / "state.json"
    state.write_text(
        json.dumps({"eventId": "434629", "slideId": "deck", "adminToken": "secret"})
    )
    calls = []

    def api(method, path, **kwargs):
        calls.append(method)
        return {"markdown": "before" if len(calls) == 1 else "human edit"}

    monkeypatch.setattr(publisher, "api", api)
    monkeypatch.setattr(publisher, "render_markdown", lambda *a, **k: "new content")
    with pytest.raises(RuntimeError, match="changed"):
        publisher.update(state)
    assert calls == ["GET", "GET"]
