from datetime import datetime, timezone
from pathlib import Path

SPEC = {
    "name": "write_note",
    "description": "Save a short note to notes/<title>.md in the working directory.",
    "args": {
        "title": {"type": "string", "description": "File name for the note, without extension."},
        "body": {"type": "string", "description": "The note's text."},
    },
}


def run(title, body):
    safe = "".join(c for c in title if c.isalnum() or c in "-_") or "note"
    path = Path("notes") / f"{safe}.md"
    path.parent.mkdir(exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path.write_text(f"# {title}\n\n{body}\n\n_written by write_note at {stamp}_\n")
    return {"written": str(path), "source": "write_note"}
