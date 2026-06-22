# Apple Notes sync: the Content Ideas note is the source of truth

You keep one Apple Note as the master content doc. Every run of this skill READS from it at the start and WRITES back to it at the end. The chat is for review and iteration; the note is the system of record. Never let the note and the runs/ files drift: the note wins, the runs/ files are a backup/working copy.

## First-time setup: point the skill at your note

This skill writes to ONE specific Apple Note, targeted by its stable note ID (not by name, so it can never clobber a different note). Before the first run:

1. Create (or pick) an Apple Note named `Content Ideas`. This is where you'll paste raw ideas.
2. Find its note ID. Easiest way: ask the skill "find my Content Ideas note ID" and it will run the AppleScript below to list matching notes and their IDs, then confirm the right one with you. The ID looks like `x-coredata://<UUID>/ICNote/p<NNNN>`.
3. Set that ID as `NOTE_ID` everywhere in this file (replace the `<YOUR_NOTE_ID>` placeholder) and in `references/note-surgical-edit-template.py`.

```bash
# List notes named "Content Ideas" and their IDs, so you can pick the right one
osascript -e 'tell application "Notes"
set out to ""
repeat with n in (notes whose name is "Content Ideas")
set out to out & (id of n) & "  |  modified: " & (modification date of n) & "\n"
end repeat
return out
end tell'
```

If you have more than one note with the same name, pick the one with the most recent modification date and confirm it before writing. If the ID ever stops resolving (Notes can reassign on major edits/migrations), re-find it by name + most-recent modification date. Always back up the current body to disk before overwriting (see below).

> Throughout this file, `<YOUR_NOTE_ID>` is a placeholder. Replace it with your real note ID once.

## Structure of the note (keep it in this exact order)

1. **Title line:** `Content Ideas`.
2. **INBOX (new ideas)**: where you paste raw new ideas, half-thoughts, links, or written-out thoughts for an existing draft. The skill drains it every run, then resets it to `(empty)`.
3. **PRIORITIZATION**: TWO sub-lists, `LinkedIn (ranked for LinkedIn reach):` and `TikTok (ranked for TikTok reach):`. Each line is the idea source (your shorthand), numbered, in priority order, followed by a plain-text **audience-fit tag** in parentheses: `(strong audience fit)` / `(medium audience fit)` / `(weak audience fit)`. No status tags, no platform suffixes, no tiers (the audience-fit tag is the only parenthetical, plus any pre-existing sequencing note). The two lists are ranked INDEPENDENTLY: LinkedIn by what's trending/performing on LinkedIn, TikTok by what's trending/performing on TikTok (including the niche intersections you track). Audience fit (how well the idea matches your most-engaged audience, especially NEW followers, per the LIVE LEARNINGS) is a ranking input alongside trend relevance and expected performance. See "Audience-fit weighting" below.
4. **TRENDS (updated YYYY-MM-DD)**: its own section, right below prioritization. Refreshed by the daily scheduled run (and any manual run). Short, scannable: sources line, LinkedIn + X trends, TikTok trends with your tracked intersections, format notes.
5. **LIVE (its own top-level section; sits right after TRENDS)**: published posts with their analytics, so performance + learnings are front and center. It opens with a **LEARNINGS (updated YYYY-MM-DD)** readout (what's working + who the most-engaged / newest-follower audience is + the directives applied to drafts), then TWO subsections, `LinkedIn` and `TikTok`, each holding the tracking entries for that platform sorted NEWEST FIRST. This is the ONLY place LIVE/published posts live; the per-platform draft sections below no longer carry a LIVE stage. See "Posted-post tracking" and "LIVE LEARNINGS" below.
6. **LINKEDIN**: idea blocks organized by stage subheaders, in this order: `LOCKED`, `ITERATION`, `EARLY DRAFTS`. (`LOCKED` = locked posts, including those already saved as a LinkedIn draft, that are not yet live. There is no `LIVE` stage here: published posts live in the top-level LIVE section. There is no `IDEAS` stage.)
7. **TIKTOK**: same stage subheaders (`LOCKED`, `ITERATION`, `EARLY DRAFTS`). TikTok early-draft blocks carry **3 to 5 variants** each (see below).

Keep the note lean: your content, the lists, the trends, the LIVE analytics + learnings, nothing meta. Never re-add scaffolding you removed (e.g. a "HOW THIS WORKS" explainer).

### Formatting conventions (match them EXACTLY everywhere)
The approach is SURGICAL line edits on the live note HTML, not full rebuilds: read the body, split on newlines (one `<div>` per line), assert anchor lines before splicing, replace only the lines you mean to change, keep every other line (especially section headers and your writing) byte-for-byte, grep the result for `[—–]`, then write. Template: `references/note-surgical-edit-template.py`. Never hand-roll the whole note from templates; full rebuilds are what clobber mobile formatting and wipe attachments.

- **NO COLOR ANYWHERE.** Everything in the note is plain default black: headers, stage subheaders, LIVE subsection headers, audience-fit tags, titles, body. NEVER wrap anything in `<font color="#HEX">` or `<span style="color:#HEX">`. If a read shows any `font color` tags, strip them (regex: `<font color="#[0-9A-Fa-f]{6}">(.*?)</font>` -> `\1`). The only formatting that carries is bold (`<b>`), underline (`<u>`), `<h2>` subheaders, and any `<span style="font-size">` sizes already in the headers.
- **Top section headers** (INBOX, PRIORITIZATION, TRENDS, LIVE, LINKEDIN, TIKTOK): bold bars, NO emoji, NO color. **PRESERVE YOUR EXACT HEADER LINES VERBATIM** once you've set them: if you hand-tune the `═` bar lengths per header so they fit on your phone without wrapping, copy each header line exactly as read from the live note at Step 0 (the only permitted change is the date inside the TRENDS/LEARNINGS header text). Differing bar lengths per header is intentional mobile-friendly formatting, not drift to fix. Never alter the `═` count or the words.
- **Stage subheaders** (LOCKED / ITERATION / EARLY DRAFTS): a clean bold heading, single word(s) only, NO color. Render `<div><b><h2>NAME</h2></b></div>`. NO emoji, NO `──────` bars, NO parenthetical description. It is `ITERATION`, not "IN ITERATION".
- **LIVE-section subsection headers** (`LinkedIn` and `TikTok` inside the LIVE section): same `<h2>` treatment, plain black, NO color.
- **Idea block title = the SOURCE IDEA** (your shorthand from the prioritization list), bold + underlined, NO `###` and NO `[STATUS]` tag. Render `<div><b><u>the source idea</u></b></div>`. The title IS the idea, so there is NO separate "Idea (source)" line. Any headline/hook lives as the first line of the Draft, not the title.
- **No emoji in any header or title.** Emoji are fine inside draft/caption body text.
- **Every idea has a draft.** Don't leave bare ideas. When a new idea lands, draft it immediately (LinkedIn: one merged post; TikTok: 3 to 5 variants) so it goes straight under EARLY DRAFTS.

Each idea block:
```
<bold+underline SOURCE IDEA as the title>
Your thoughts: <your writing, verbatim>   <- show whenever non-empty (never drop your writing); omit the line entirely if empty
Draft: <the current draft>                <- LinkedIn blocks
```
TikTok blocks use the SAME title + optional thoughts, then 3 to 5 variants, each in the **Draft / Caption / Format** shape:
```
V1 (short label):
Draft: <the spoken script; the hook is its first line>
Caption: <caption text, with hashtags appended here>
Format: <talking head / voiceover+demo / skit, plus the visual cue and sound note, all on this line>
```
No separate Hook/Script/Tags/Visual/Sound lines; fold the hook into the Draft, hashtags into the Caption, and visual+sound into the Format. LOCKED TikTok blocks can also list "F1/F2" follow-up shoots in the same Draft/Caption/Format shape.

A "both platforms" idea appears as TWO blocks (one per section), sharing the same core insight. Internal status values still drive placement: `[IDEA] [EARLY DRAFT] [REWORKED] [LOCKED] [DRAFTED] [POSTED]` (IDEA and EARLY DRAFT → EARLY DRAFTS, REWORKED → ITERATION, LOCKED/DRAFTED → LOCKED, POSTED → the top-level **LIVE** section under the matching platform subsection, as a metrics tracking entry sorted newest first), but the tags are NOT printed in the note. (`DRAFTED` = locked + saved as a LinkedIn draft, no schedule.) A block whose "Your thoughts" is filled but not yet absorbed into the draft is owed a REWORK.

### Links and attachments in Notes (hard limitation)
Setting the note body via osascript STRIPS every `<a href>` anchor, both `file://` and `https://`. URLs survive only as plain text (Notes may re-detect them as tappable when you open the note, but don't rely on it). And file ATTACHMENTS can't be added via osascript at all, and a `set body` rebuild wipes any attachment that was added by hand. Consequences:
- Posted-post links in tracking entries go in as plain-text URLs (still useful; you can copy or long-press).
- Companion files (a report PDF, a deck) can't live durably inside Content Ideas (a rebuild erases them). Keep them in a separate note (never rebuilt) plus on disk, and reference them in text from Content Ideas. Re-drag the file into the companion note by hand if you want it in-note.

## The 5-stage process (the workflow, honor it)

1. **IDEA**: you write shorthand (inbox or chat).
2. **EARLY DRAFT**: the skill prioritizes it and writes a first draft (LinkedIn: one merged post; TikTok: 3 to 5 variants).
3. **YOUR THOUGHTS**: you write out everything you think.
4. **REWORKED**: the skill uses your thoughts to write a genuinely stronger draft; move the block up under ITERATION.
5. **LOCKED**: you iterate together until you lock it; move the block to the top under LOCKED.

Then **DRAFTED** (saved as a LinkedIn draft, NO schedule; stays under LOCKED) and **POSTED** (moves to the top-level LIVE section as a deep-analytics tracking entry, refreshed every run, see below).

## Posted-post tracking + deep analytics (pull FULL per-post analytics, not just the surface counts)

Published posts live in the top-level **LIVE** section (right after TRENDS), split into a `LinkedIn` subsection and a `TikTok` subsection, each sorted NEWEST FIRST. Posted posts drop off the PRIORITIZATION lists (they're done); the LIVE entry stays and its analytics are refreshed every run. The point of going deep here is the LEARNINGS loop: the per-post numbers AND demographics are what you mine to align every future draft to the best-performing, newest-follower audience (see "LIVE LEARNINGS" below).

**Click INTO each post's full analytics, don't stop at the feed counts.** The activity feed only shows impressions + a reaction count. The real signal (reach, demographics, follows gained, profile/page visits, saves) is behind the post's own analytics view. For each live post, open its dedicated analytics and capture everything available for that platform.

**Pull analytics at two checkpoints: a frozen 24-hour snapshot, then a rolling latest.** The first run AFTER a post crosses 24 hours old, capture a `@24h` snapshot and FREEZE it (never overwrite it; it's the clean early-velocity read). Every run after that, refresh the `latest` line. So a mature entry shows both: how it opened (24h) and where it stands now. If a post is still under 24h old this run, capture a `<24h (as of <time>)` provisional line and replace it with the frozen `@24h` snapshot once it crosses the mark.

Tracking-entry format (LinkedIn):
```
<bold+underline POST NAME>
Posted: <YYYY-MM-DD (edited if applicable)>
Link: <plain-text post URL>   (anchors get stripped by osascript; leave the URL as text)
Metrics @24h: <impressions, members reached, reactions, comments, reposts, saves, new followers, profile/page visits> (frozen 24h read)
Metrics latest: <same fields> (as of <date>)
Audience (who engaged + new followers): <top job titles, seniorities, industries, locations, company sizes from the post's "Top demographics" + the new-follower demographics from creator analytics>
Learnings: <1 to 2 lines: what this post's numbers + audience say worked or didn't, in plain language>
```

Tracking-entry format (TikTok):
```
<bold+underline POST NAME>
Posted: <YYYY-MM-DD>
Link: <plain-text video URL>
Metrics @24h: <views, likes, comments, shares, saves, new follows, avg watch time, % watched full, traffic source mix> (frozen 24h read)
Metrics latest: <same fields> (as of <date>)
Audience (who engaged + new follows): <gender split, top territories, follower-activity notes from TikTok analytics>
Learnings: <1 to 2 lines>
```

If a metric genuinely isn't exposed for that post, write `n/a` for it rather than dropping the field, so it's clear it was checked.

**Exact posted date (do NOT trust "Nd ago" relative text, it goes stale on a frozen tab):** decode it from the LinkedIn activity URN. `posted_ms = activity_id >> 22` gives Unix milliseconds; convert to your local date. Cross-check against memory if available.

Every run (including the scheduled run):
1. Open `https://www.linkedin.com/in/me/recent-activity/all/` in your session and extract your recent original posts (ignore reposts) with their activity URNs + posted dates.
2. For each live post, **open its full analytics** and capture the deep set:
   - **Discovery:** impressions, members reached (unique), and the impression-source split (feed / profile / search) when shown.
   - **Engagement:** reactions, comments, reposts, saves (when shown), and any "members who viewed your profile from this post" / page-visit attribution.
   - **Follows:** new followers gained (creator-mode posts surface this; otherwise read net new followers from the creator analytics for the period and attribute the spike to the post that drove it).
   - **Top demographics** of who engaged/was reached: job titles, seniorities, industries, locations, company sizes (LinkedIn's "Top demographics" panel). This is the audience signal that feeds LEARNINGS.
   - Where LinkedIn exposes per-post analytics: the post overflow menu → "View analytics", or `linkedin.com/analytics/post-summary/urn:li:activity:<id>/`. The creator/follower analytics (new followers + their demographics) is under `linkedin.com/dashboard/` / the Followers analytics page.
   - Capture the `@24h` snapshot once (freeze it) and refresh `latest` every run.
3. Remove the matching block from the PRIORITIZATION lists (it's no longer up-next), but KEEP the LIVE tracking entry. Archive the full analytics + demographics snapshot in `runs/<ts>/analytics/` as a backup (this is the audit trail the LEARNINGS synthesis is rebuilt from).
4. TikTok: from your profile `https://www.tiktok.com/@<your-handle>`, open each video's analytics (or the creator analytics in your session) and capture views, likes, comments, shares, saves, new follows, avg watch time, % watched full, traffic-source mix, and audience (gender split, top territories). Keep posted TikToks under the LIVE > TikTok subsection, newest first, with the same `@24h` + `latest` checkpoints. Extract via the rehydration JSON / `[data-e2e]` selectors in your logged-in session.
5. After refreshing all LIVE entries, REBUILD the LIVE LEARNINGS readout (below) from the current set, and apply it to drafts.

## LIVE LEARNINGS (the readout that opens the LIVE section, and the loop that feeds drafting)

At the very top of the LIVE section, keep a compact, always-current **LEARNINGS (updated YYYY-MM-DD)** readout, rebuilt every run that has new/changed metrics. It is the synthesis of every live post's numbers + demographics into a few actionable directives. Keep it short and scannable (no em/en dashes):

```
LEARNINGS (updated YYYY-MM-DD)
What's working: <2 to 4 bullets: post traits that correlate with high reach/engagement/saves, e.g. "first-line named-brand hooks outperform category openers", "personal-story posts pull 2x the saves of analysis posts">
Most-engaged audience: <the dominant job titles / seniorities / industries / locations across the best posts>
Newest followers: <who the recent new followers are, from follower analytics; this audience is weighted highest because growth is the goal>
Apply to drafts: <2 to 3 concrete directives derived from the above, e.g. "open to founders/operators, not enterprise marketers", "lead with the hands-on build, name the tool", "lean lifestyle-AI crossover, it converts new follows">
```

**The loop: study learnings from EVERY live post and apply them to EVERY new idea and draft, every time there are new metrics.** Concretely:
- Whenever LIVE metrics refresh and the synthesis SHIFTS, revisit the open drafts (EARLY DRAFTS + ITERATION) and realign them to the most-engaged / newest-follower audience: adjust the hook, the framing, the named anchors, and the platform routing to match who is actually engaging and following. Do NOT silently rewrite LOCKED/DRAFTED posts (those are locked); instead flag in the summary if a locked post now looks off-audience.
- Every brand-new idea's FIRST draft must already reflect the current LEARNINGS (it's written for the proven audience from the start, not generically).
- The "Apply to drafts" directives are the bridge: when you draft in the SKILL's Step 2/3, read this readout first and obey it the same way you obey the voice profile.

## Audience-fit weighting (the PRIORITIZATION tag)

Every prioritization line (both lists) ends with a plain-text audience-fit tag: `(strong audience fit)` / `(medium audience fit)` / `(weak audience fit)`. Audience fit = how well the idea matches your most-engaged audience and, weighted highest, your NEWEST followers (from LIVE LEARNINGS). It is a ranking input ALONGSIDE trend relevance and expected performance, not a replacement for them: a high-trend idea with weak audience fit can still rank, but audience fit breaks ties and pulls strong-fit ideas up. The unchanged half of the rule still holds: **workflow state never moves a rank** (never bump an idea because it's being worked on, was just drafted, or came up in chat), and LOCKED/DRAFTED/POSTED items leave the lists. If there is not yet enough LIVE data to judge fit for an idea, tag it `(medium audience fit)` and say so.

## Step 0 protocol (START of every invocation)

1. Read the whole note (AppleScript below). Back up the raw body to `runs/<timestamp>/note-backups/` first.
2. Track published posts: pull each live post's FULL analytics (deep metrics + demographics, `@24h` snapshot + `latest`), update the LIVE section, and remove the posts from the prioritization lists (see "Posted-post tracking + deep analytics" above). Then rebuild the LIVE LEARNINGS readout from the refreshed set.
3. Drain the INBOX: new idea → new block(s) under the right platform section(s), drafted with the current LEARNINGS already applied; written thoughts for an existing idea → file under that block's "Your thoughts", mark owed-a-REWORK. Reset inbox to `(empty)`.
4. Reprioritize BOTH lists independently, new ideas against old, using the freshest trend data AND audience fit. Rebuild the two lists; append the plain-text `(strong/medium/weak audience fit)` tag to every line. Rank on trend relevance + expected performance + audience fit (audience fit weighted toward newest followers). UNCHANGED rule: workflow state never moves rank (no bumping the idea you're currently working on); LOCKED/DRAFTED/POSTED items leave the lists; sequencing commitments are a parenthetical on the line, not a rank change.
5. Apply LEARNINGS to the open drafts: if the synthesis shifted this run, realign EARLY DRAFTS + ITERATION to the most-engaged / newest-follower audience (don't rewrite LOCKED/DRAFTED; flag them if off-audience).
6. Then do whatever was asked this run.

## Step N protocol (END of every invocation)

- Write back every change: new blocks, reworked drafts, new variants, status changes, stage re-ordering (blocks must sit under the right stage subheader), refreshed prioritization lists (with audience-fit tags), refreshed LIVE analytics + LEARNINGS, refreshed TRENDS if new scrape data exists.
- NO color anywhere: headers, subheaders, fit tags, titles, and body are all plain default black. Strip any `<font color>` tags found on read.
- Never leave the note messier than you found it; never re-add deleted scaffolding.

## The optional daily scheduled run

A scheduled task ("Daily content trends + note sync") can run every morning in a fresh session on your Mac. What it does:
1. Scrape ~200 posts total, ALL platforms scraped (never a web pulse): your LinkedIn feed + topic content searches (your session), your X home timeline (sync-XHR via your session), and TikTok via `tiktok.com/search?q=<topic>` reading `[data-e2e="search-card-desc"]` captions in your logged-in session, sweeping your tracked intersections. WebSearch only if a platform is genuinely logged out, and say so.
2. Rebuild the TRENDS section with the date.
3. Run the full Step 0 protocol (pull deep per-post analytics + rebuild LIVE LEARNINGS, drain inbox, reprioritize both lists with audience-fit tags, apply learnings to open drafts) and write back (Step N).
4. Draft EARLY DRAFTS for any new inbox ideas (with current LEARNINGS applied), and refresh variants for top-5 TikTok ideas ONLY if trends shifted materially. If LIVE LEARNINGS shifted this run, realign open EARLY DRAFTS + ITERATION to the newest-follower audience.
5. It does NOT touch the LinkedIn browser (no auto-publish, no auto-draft). It surfaces LOCKED-but-undrafted posts in its summary instead.

Constraints to surface honestly when they bite: the Mac must be awake at run time; Chrome must be running with the extension paired for the LinkedIn/X/TikTok scrapes; Apple Notes is local so a cloud run cannot do this job.

### Lock-to-draft policy
- In an interactive session, the moment you say a post is locked, save it as a native LinkedIn DRAFT (no date, no scheduler) WITHOUT asking again, via the browser flow in `references/linkedin-draft-via-browser.md`. Mark the block [DRAFTED]; it stays under LOCKED. The skill tells you the draft landed and where to find it (composer → drafts).
- No cadence, no slot, no clock by default. Schedule a specific post only if you explicitly ask for that one, as a flagged exception.
- Autonomous runs (the scheduled task) still never touch the browser; they surface LOCKED-but-undrafted posts in their summary.

## Mechanics (osascript via the Bash tool)

osascript can drive Notes on this Mac. If Notes is slow to launch, the first call may time out; wrap calls in `with timeout` and retry once.

**Read the note + back it up:**
```bash
osascript -e 'with timeout of 120 seconds
tell application "Notes"
set n to note id "<YOUR_NOTE_ID>"
return body of n
end tell
end timeout' > runs/<ts>/note-backups/content-ideas-raw-backup.txt
```

**Write the note (rebuild body):** generate the full HTML to a file, then set the body from that file so you never fight AppleScript string escaping.
- Build HTML in a small Python script: wrap each text line in `<div>...</div>`, blank lines as `<div><br></div>`, section headers in `<b>`, and ESCAPE `&` `<` `>` to `&amp;` `&lt;` `&gt;` in all text content.
- Keep the first line `<div><h1>Content Ideas</h1></div>` so the note name is preserved.
```bash
osascript <<'APPLESCRIPT'
with timeout of 120 seconds
  set theHTML to (read POSIX file "/tmp/content_note.html" as «class utf8»)
  tell application "Notes"
    set body of note id "<YOUR_NOTE_ID>" to theHTML
  end tell
end timeout
APPLESCRIPT
```
Notes re-renders the HTML into its own markup. Re-read to verify length and title. Unicode (emoji, →, ═) survives via the `«class utf8»` read.

For mechanics, use the surgical-edit approach above (`references/note-surgical-edit-template.py`): it has the escaping, anchor assertions, and dash check. The live note itself is the source of truth for formatting; copy its existing lines rather than regenerating them.

## Scraping playbook (what actually works)

- Chrome may freeze the MCP tab in the background (timers suspended, async JS never resolves, lazy-load dead). Workarounds that work on a frozen tab: synchronous JS via javascript_tool; **sync XMLHttpRequest** for API calls; repeated page loads to sample server-rendered content.
- **LinkedIn feed**: server-renders ~3 posts per load; reload-sample and dedupe. Content searches (`/search/results/content/?keywords=...`) server-render ~3-5 posts per query; sweep many queries. The activity page (`/in/me/recent-activity/all/`) renders post list after a few seconds; split on "Feed post number".
- **X home timeline**: extract `queryId` for HomeTimeline + Bearer token from the main.js bundle (sync XHR), read `ct0` cookie, POST `/i/api/graphql/<qid>/HomeTimeline` with sync XHR; on a features error, parse the missing feature names from the error and retry with them set false. Walk the JSON for `legacy.full_text`.
- **TikTok (SCRAPE, not a pulse, when logged in).** When your Chrome session is logged into TikTok: navigate to `https://www.tiktok.com/search?q=<topic>` and read caption text from the DOM via `javascript_tool` innerText: `document.querySelectorAll('[data-e2e="search-card-desc"]')` returns ~20 to 38 caption strings per query (each followed by the creator handle + a date). Sweep your tracked intersections with several queries each. The For You feed uses `[data-e2e="video-desc"]` (too random for niche signal, use search). Your handle + login state live in `#__UNIVERSAL_DATA_FOR_REHYDRATION__` (walk the JSON for `uniqueId`). WebSearch is a fallback ONLY if logged out; if you fall back, say so. Do NOT default TikTok to a web pulse.
- Accumulate scraped text in `localStorage` (survives navigations) and read it out in chunks; tool results truncate around ~1300 chars.

## Guardrails
- Back up before every overwrite. Your written thoughts are irreplaceable.
- Target by note ID, never clobber a different note.
- Preserve your writing verbatim in "Your thoughts." Reword only in Draft/Variants.
- Respect your deletions: never re-add scaffolding or sections you removed.
- Never auto-publish. On lock, save a LinkedIn DRAFT only (no schedule); you publish from your drafts yourself. The scheduled task never drafts or publishes on its own.
- **Never downgrade the TRENDS date.** Any time you rewrite the note for ANY reason (a formatting pass, a single edit, adding one block), do NOT carry a stale, hardcoded `TRENDS (updated YYYY-MM-DD)` from an old builder. Read the date currently live in the note first; either refresh TRENDS with a new scrape and today's date, or preserve the existing live section verbatim.
