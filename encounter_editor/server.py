"""Local encounter-rules editor. Stdlib only, bound to 127.0.0.1.

Edits the farm's live encounter_rules.json (the parent of this folder).
Never writes the simulator pin.
"""
from __future__ import annotations

import argparse
import json
import re
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

import encounter_rules as rules

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
DEFAULT_JSON = rules.default_rules_path()
VENDOR_SPRITES = ROOT / "vendor" / "pokerogue" / "assets" / "images" / "mystery-encounters"
SPRITE_NAME = re.compile(r"^[A-Za-z0-9_-]+\.png$")


def sprite_file(key: str) -> Path | None:
    if not key:
        return None
    name = f"{key}.png"
    for folder in (HERE / "sprites", VENDOR_SPRITES):
        path = folder / name
        if path.is_file():
            return path
    return None


def make_server(json_path: Path | str, host: str = "127.0.0.1", port: int = 8766) -> ThreadingHTTPServer:
    path = Path(json_path).resolve()
    rules.assert_not_sim_pin(path)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt: str, *args) -> None:
            return

        def _send(self, code: int, body, content_type: str = "application/json") -> None:
            if not isinstance(body, (bytes, bytearray)):
                body = json.dumps(body).encode()
            self.send_response(code)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def _origin_ok(self) -> bool:
            origin = self.headers.get("Origin")
            host_header = self.headers.get("Host") or f"{host}:{port}"
            allowed = {None, f"http://{host_header}", f"http://127.0.0.1:{self.server.server_address[1]}", f"http://localhost:{self.server.server_address[1]}"}
            return origin in allowed

        def do_GET(self) -> None:
            route = self.path.split("?", 1)[0]
            try:
                if route in ("/", "/index.html"):
                    self._send(200, (HERE / "index.html").read_bytes(), "text/html; charset=utf-8")
                    return
                if route.startswith("/sprites/"):
                    name = Path(route[9:]).name
                    if not SPRITE_NAME.match(name):
                        self._send(404, {"error": "no sprite"})
                        return
                    file = sprite_file(name[:-4])
                    if file is None:
                        self._send(404, {"error": "no sprite"})
                        return
                    self._send(200, file.read_bytes(), "image/png")
                    return
                if route == "/api/data":
                    self._send(200, payload(self.server.json_path))
                    return
                if route == "/api/backups":
                    folder = self.server.json_path.parent / "encounter_rules_backups"
                    folder.mkdir(parents=True, exist_ok=True)
                    names = sorted((item.name for item in folder.glob("*.json")), reverse=True)[:100]
                    self._send(200, {"backups": names})
                    return
                if route == "/api/ping":
                    self._send(200, {"ok": True, "json": str(self.server.json_path)})
                    return
                self._send(404, {"error": "not found"})
            except Exception as exc:
                self._send(500, {"error": repr(exc)})

        def do_POST(self) -> None:
            route = self.path.split("?", 1)[0]
            if not self._origin_ok():
                self._send(403, {"error": "bad origin"})
                return
            try:
                length = int(self.headers.get("Content-Length") or 0)
                body = json.loads(self.rfile.read(length) or b"{}")
                with self.server.lock:
                    current, mtime = read_doc(self.server.json_path)
                    if route == "/api/save":
                        if body.get("base_mtime") is not None and abs(float(body["base_mtime"]) - mtime) > 1e-4:
                            self._send(409, {"error": "encounter_rules.json changed on disk since you loaded it. Reset to file and redo your edits."})
                            return
                        updated = rules.apply_edit(current, body)
                        if updated == current:
                            self._send(200, {"ok": True, "unchanged": True, **payload(self.server.json_path)})
                            return
                        backup = rules.save_document(self.server.json_path, updated, "presave")
                        self._send(200, {"ok": True, "backup": backup.name if backup else None, **payload(self.server.json_path)})
                        return
                    if route == "/api/revert":
                        name = Path(str(body.get("name") or "")).name
                        folder = self.server.json_path.parent / "encounter_rules_backups"
                        file = folder / name
                        if not name or not file.is_file():
                            self._send(404, {"error": "backup not found"})
                            return
                        restored = json.loads(file.read_text(encoding="utf-8"))
                        rules.validate(restored)
                        backup = rules.save_document(self.server.json_path, restored, "prerevert")
                        self._send(200, {"ok": True, "reverted_to": name, "backup": backup.name if backup else None, **payload(self.server.json_path)})
                        return
                    if route == "/api/quit":
                        threading.Timer(0.3, lambda: os_exit()).start()
                        self._send(200, {"ok": True})
                        return
                self._send(404, {"error": "not found"})
            except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
                self._send(400, {"error": f"validation failed: {exc}"})
            except Exception as exc:
                self._send(500, {"error": repr(exc)})

    httpd = ThreadingHTTPServer((host, port), Handler)
    httpd.json_path = path
    httpd.lock = threading.Lock()
    return httpd


def os_exit() -> None:
    import os
    os._exit(0)


def read_doc(path: Path) -> tuple[dict, float]:
    return json.loads(path.read_text(encoding="utf-8")), path.stat().st_mtime


def payload(path: Path) -> dict:
    doc, mtime = read_doc(path)
    sprites = {}
    real = 0
    for encounter in doc["encounters"]:
        key = encounter.get("sprite_key") or ""
        found = sprite_file(key) is not None
        sprites[encounter["key"]] = {"key": key, "found": found}
        real += int(found)
    return {
        "data": doc,
        "mtime": mtime,
        "path": str(path),
        "live": path.resolve() == DEFAULT_JSON.resolve(),
        "hash": rules.content_hash(doc),
        "short_hash": rules.short_hash(doc),
        "sprites": sprites,
        "sprite_real": real,
        "sprite_total": len(doc["encounters"]),
        "md_path": str(rules.markdown_path_for(path)),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Encounter rules editor")
    parser.add_argument("--json", default=None, help="rules file (else ENCOUNTER_RULES_JSON, else the platform default)")
    parser.add_argument("--port", type=int, default=8766)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    path = Path(args.json).resolve() if args.json else rules.default_rules_path().resolve()
    if not path.is_file():
        raise SystemExit(f"rules file not found: {path}")
    httpd = make_server(path, "127.0.0.1", args.port)
    url = f"http://127.0.0.1:{args.port}/"
    print("Encounter editor on", url, "editing", path, flush=True)
    if not args.no_browser:
        threading.Timer(0.4, lambda: webbrowser.open(url)).start()
    httpd.serve_forever()


if __name__ == "__main__":
    main()
