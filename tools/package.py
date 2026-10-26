"""Build release ZIPs for every extension listed in extensions.json.

Usage:  python tools/package.py            # all extensions
        python tools/package.py zoomer     # just one

Each entry in extensions.json:
  id            short slug used for the zip file name
  source        extension folder (absolute, or relative to SOURCE_ROOT)
  package_root  folder inside `source` that holds manifest.json ("." or "dist")
  include       files/dirs (relative to package_root) to ship
  build         optional shell command run in `source` before zipping
"""
import json
import subprocess
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONFIG = json.loads((REPO / "extensions.json").read_text(encoding="utf-8"))
SOURCE_ROOT = Path(CONFIG["source_root"])
OUT = REPO / "zips"
SKIP_NAMES = {".DS_Store", "Thumbs.db", ".git", "node_modules"}


def iter_files(base: Path, rel: str):
    p = base / rel
    if not p.exists():
        raise FileNotFoundError(f"missing include: {p}")
    if p.is_file():
        yield p
        return
    for f in sorted(p.rglob("*")):
        if f.is_file() and not (set(f.relative_to(base).parts) & SKIP_NAMES):
            yield f


def check_manifest_refs(root: Path, manifest: dict, shipped: set):
    """Warn about files the manifest references that are not in the zip."""
    refs = []
    bg = manifest.get("background", {})
    refs += [bg.get("service_worker")] if bg.get("service_worker") else []
    for cs in manifest.get("content_scripts", []):
        refs += cs.get("js", []) + cs.get("css", [])
    refs += list((manifest.get("icons") or {}).values())
    action = manifest.get("action", {})
    refs += [action.get("default_popup")] if action.get("default_popup") else []
    refs += list((action.get("default_icon") or {}).values()) if isinstance(action.get("default_icon"), dict) else []
    for key in ("options_page",):
        if manifest.get(key):
            refs.append(manifest[key])
    for key in ("side_panel", "options_ui"):
        if (manifest.get(key) or {}).get("default_path" if key == "side_panel" else "page"):
            refs.append(manifest[key].get("default_path") or manifest[key].get("page"))
    missing = [r for r in refs if r and r.lstrip("/").replace("\\", "/") not in shipped]
    return missing


def resolve_msg(root: Path, manifest: dict, value: str) -> str:
    """Turn "__MSG_key__" into its default-locale text."""
    if not value.startswith("__MSG_"):
        return value
    key = value[6:-2]
    msgs = root / "_locales" / manifest.get("default_locale", "en") / "messages.json"
    data = json.loads(msgs.read_text(encoding="utf-8-sig"))
    entry = next((v for k, v in data.items() if k.lower() == key.lower()), None)
    return entry["message"] if entry else value


def build(ext: dict) -> Path:
    src = Path(ext["source"])
    if not src.is_absolute():
        src = SOURCE_ROOT / src
    if ext.get("build"):
        print(f"  build: {ext['build']}")
        subprocess.run(ext["build"], cwd=src, shell=True, check=True)
    root = src / ext.get("package_root", ".")
    manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8-sig"))
    version = manifest["version"]

    files = {}
    for rel in ["manifest.json", *ext["include"]]:
        for f in iter_files(root, rel):
            files[f.relative_to(root).as_posix()] = f

    missing = check_manifest_refs(root, manifest, set(files))
    if missing:
        raise RuntimeError(f"{ext['id']}: manifest references files not shipped: {missing}")

    OUT.mkdir(exist_ok=True)
    zip_path = OUT / f"{ext['id']}.zip"  # stable name so website links never break
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for arc, f in sorted(files.items()):
            z.write(f, arc)
    ext["_version"] = version
    ext["_name"] = resolve_msg(root, manifest, manifest.get("name", ""))
    print(f"  -> {zip_path.name} ({len(files)} files, {zip_path.stat().st_size // 1024} KB)")
    return zip_path


def main():
    wanted = set(sys.argv[1:])
    results = []
    for ext in CONFIG["extensions"]:
        if wanted and ext["id"] not in wanted:
            continue
        print(f"[{ext['id']}]")
        build(ext)
        results.append({"id": ext["id"], "name": ext["_name"], "version": ext["_version"],
                        "zip": f"zips/{ext['id']}.zip"})
    if not wanted:
        (OUT / "index.json").write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
