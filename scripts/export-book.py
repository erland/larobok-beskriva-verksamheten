#!/usr/bin/env python3
import os
import re
import sys
import subprocess
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
META_PATHS = [ROOT / "docs" / "export-metadata.yaml", ROOT / "book.yaml"]
BUILD = ROOT / "build"
EXPORTS = ROOT / "exports"

def read_simple_yaml(path):
    if yaml:
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    data = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data

def load_metadata():
    for path in META_PATHS:
        if path.exists():
            return read_simple_yaml(path)
    raise SystemExit("Saknar docs/export-metadata.yaml eller book.yaml.")

def chapter_list(meta):
    chapters = meta.get("chapters")
    if isinstance(chapters, list) and chapters:
        return [ROOT / c for c in chapters]
    return sorted((ROOT / "chapters").glob("*.md"))

def validate_markdown(path, text):
    errors = []
    if re.search(r"^#{4,}\s", text, flags=re.MULTILINE):
        errors.append(f"{path}: innehåller H4 eller djupare rubrik.")
    if text.count("```") % 2 != 0:
        errors.append(f"{path}: ojämnt antal kodblocksmarkörer.")
    for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", text):
        target = match.group(1)
        if target.startswith(("http://", "https://")):
            continue
        image_path = (path.parent / target).resolve()
        if not image_path.exists():
            errors.append(f"{path}: saknad bildfil {target}.")
    return errors

def check_required(meta):
    errors = []
    for key in ["title", "author", "language", "identifier", "date", "version"]:
        if not meta.get(key):
            errors.append(f"Metadata saknar obligatoriskt fält: {key}")
    return errors

def pandoc_exists():
    try:
        subprocess.run(["pandoc", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        return True
    except FileNotFoundError:
        return False

def main():
    meta = load_metadata()
    errors = check_required(meta)
    chapters = chapter_list(meta)

    if not chapters:
        errors.append("Inga kapitel hittades.")

    combined = []
    for chapter in chapters:
        if not chapter.exists():
            errors.append(f"Saknat kapitel: {chapter}")
            continue
        text = chapter.read_text(encoding="utf-8")
        errors.extend(validate_markdown(chapter, text))
        combined.append(text.strip() + "\n")

    if errors:
        print("Valideringen stoppade exporten:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    BUILD.mkdir(exist_ok=True)
    EXPORTS.mkdir(exist_ok=True)
    book_md = BUILD / "book.md"
    book_md.write_text("\n\n".join(combined), encoding="utf-8")

    if not pandoc_exists():
        print("Validering klar och build/book.md skapad.")
        print("Pandoc hittades inte. Installera Pandoc för EPUB/PDF-export.")
        return

    title = meta.get("title", "")
    author = meta.get("author", "")
    lang = "sv-SE" if meta.get("language") == "sv" else meta.get("language", "en")

    epub_out = EXPORTS / "att-beskriva-verksamheten-ratt.epub"
    pdf_out = EXPORTS / "att-beskriva-verksamheten-ratt.pdf"

    subprocess.run([
        "pandoc", str(book_md),
        "--from=gfm",
        "--to=epub3",
        "--metadata", f"title={title}",
        "--metadata", f"author={author}",
        "--metadata", f"lang={lang}",
        "--css=styles/epub.css",
        "--output", str(epub_out)
    ], cwd=ROOT, check=True)

    try:
        subprocess.run([
            "pandoc", str(book_md),
            "--from=gfm",
            "--pdf-engine=xelatex",
            "--toc",
            "--toc-depth=3",
            "--metadata", f"title={title}",
            "--metadata", f"author={author}",
            "--metadata", f"lang={lang}",
            "--output", str(pdf_out)
        ], cwd=ROOT, check=True)
    except subprocess.CalledProcessError:
        print("EPUB skapades, men PDF-exporten misslyckades.")
        print("Kontrollera att xelatex finns installerat, exempelvis via MacTeX eller TinyTeX.")
        raise

    print(f"Skapade: {epub_out}")
    print(f"Skapade: {pdf_out}")

if __name__ == "__main__":
    main()
