---
name: idea-to-linkedin-tiktok
description: >-
  Turns your raw content ideas into ready-to-post content for LinkedIn AND TikTok, each
  built around a popular insight at its core. For every idea it produces a strongest post
  per platform: one anchored on a live/trending insight (researched from the web + X) and
  one on an evergreen insight (reasoned from knowledge), often merged into a single best
  post. Each idea ships as a voice-matched LinkedIn post and a full TikTok production
  script (hook, beat-by-beat voiceover, on-screen text, b-roll, caption, hashtags, sound).
  After you review and pick a variant per idea, the chosen LinkedIn posts are saved as
  DRAFTS in your LinkedIn (native composer drafts via the browser, NO scheduling) for you
  to publish whenever you want. Your master content doc is an Apple Note: every run this
  skill READS new ideas and written thoughts from it, reprioritizes all ideas (new against
  old) with SEPARATE LinkedIn and TikTok rankings weighted by audience fit, tracks your
  published posts in a LIVE analytics section (clicking into each post for deep metrics:
  reach, saves, new followers, profile visits, and audience demographics), synthesizes
  those into LEARNINGS it applies to every new draft, refreshes a daily TRENDS section
  (an optional scheduled run scrapes ~200 posts across LinkedIn + X + TikTok), gives every
  TikTok idea 3 to 5 variants, and WRITES the organized, stage-sorted drafts back, split by
  LinkedIn vs TikTok.
  Handles a single idea or a whole batch. Use this whenever you want to develop, flesh out,
  or "bake out" content ideas into posts, turn a list of ideas into LinkedIn + TikTok
  content, draft posts with a viral or trending hook, build a content batch, save a batch
  of LinkedIn posts as drafts, sync or reorganize your content note, reprioritize your
  content, or brainstorm-to-draft in your voice. Trigger phrases: "turn my ideas into
  posts", "bake out these content ideas", "make LinkedIn and TikTok content from this idea",
  "draft posts for these ideas", "I have content ideas", "draft these posts in LinkedIn",
  "flesh out this idea into content", "make me a LinkedIn post and TikTok script", "sync my
  content note", "reprioritize my content ideas", "what should I post next".
---

# Idea to LinkedIn + TikTok

You have lots of raw content ideas. This skill develops each one into cohesive, ready-to-post content: a LinkedIn post and a TikTok script, each anchored on a popular insight so the post earns attention instead of getting scrolled past.

The whole reason this skill exists: a raw idea ("AI is changing search") is not a post. It needs a sharp insight at its core, your voice on top, and the right shape for each platform. If a draft reads like a generic LinkedIn thought-leader or a paragraph someone pasted into TikTok, the skill failed.

## First-time setup (do this once)

This skill is built to sound like *you*, work from *your* content note, and post to *your* accounts. Before the first real run, walk through `references/setup.md` once to personalize three things:

1. **Build your voice profile.** Connect your LinkedIn (browser) so the skill can read your recent original posts and generate `references/voice-profile.md` from how you actually write. This is what makes drafts sound like you instead of like "a LinkedIn thought leader." See `references/voice-profile-bootstrap.md`.
2. **Point it at your content note.** Set your Apple Note ID in `references/apple-notes-sync.md` (the skill can help you find it). This note becomes the source of truth.
3. **Confirm your handles.** Your LinkedIn profile and (optionally) your TikTok handle, used for scraping trends and tracking your published posts.

If `references/voice-profile.md` still contains template placeholders, run the bootstrap first; drafting in a generic voice is the most common failure.

## What it produces per idea

For each idea you have two angles available, because the same idea lands differently depending on whether you hook it to the news cycle or to a durable truth:

- **Live trend.** Research what is currently popular, trending, or being debated about the topic (web + X). Anchor on that real, timely insight so it rides existing momentum.
- **Evergreen.** Anchor on a proven, durable insight about the topic that would resonate in any month. No research dependency.

**Default to ONE strongest post per idea, often blending these two angles, over two separate variants.** A great post often opens with the live framing ("everyone talks about AI making them more productive") and then delivers the evergreen story. So produce the single best post per idea, merging the timely peg and the durable truth when that makes it stronger. Use the live-trend research to make it current and the evergreen reasoning to make it resonant. Only produce two separate variants if you ask to see options or the two angles are genuinely too different to merge. When you produce one merged post, still keep the timely peg real and the story grounded.

What ships per idea:
1. **LinkedIn:** ONE strongest voice-matched post (merged live + evergreen angle), landed in the note and ultimately as a LinkedIn draft (no scheduling).
2. **TikTok:** **3 to 5 full variants** (each a complete hook + script + caption + tags unit, different angles), saved in the note for you to pick or mix per shoot.

Platform routing happens in Step 1.5 below; a "both" idea gets the LinkedIn post AND the TikTok variant set.

## The source of truth: your "Content Ideas" Apple Note

You keep ONE Apple Note as the master content doc, and this skill maintains it. Read [references/apple-notes-sync.md](references/apple-notes-sync.md) every run; it has the note ID, structure, and the exact osascript read/write mechanics. The contract:

- **The note is the system of record, not the chat.** Every invocation READS from it first (Step 0) and WRITES back at the end (Step N). The `runs/` files are a backup/working copy; if they ever disagree, the note wins.
- **The note's order:** INBOX → PRIORITIZATION (two independent ranked lists, LinkedIn and TikTok, each line = the idea source + a plain-text `(strong/medium/weak audience fit)` tag) → TRENDS (refreshed daily) → **LIVE** (its own top section: a LEARNINGS readout, then `LinkedIn` and `TikTok` subsections of published posts with deep analytics, newest first) → LINKEDIN section → TIKTOK section.
- **Plain default text, no color.** Keep the whole note plain default black: headers, stage subheaders, LIVE subsections, audience-fit tags, titles, body. Don't wrap anything in `<font color>` / `<span style="color">`; strip any color tags found on read. Bold, underline, `<h2>`, and existing header font-sizes still carry. Don't change the `═` bar lengths once you've set them.
- **Inside each platform DRAFT section, blocks are organized by stage with bold H2 subheaders (no emoji), in this order:** LOCKED → ITERATION → EARLY DRAFTS. (LOCKED = locked/drafted posts NOT yet live. Published posts live in the top-level LIVE section, not here.) **The block title IS the source idea** (your shorthand, bold+underline); there is NO separate "Idea (source)" line. Then optional `Your thoughts` (verbatim), then `Draft` (LinkedIn) or the variant set (TikTok). A "both" idea lives as two blocks.
- **Every idea gets a draft.** Don't leave bare ideas; draft each one on arrival (LinkedIn merged post; TikTok 3 to 5 variants) so a new idea lands directly under EARLY DRAFTS.
- **TikTok blocks carry 3 to 5 variants per idea in Draft / Caption / Format shape** (hook folded into the Draft, hashtags into the Caption, visual + sound into the Format).
- **Posted means TRACKED in the top-level LIVE section with DEEP analytics** (its own section after TRENDS, with `LinkedIn` + `TikTok` subsections). When a post goes live, put it under LIVE > its platform as a tracking entry: bold+underline post name, `Posted:` date, `Link:` URL, then **click INTO the post's full analytics** and capture the deep set: impressions, members reached, reactions, comments, reposts, saves, NEW FOLLOWERS, profile/page visits, plus the **Top demographics** of who engaged + the new-follower demographics (TikTok: views, likes, comments, shares, saves, follows, avg watch time, % watched, traffic source, audience territories). Capture a frozen **`@24h` snapshot** the first run a post is >24h old, then a rolling **`latest`** line every run after. Sort entries NEWEST FIRST. Drop the post from the prioritization lists (it is done) but keep refreshing its analytics every run. Archive each run's full analytics + demographics in `runs/<ts>/analytics/`. **Get the EXACT posted date by decoding the LinkedIn activity URN, never the unreliable "Nd ago" relative text: posted_ms = activity_id >> 22, then format the date in your timezone.** LOCKED (in the draft section) is reserved for locked/drafted posts not yet live. See the deep-analytics + LEARNINGS sections in the sync reference.
- **LIVE LEARNINGS loop:** the LIVE section opens with a `LEARNINGS (updated <date>)` readout synthesized from every live post's numbers + demographics (what's working, the most-engaged audience, the NEWEST followers, and concrete "apply to drafts" directives). Study it and apply it to EVERY new idea and draft, every time metrics change: every new idea's first draft is written for your proven + newest-follower audience, and when the synthesis shifts you realign the open EARLY DRAFTS/ITERATION (never silently rewrite LOCKED/DRAFTED; flag those if off-audience). Treat the "apply to drafts" directives like the voice profile: obey them when drafting in Steps 2 to 3.
- **Audience fit is a prioritization weight:** every prioritization line ends with a plain-text `(strong/medium/weak audience fit)` tag. Audience fit (match to your most-engaged + NEWEST-follower audience, from LEARNINGS) ranks alongside trend relevance and expected performance; it breaks ties and pulls strong-fit ideas up. The unchanged half of the rule still holds: workflow state never moves a rank, and LOCKED/DRAFTED/POSTED leave the lists.
- **Notes link/attachment limits:** osascript `set body` strips all `<a href>` (file:// and https://), so URLs land as plain text; file attachments can't be added programmatically and a rebuild wipes hand-added ones, so keep any companion PDFs/files in a separate note + on disk, not inside Content Ideas.
- **You only have to touch the INBOX.** You paste raw ideas or written thoughts there; the skill drains it into the right blocks each run. Never re-add scaffolding you deleted.

### The 5-stage process (honor it, this is how the system works)

1. **IDEA**: you write shorthand (in the note's inbox or chat).
2. **EARLY DRAFT**: the skill prioritizes it and writes a first draft.
3. **YOUR THOUGHTS**: you write out everything you think.
4. **REWORKED**: the skill uses your thoughts to write a genuinely stronger draft (pull your specific arguments, numbers, examples, and phrasings in; don't just lightly edit).
5. **LOCKED**: you iterate together in chat until you lock it.

Then **DRAFTED** (saved as a LinkedIn draft, no schedule) → **POSTED**. Status tags in the note: `[IDEA] [EARLY DRAFT] [REWORKED] [LOCKED] [DRAFTED] [POSTED]`. If a block has "Your thoughts" filled but the draft hasn't absorbed them, it is owed a REWORK; surfacing those is a good first move each run.

## Before you start: load the voice

Read [references/voice-profile.md](references/voice-profile.md) first, every run. It is the difference between "sounds like you" and "sounds like LinkedIn." If it still has template placeholders, run the voice-profile bootstrap (`references/voice-profile-bootstrap.md`) first. The non-negotiables that live there and override everything else:

- **No em dashes or en dashes, ever.** Use periods, colons, commas, or parentheses.
- **Sentence case.** Never all-lowercase, never Title Case sentences.
- **No hashtags on LinkedIn.** (Hashtags ARE used on TikTok captions, where they're native.)
- **First line earns the scroll-stop**: lead with a recognizable brand/person/number or a sharp opinion, not a generic category noun.

## Workflow

### Step 0: Sync the Content Ideas note (run this FIRST, every time)

Before anything else, sync with your "Content Ideas" Apple Note per [references/apple-notes-sync.md](references/apple-notes-sync.md). This is what makes new ideas and your written thoughts get pulled in "automatically" and what keeps the note the source of truth.

1. **Read + back up** the note (osascript). Save the raw body to `runs/<timestamp>/note-backups/` before any write.
2. **Do the FULL scrape (every resync, not just a scheduled run). Every resync is an entire scrape, never a web "pulse."** Scrape ~200 posts total in your logged-in Chrome session per [references/apple-notes-sync.md](references/apple-notes-sync.md) (the frozen-tab workarounds: sync-XHR, reload-sampling, JS innerText reads): (a) your LinkedIn feed via reload-sampling PLUS ~12 topic content searches (`/search/results/content/?keywords=...`) covering the themes your idea list suggests; (b) your X home timeline (sync-XHR HomeTimeline, or article-innerText reads with scroll-sampling); (c) TikTok scraped in your logged-in session: `tiktok.com/search?q=<topic>`, read `[data-e2e="search-card-desc"]` caption text via `javascript_tool` (~20 to 38 per query), sweeping the niche intersections you care about. A `WebSearch` pulse is a LAST-RESORT FALLBACK only for a platform that is genuinely logged out or blocked, NEVER the default for any platform including TikTok, and you must say in the summary which platforms were really scraped vs fell back to web. If Chrome is not paired, say so and ask the user to pair it; do not silently downgrade the whole run to a web pulse.
3. **Rebuild the TRENDS section** from that scrape, dated today (real `date`, never inferred). LinkedIn + X trends (call out what shifted), TikTok trends with the tracked intersections, format notes. Scannable, no em/en dashes.
4. **Track published posts with DEEP analytics.** Check your LinkedIn recent-activity page (and your TikTok profile); for each post that has gone live, **click into its full analytics** and capture the deep set (impressions, reach, reactions, comments, reposts, saves, new followers, profile/page visits, and the Top demographics of who engaged + new-follower demographics; TikTok: views/likes/comments/shares/saves/follows/watch-time/traffic-source/territories). File it under the top-level **LIVE** section's `LinkedIn` or `TikTok` subsection as a tracking entry with a frozen `@24h` snapshot + a rolling `latest` line, sorted NEWEST FIRST, dropped from both prioritization lists. Use the URN-decoded exact posted date (`activity_id >> 22` ms), not "Nd ago". Archive the full analytics + demographics in `runs/<ts>/analytics/`. See the deep-analytics section in the sync reference for the exact fields, the per-post analytics URLs, and the 24h-checkpoint rule.
5. **Rebuild LIVE LEARNINGS.** From the refreshed analytics, rebuild the `LEARNINGS (updated <date>)` readout at the top of the LIVE section: what's working, the most-engaged audience, the NEWEST followers (weighted highest), and 2 to 3 concrete "apply to drafts" directives. If the synthesis shifted from last run, realign the open EARLY DRAFTS + ITERATION drafts to that audience (don't rewrite LOCKED/DRAFTED; flag them if now off-audience).
6. **Drain the INBOX.** For each item: a brand-new idea becomes a new block drafted straight into EARLY DRAFTS **with the current LEARNINGS applied** (route it in Step 1.5); written thoughts for an existing idea get filed under that block's "Your thoughts" and mark it owed-a-REWORK. Clear the inbox to "(empty)".
7. **Reprioritize both platform lists independently,** new ideas against old, using THIS run's fresh scrape. LinkedIn ranks on LinkedIn signals; TikTok ranks on TikTok signals, including your tracked intersections. This is the standing "constantly prioritize my new ideas against old ones" promise, so do it even if you only asked to draft one thing. **Rank on trend relevance, expected performance, AND audience fit.** Append a plain-text `(strong/medium/weak audience fit)` tag to every line; audience fit (match to your most-engaged + newest-follower audience, from LEARNINGS) breaks ties and pulls strong-fit ideas up. Workflow state must never move a rank: never bump an idea because it's being actively worked on, was recently drafted, or came up in chat. LOCKED/DRAFTED items leave the lists once posted. A sequencing commitment is recorded as a short parenthetical on that idea's line, never by inflating its rank.
8. Then proceed with whatever was asked this run.

**The optional daily scheduled run** ("Daily content trends + note sync") executes this exact protocol autonomously every morning, including the full scrape in step 2. It never touches the LinkedIn browser on its own (no autonomous publishing or drafting); it surfaces LOCKED-but-undrafted posts in its summary. Requirements it should flag when unmet: Mac awake, Chrome running with the extension paired. The full scrape is the standard for ALL runs, scheduled and manual alike; a web pulse alone is never an acceptable substitute for a resync.

If the skill was invoked just to "sync / reorganize / reprioritize my note," Step 0 IS the deliverable: do it, write back (Step N), and report the refreshed priority lists. A cloud/scheduled run can't reach local Notes, so this only happens during an on-machine run; say so if Notes is unreachable rather than silently skipping.

### Step 1: Collect the ideas

Ideas come from the note's INBOX and existing blocks (Step 0) and/or from chat. Detect whether the input is a single idea or a batch:
- **Single idea**: a sentence or two in chat, or one inbox line. Develop just that one (but still reprioritize the whole note in Step 0).
- **Batch**: a numbered/bulleted list, a pasted note dump, the note inbox, or a file (`.md`, `.txt`, `.csv`). Parse it into a clean list of discrete ideas. If items are ambiguous or two ideas are mashed together, split them and briefly confirm the parsed list before generating (cheap to confirm, expensive to regenerate 40 deliverables on a misread).

If an idea is just a topic with no angle ("AI search"), that's fine, the insight-finding in Step 2 is exactly the job. Don't push back asking for more detail; develop it. If a block already has "Your thoughts" filled in, jump it straight to a REWORK (Stage 4) using those thoughts rather than starting a blind early draft.

### Step 1.5: Route each idea to platform(s)

Not every idea belongs on both platforms. Decide per idea. The two platforms reward different things: LinkedIn rewards professional credibility and thesis-driven thinking, TikTok rewards personality, relatability, and lifestyle. Route by the topic's center of gravity:

- **LinkedIn only** = professional, heavier, thesis-driven topics. Industry analysis, frameworks, career takes, cultural/economic theses. The kind of thing that builds professional authority but would feel out of place between a get-ready-with-me and a recipe on TikTok.
- **Both** = a professional topic that also has a genuine lighter, personal, or lifestyle angle. If you can tell it as a credible take AND as a "let me show you my life" story, it earns both. This is the sweet spot for AI-meets-real-life content.
- **TikTok only** = purely lifestyle, personal, or comedic. A joke, a relatable bit, a "girl math" riff, a day-in-the-life. Real but light. It would dilute a LinkedIn feed but thrives on TikTok.

Make the call, then state it with a one-line reason so the user can override. When unsure between "LinkedIn only" and "both," ask whether the idea has a real personal/lifestyle story in it: if yes, lean "both"; if it is purely analysis, lean "LinkedIn only." When unsure between "both" and "TikTok only," ask whether a professional would learn something or respect them more for it: if yes, "both"; if it is just a laugh, "TikTok only."

Generate only the deliverables for the assigned platform(s): LinkedIn-only ideas get the LinkedIn post and no TikTok script; TikTok-only ideas get the TikTok variants and no LinkedIn post; "both" ideas get the full set. Present the routing table for the whole batch up front and let the user adjust before you generate everything.

### Step 2: Find the core insight for each variant

**First, load the LIVE LEARNINGS** (the readout at the top of the LIVE section, rebuilt in Step 0). Treat its "apply to drafts" directives as binding the same way the voice profile is: aim the insight and the framing at the most-engaged and NEWEST-follower audience, and lean into the post traits that the live numbers show are working (the hook style, the story-vs-analysis mix, the named anchors that pull saves and follows). A post that ignores who is actually engaging and following is a miss even if the insight is sharp.

The insight is what makes a post worth reading. A good insight is a specific, slightly contrarian or non-obvious claim, not a platitude. "AI is important" is not an insight. "Your customers now ask ChatGPT before Google, so your SEO budget is defending a door no one uses" is an insight.

**Variant A (live trend), research it:**
- `WebSearch` the topic for what's current: recent launches, debates, data points, news pegs. Pull 1 to 3 concrete, timely hooks.
- Use the grok tools for the X/social pulse: `mcp__grok__search_posts` (what people are actually saying/arguing) and `mcp__grok__get_trends` if a topic is broad. This surfaces the popular framing and the contrarian counter-take, both useful. If grok returns a credits/auth error, don't stall: WebSearch is the primary live-trend source and is enough on its own. Just note that the X pulse was skipped.
- Land on ONE timely insight. Note the source/peg so the post can reference it concretely (a named company, a number, a recent moment).

**Variant B (evergreen), reason it:**
- From your own knowledge of the topic, pick a durable insight that doesn't depend on this week's news. Often this is a first-principles truth, a counterintuitive lesson, or a reframe. The "translate the jargon into everyday value" move is a reliable evergreen engine: take the topic's buzzword and make a normal person feel why it matters.

Keep the two insights genuinely different. If Variant A and Variant B end up making the same point, push Variant B to a different angle (a contrarian take, a personal-story frame, a "here's what everyone misses").

### Step 3: Write the LinkedIn post for each variant

Follow the voice profile. A structure that consistently works:
- **Line 1**: the scroll-stopper. A named anchor (brand/person/number) or a sharp opinion. For Variant A, this is often the timely peg. Pick the anchor that lands with the audience the LEARNINGS show is engaging and following (e.g. founders/operators vs enterprise marketers): name the brand/person THAT audience would recognize, since line 1 is what decides the scroll-stop for a new follower.
- **Body**: the insight, made concrete. Translate any jargon. Use a skim-friendly structure (a short numbered list, • bullets, or 📍/👉 markers) when it fits, but don't force structure onto a post that wants to be a flowing 3-sentence take.
- **Body**: lead with ONE story told all the way through (setup, what was done, the specific result, the turn), then layer the other examples more briefly. Use a staccato fragment list for rhythm where it fits. Use the humility reframe (credit the friction removal, not the talent). Ground every flex with real specifics and numbers, never embellish.
- **Closer**: end warm and reflective, on a feeling or a forward-looking thought, not on a reflexive engagement question. Save explicit CTAs + links (with UTMs `?utm_source=content&utm_medium=linkedin&utm_campaign=<idea-slug>`) for genuinely promotional posts. Tag any named brand/person as an @mention (resolved in the LinkedIn UI per the draft reference).
- **Length**: not a constraint. Quality and storytelling win. A longer post is good when the story earns it; do not trim a strong story to be short, and do not pad a thin one. See the "Structure and storytelling" section in the voice profile.

### Step 4: Write the TikTok variants (3 to 5 per idea)

Read [references/tiktok-script-format.md](references/tiktok-script-format.md) and follow it. **Every TikTok idea gets 3 to 5 full variants, not one script with alternate hooks.** Each variant is a complete shootable unit (hook + script + caption + tags) taking a genuinely different angle: receipts/screen-record, mock-the-cliché, PSA, POV/skit, list-tease, girl-math, contrarian. Mark one as recommended. Share one Visual + Sound line per idea. This matches how TikTok actually works now (creative fatigues in ~72 hours, so variants are the system) and lets the user pick or mix per shoot. Two things dominate:

1. **Keep it SHORT.** Target 15 to 30 seconds, roughly 40 to 70 words. A tight spoken script with a punchy hook and a rapid list of real examples, NOT a 45-second five-beat shot list. Short clips get watched to completion and shared most. If a draft runs long, cut it.
2. **Talk like a friend, not an announcer.** Open mid-conversation, real reactions, "you," contractions. Playful personal slang is great; avoid generic creator clichés ("main character," "superior," "it's giving"). A strong hook formula: mock the cliché with repetition, then pivot ("AI productivity this. AI productivity that. Nobody's talking about...").

Deliver a hook, the tight spoken script, an optional light visual cue or two, a short playful caption (can tag the tools used), 3 to 5 hashtags, and a sound recommendation. For sound, recommend a CURRENT trending audio (don't name a specific track, it'll be stale) layered under the voice, and describe the vibe. The reference file has the details, including TikTok posting times (Tue-Thu ~11am-1pm ET) for when the user chooses to post.

### Step 4.5: Final dash sweep (required, do not skip)

Before saving or landing anything, scan the ENTIRE output, including section headers and labels, for em dashes and en dashes (the characters `—` and `–`) and replace every one with a period, colon, comma, or parentheses. This is the easiest rule to state and the easiest to leak on a long generation: em dashes can creep into the file's own section headers (`## Variant A — LinkedIn post`). Use a colon instead (`## Variant A: LinkedIn post`). A single leaked dash anywhere is a failure of the skill's hardest rule, so treat this sweep as mandatory, not optional. If you can run a quick grep for `[—–]` over the text you're about to write, do it.

### Step 5: Save everything (note + files), then review in chat

1. **Write back to the note (Step N).** This is the primary save. Update every changed block (new ideas, reworked drafts, status changes), refresh the PRIORITY QUEUE, keep it split by LinkedIn vs TikTok, and leave it at least as organized as you found it. Back up before overwriting and target by note ID per the sync reference.
2. **Also write `runs/<timestamp>-<batch-slug>/`** as a backup copy, one markdown file per idea (`idea-01-<slug>.md`) with all deliverables clearly labeled. Use colons in labels, never dashes. This is the offline copy of record for the TikTok scripts (TikTok has no draft API). If the note and files disagree, the note wins.
3. **Show the work in chat first.** Don't touch the browser until the user has reviewed. For a batch, show the first idea's full set as a sample and summarize the rest, then ask if the voice/insight is landing before generating everything. Burning a big batch on a wrong voice read is the expensive mistake.
4. **Per idea, the user picks which variant to publish.** Present the draft(s) for an idea and let them choose. As they react, you iterate in chat (Stage 4 → 5); when they say a post is locked, set that block to `[LOCKED]` in the note. The unpicked/held-back variant stays in the note as a backup block. TikTok scripts stay in the note + files to shoot; they are not drafted into any tool.

### Step 6: Save the approved LinkedIn posts as drafts (NO scheduling)

**Lock-to-draft policy:** the skill does NOT schedule posts. The moment the user locks a post in an interactive session, save it as a native LinkedIn DRAFT (no date, no scheduler) without asking again, so it sits in their LinkedIn drafts ready to publish whenever they want. Do not pick a slot, do not open the scheduler clock, do not set any publish time. Autonomous runs (the scheduled task) still never touch the browser on their own; they surface locked-but-undrafted posts in their summary.

Follow [references/linkedin-draft-via-browser.md](references/linkedin-draft-via-browser.md) for the exact browser flow (Start a post → type body → resolve @mentions → close → Save as draft → verify "Draft saved" toast). The optional [references/linkedin-scheduling-via-browser.md](references/linkedin-scheduling-via-browser.md) covers the clock/scheduler flow only if the user explicitly asks to schedule a specific post. Key points:

- **A single locked post is drafted immediately** under the lock-to-draft policy. For a **multi-post batch**, save each approved post as its own draft in approval order; label each draft's first line clearly so the user can tell them apart in their drafts list. Report which drafts landed; don't block on a confirmation.
- **No scheduling, no slot table, no cadence by default.** If the user explicitly asks to schedule a specific post for a specific time, do that one as a one-off and say it's an exception to the draft-only default.
- **Update the note as you go:** when a post's draft is saved, mark the block internally `[DRAFTED]` (it stays under the LOCKED stage subheader, since it's locked + drafted but not yet live); if the user confirms one published, it moves to the LIVE section. The note should always show what's locked/drafted vs what's already live.
- **Visibility** is whatever the composer defaults to for a draft; the user sets visibility (Anyone) at publish time themselves. Don't change account settings.
- Drafts carry text only; the user attaches any hero image themselves before publishing (tell them the suggested visual in the hand-off).
- If a draft won't save (composer error, @mention won't resolve), flag it and leave the copy in the note + `runs/` so nothing is lost.

### Step 7: Hand off

Tell the user:
- The drafts that landed in LinkedIn: how many, and how to find them (composer → drafts), with the first-line label that maps each draft to its idea/variant.
- Which variant was chosen per idea, and where the held-back variants live.
- Where the TikTok scripts are saved (the `runs/` path).
- The suggested visual/hero for each drafted post (they attach it before publishing).
- Anything they need to finish manually (@mentions that didn't resolve, the URL preview card to eyeball, visibility to set at publish).

## Scaling to batches

For a big batch, the work is repetitive across ideas, so be systematic: parse all ideas first (Step 1), confirm the list, then run Steps 2 to 4 per idea. Consider doing the research and drafting for all ideas before opening the browser, so the browser session lands all drafts in one pass. Always show a sample and get a voice check before committing to the full set of browser drafts.

## Failure modes to avoid

- **Generic insight.** If the "insight" is something everyone already agrees with, it's not done. Push for the specific, slightly contrarian version.
- **Voice drift.** Re-read the voice profile if drafts start sounding corporate. The tells: no personal stake, no jargon-to-value translation, hashtags on LinkedIn, em dashes. If the voice profile is still template placeholders, you skipped the bootstrap.
- **TikTok as a paragraph.** The TikTok deliverable must be a shootable table, not prose.
- **Identical variants.** A and B must make genuinely different points, not the same point with different words.
- **Silent browser fallback.** If Chrome isn't paired, say so and ask the user to pair it. Don't quietly dump a paste file and call it done.
- **Skipping the note sync.** The note is the source of truth. Forgetting Step 0 (pull + reprioritize) or Step N (write back) breaks the whole system: the inbox piles up, statuses go stale, and the chat and note drift. Never skip them, and never overwrite the note without backing it up first.
- **Clobbering the user's writing.** Preserve "Your thoughts" verbatim; reword only in the Draft field. Target the note by ID so you never overwrite an unrelated note.
