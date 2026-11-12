import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
HOME_NOTE = "README.md"
EXCLUDED_DIRS = {".git", ".github", ".obsidian", "_plantillas", "scripts"}
EXCLUDED_FILES = {"CONTRIBUTING.md"}
FORBIDDEN_NAME_CHARS = set('¿?|/\\:*"<>#^[]')
NOTION_ID = re.compile(r"[0-9a-f]{32}")
LOCAL_LINK = re.compile(r"!?\[[^\]]*\]\((?!https?:|mailto:)(\S+?\.[A-Za-z0-9]+)(?:#[^)\s]*)?\)")
ANGLE_LINK = re.compile(r"\]\(<[^>]+>\)")
WIKILINK = re.compile(r"\[\[[^\]]+\]\]")
LINK_FORMAT_HINT = "usa links Markdown como los genera Obsidian: [texto](Mi%20nota.md)"


def find_notes():
    for path in sorted(ROOT.rglob("*.md")):
        relative = path.relative_to(ROOT)
        if EXCLUDED_DIRS.intersection(relative.parts[:-1]) or str(relative) in EXCLUDED_FILES:
            continue
        yield path


def name_errors(relative):
    errors = []
    bad_chars = sorted(FORBIDDEN_NAME_CHARS.intersection(relative.stem))
    if bad_chars:
        errors.append(f"{relative}: el nombre tiene caracteres no permitidos: {' '.join(bad_chars)}")
    if NOTION_ID.search(relative.stem):
        errors.append(f"{relative}: el nombre conserva un ID de Notion")
    return errors


def content_errors(relative, text):
    errors = []
    if not text.startswith("# "):
        errors.append(f"{relative}: la primera línea debe ser el título, con formato '# Título'")
    if WIKILINK.search(text):
        errors.append(f"{relative}: hay [[wikilinks]]; {LINK_FORMAT_HINT}")
    if ANGLE_LINK.search(text):
        errors.append(f"{relative}: hay links con <ruta>; {LINK_FORMAT_HINT}")
    return errors


def check_links(path, text, linked):
    errors = []
    for match in LOCAL_LINK.finditer(text):
        destination = unquote(match.group(1))
        target = (path.parent / destination).resolve()
        if not target.is_file():
            errors.append(f"{path.relative_to(ROOT)}: link roto a '{destination}'")
            continue
        linked.add(target)
    return errors


def main():
    notes = list(find_notes())
    linked = set()
    errors = []
    for path in notes:
        relative = path.relative_to(ROOT)
        text = path.read_text(encoding="utf-8")
        errors += name_errors(relative)
        errors += content_errors(relative, text)
        errors += check_links(path, text, linked)
    orphans = [p for p in notes if p.resolve() not in linked and p.name != HOME_NOTE]
    errors += [f"{p.relative_to(ROOT)}: ninguna nota la enlaza; agrégala al índice de su carpeta" for p in orphans]
    for error in errors:
        print(error)
    print(f"{len(notes)} notas revisadas, {len(errors)} errores")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
