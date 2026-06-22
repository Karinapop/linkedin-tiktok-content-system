# Guided setup wizard

Run this when the user is setting up the skill for the first time, or anytime they ask to
(re)configure it. Triggers: "set up the content system", "set up this skill", "help me get
started", "configure the skill", or a detected first run (see below). Also run the relevant
step on demand, e.g. "redo my voice profile" or "change my note."

**This is a conversational, step-by-step flow. Do ONE step at a time, confirm it worked, then move on.** Never batch it all silently. Never publish anything. The goal: at the end, every prerequisite is green and the user has done one successful dry run.

## Detecting a first run

The skill is NOT set up yet if any of these are true:
- `references/voice-profile.md` still contains `<...>` template placeholders.
- `references/apple-notes-sync.md` still contains the `<YOUR_NOTE_ID>` placeholder.

If a user invokes the skill to make content but it's clearly a first run, pause and offer the wizard first: "Looks like this is a fresh install. Want me to walk you through a 5 minute setup so drafts sound like you and save to your note? (Or I can do a one-off draft now and set up later.)"

## The checklist

Track these out loud as you go, marking each ✅ / ⬜ so the user sees progress:

1. Chrome extension paired
2. Logged into LinkedIn (required), TikTok + X (optional)
3. macOS permission to control Notes
4. Voice profile built from their posts
5. Content Ideas note created + ID saved
6. Handles confirmed
7. (Optional) daily sync scheduled
8. Dry run

## Step 1: Pair Chrome

- Call `mcp__Claude_in_Chrome__list_connected_browsers`. If it returns a browser, ✅.
- If empty: tell the user to install the [Claude for Chrome extension](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn) if they haven't, then click **Connect** in the extension. Call `switch_browser` and wait (60 to 120s). Re-check.
- Do not proceed past this step until a browser is connected; every later step needs it.

## Step 2: Confirm logins

- In the paired Chrome, navigate to `https://www.linkedin.com/feed/` and confirm the user is logged in (you can see their name / the composer). LinkedIn is **required**.
- Optionally check `https://www.tiktok.com/` and `https://x.com/home` for logged-in state. If logged out, tell the user what they lose (TikTok trend scraping + post tracking; the X social pulse) and let them choose to log in now or skip. Web search is the fallback for whatever they skip.
- Mark ✅ for each platform that's logged in.

## Step 3: Grant macOS permission to control Notes

- Run a harmless read to trigger the permission prompt:
  ```bash
  osascript -e 'tell application "Notes" to count notes'
  ```
- The first time, macOS shows "…wants to control Notes." Tell the user to click **Allow** (or go to System Settings → Privacy & Security → Automation and enable Notes for their terminal/Claude). If the command errors with a permission/authorization message, that's the prompt being declined or pending: ask them to allow it, then retry once.
- When the command returns a number, ✅.

## Step 4: Build the voice profile

- This is the most important step. Follow `references/voice-profile-bootstrap.md` in full: read ~15 of the user's recent original LinkedIn posts and write a personalized `references/voice-profile.md` (throughline, signature moves with real quoted lines, tone dials, reference posts).
- If Chrome can't reach their posts, fall back: ask them to paste 8 to 12 of their own posts.
- Show the summary and get their "yes, that sounds like me" before moving on. ✅ only after they confirm.

## Step 5: Create + wire up the Content Ideas note

- Ask if they already have an Apple Note named `Content Ideas`. If not, have them create one (or offer to create it for them via osascript), with the single line `Content Ideas` as the title.
- Find its ID:
  ```bash
  osascript -e 'tell application "Notes"
  set out to ""
  repeat with n in (notes whose name is "Content Ideas")
  set out to out & (id of n) & "  |  modified: " & (modification date of n) & "\n"
  end repeat
  return out
  end tell'
  ```
- If multiple match, show them with modified dates and have the user pick. Confirm the right one.
- Write that ID into `references/apple-notes-sync.md`, replacing every `<YOUR_NOTE_ID>` placeholder. Also update `references/note-surgical-edit-template.py` if it carries a note path.
- Offer to scaffold the empty note structure (INBOX, PRIORITIZATION, TRENDS, LIVE, LINKEDIN, TIKTOK headers) so their first run has somewhere to write. Back up the existing body first if non-empty. ✅ when the ID is saved.

## Step 6: Confirm handles

- LinkedIn uses `/in/me/...` in their session, so no handle needed beyond being logged in.
- Ask for their TikTok handle if they want TikTok tracking, and note where `apple-notes-sync.md` references `@<your-handle>`. ✅.

## Step 7: (Optional) schedule the daily sync

- Ask if they want the daily "trends + note sync" to run automatically each morning (default 7am). If yes, set up the scheduled task. Remind them: Mac awake + Chrome paired at run time, and it never publishes on its own. If they'd rather run it manually, skip. ✅ or marked skipped.

## Step 8: Dry run

- Offer to do a real but safe first pass: sync the note (Step 0 of the main skill) and draft ONE sample idea end to end, stopping before any browser publish. This proves voice + note + scraping all work.
- Use one of their inbox ideas, or ask for a quick throwaway idea, or use a sample like "AI is changing how people search."
- Show the LinkedIn draft + a TikTok variant in chat. Confirm it sounds like them. Do NOT save a LinkedIn draft unless they ask.

## Wrap up

Report the final checklist with ✅ / ⬜ / skipped, and tell them exactly how to use it day to day: paste ideas into the note's INBOX, then say "turn my ideas into posts" or "what should I post next." Note anything still missing (e.g. "TikTok login skipped, trends will use web search until you log in").
