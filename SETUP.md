# One-time setup

The skill is built to sound like *you*, work from *your* note, and post to *your* accounts. Do this once before your first real run. All of it is conversational: you ask Claude, it does the steps.

## 1. Build your voice profile (most important)

This is what makes drafts sound like you instead of like a generic LinkedIn post.

- Make sure Chrome is running with the Claude in Chrome extension paired, and you're logged into LinkedIn.
- Ask Claude: **"build my voice profile from my LinkedIn."**
- It opens your activity feed, reads ~15 of your recent original posts, and fills in `references/voice-profile.md`: your throughline, signature moves (with real example lines from your posts), tone dials, and a few reference posts.
- It will show you a summary and ask if it sounds like you. Adjust from there.

No Chrome? Paste 8 to 12 of your own posts into chat and say "build my voice profile from these." That's enough.

You can refresh this anytime your voice evolves: "refresh my voice profile from my latest posts."

## 2. Set up your Content Ideas note

The skill uses ONE Apple Note as the master content doc, targeted by a stable ID so it can never clobber another note.

- In Apple Notes, create a note named **Content Ideas** (or pick an existing one).
- Ask Claude: **"find my Content Ideas note ID."** It lists matching notes and their IDs, you confirm the right one, and it sets that ID in `references/apple-notes-sync.md` (replacing the `<YOUR_NOTE_ID>` placeholder).
- That's it. From now on you just paste raw ideas into the note's INBOX and the skill drains them each run.

The skill maintains the note's structure for you (inbox, two priority lists, trends, live analytics, draft sections). You only ever have to touch the INBOX.

## 3. Confirm your handles

- **LinkedIn:** the skill uses `linkedin.com/in/me/...` in your logged-in session, so no handle needed beyond being logged in.
- **TikTok (optional):** if you want trend scraping and published-post tracking on TikTok, tell Claude your TikTok handle and make sure you're logged into TikTok in the same Chrome. The skill stores it where `apple-notes-sync.md` references `@<your-handle>`.

## 4. (Optional) Schedule the daily sync

The skill can run a daily "trends + note sync" in the morning: it scrapes ~200 posts across LinkedIn, X, and TikTok, refreshes trends, updates your published-post analytics and learnings, and reprioritizes your ideas. It never touches the browser to publish on its own.

Ask Claude to "set up the daily content trends and note sync at 7am" (or your preferred time). Requires your Mac awake and Chrome paired at run time; Apple Notes is local, so this only works on-machine, not in a cloud run.

## You're ready

Paste a few ideas into your note's INBOX (or just say one in chat) and ask: **"turn my ideas into posts."**
