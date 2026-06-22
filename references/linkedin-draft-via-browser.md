# Landing the LinkedIn post as a draft (personal profile)

This skill posts from the user's personal profile (`linkedin.com/in/...`), not a company page. LinkedIn's public API does not support draft lifecycle for personal profiles, so the **only** reliable way to land a real draft is browser automation through Claude in Chrome. Do not use a `linkedin-mcp` `create_draft` tool here; it rejects personal profiles and breaks when LinkedIn deprecates API versions.

This is a standing rule: browser automation is the default path, not a fallback.

## Preconditions

1. `mcp__Claude_in_Chrome__list_connected_browsers` returns a browser. If empty, call `switch_browser` and wait for the user to click Connect in Chrome (60 to 120s).
2. The user is already logged into linkedin.com in that browser.

If Chrome isn't paired, stop and ask the user to pair it. Don't silently fall back to a paste file without telling them.

## Default sequence (text-only draft)

Drafts carry the post text only. The user attaches any image themselves after the draft lands (Chrome's `file_upload` only accepts files the user drags into chat, so automating image upload would interrupt their flow). Tell them where the suggested visual/hero idea is so they can add it.

1. `tabs_context_mcp { createIfEmpty: true }` to get a tab.
2. Navigate to `https://www.linkedin.com/feed/`.
3. Click **Start a post** to open the composer modal. Confirm it shows the user's own name as the author.
4. Click into the text area and `type` the full post body. Line breaks and unicode (📍 👉 →) come through fine. Build the post linearly from the top; never reposition the cursor with `End` (it jumps to end-of-line inside LinkedIn's contenteditable and corrupts text). If you must recover, cmd+Z walks back reliably.
5. Click the **X** to close the modal. LinkedIn pops "Save this post as a draft?" → click **Save as draft**.
6. Confirm via the toast "Draft saved." The draft is reachable from the composer's "drafts" link.

For a batch (multiple LinkedIn posts), repeat steps 3 to 6 for each post. TikTok scripts are saved as files, not LinkedIn drafts. Label each draft's first line clearly so the user can tell the posts apart at a glance.

## @mentions (only when the post names a brand/person)

A real @mention is bold in the composer and notifies the entity. Plain `@Text` is just literal text. To create one:

1. `type("@")` → `wait(1)` → `type("<name>")` → `wait(2-3)` → screenshot. Type the `@` and the name in SEPARATE actions; doing it in one batch races the picker's debounce and the dropdown never appears.
2. Screenshot, find the correct entry, and CLICK it. Do not press Enter blindly. For common names (Google, Meta), the picker lists 2nd-degree people first; arrow-down until the right org/person is highlighted, verify via screenshot, then Enter.
3. Confirm the mention rendered bold.

If a mention won't resolve, leave it as plain text and flag it in the hand-off so the user can tag it manually. Never guess a URN.

## URL preview cache trap (verify before saving)

If a post includes a link, LinkedIn auto-shortens it to `lnkd.in/<id>` and caches the preview card per shortened ID (deterministic on the destination URL string, including query params). When editing or reusing drafts, a stale preview card can silently persist.

- After typing the URL, wait 5 to 10s for the preview card, then screenshot and visually verify the card matches the intended destination.
- If stale, cache-bust by changing one UTM param (e.g. `&utm_content=v2` or bump the campaign slug). A new URL string forces a fresh fetch.
- Always tell the user the preview-card status in the hand-off.

## Hand-off

After landing drafts, tell the user:
- How many drafts landed and how to find them (composer → drafts).
- Which first-line label maps to which idea/variant.
- The suggested visual for each (they attach it).
- Any @mention or preview-card item they need to finish manually.
