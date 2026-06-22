#!/usr/bin/env python3
"""
Surgical edit template for the Content Ideas Apple Note.

Why surgical, not full-rebuild: regenerating the whole note from a template clobbers
hand-tuned mobile formatting (the `═` header bar lengths) and wipes any attachment.
So instead: read the live body, split into lines (one <div> per line), ASSERT the
anchor lines you expect, splice in only the lines you mean to change, and keep every
other line byte-for-byte. Then grep the result for em/en dashes before writing.

Flow:
  1. osascript reads the note body to a backup file (see apple-notes-sync.md).
  2. This script edits that text and writes the new HTML to /tmp/content_note.html.
  3. osascript sets the note body from /tmp/content_note.html (see apple-notes-sync.md).

Replace the SRC path and the anchor assertions to match YOUR note's current contents.
The assertions are the safety net: if the note shifted, the script fails loudly instead
of writing garbage. Never skip them.
"""

# 1) Load the current note body (the raw backup osascript just wrote).
SRC = "runs/<timestamp>/note-backups/content-ideas-raw-backup.txt"
lines = open(SRC, encoding="utf-8").read().split("\n")


def esc(t: str) -> str:
    """Escape HTML-significant chars for safe insertion into the note body."""
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


BLANK = "<div><br></div>"

# 2) Example edit: replace the LinkedIn prioritization list with a freshly ranked one.
#    Find the header line index first, then assert it, then splice.
#    (Indices below are illustrative; read your live note and set them from it.)

# --- locate anchors instead of hardcoding indices when you can ---
def find(needle: str) -> int:
    for i, ln in enumerate(lines):
        if needle in ln:
            return i
    raise AssertionError(f"anchor not found: {needle!r}")

li_header = find("LinkedIn (ranked")          # the LinkedIn prioritization header line
# Assert the next line is where the list starts, so we splice in the right place.
assert li_header + 1 < len(lines), "note ended right after the LinkedIn header"

# The new, freshly ranked LinkedIn list. Each line ends with an audience-fit tag.
new_li_list = [
    "1. <top idea shorthand> (strong audience fit)",
    "2. <next idea shorthand> (medium audience fit)",
    "3. <next idea shorthand> (weak audience fit)",
]

# Find where the old list ends (the first blank line after the header).
end = li_header + 1
while end < len(lines) and lines[end].strip() not in ("", "<div><br></div>"):
    end += 1

out = lines[: li_header + 1]                       # everything through the header
out += [f"<div>{esc(x)}</div>" for x in new_li_list]
out += lines[end:]                                 # the blank line onward, untouched

result = "\n".join(out)

# 3) Hard rule: no em or en dashes anywhere, ever. Fail before writing if any leaked.
assert "—" not in result and "–" not in result, "em/en dash leaked into the note"

open("/tmp/content_note.html", "w", encoding="utf-8").write(result)
print("ok", len(result), "chars written to /tmp/content_note.html")
