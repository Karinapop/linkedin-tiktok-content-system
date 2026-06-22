# Voice Profile Bootstrap: build the user's voice from their real LinkedIn posts

The skill is only as good as `references/voice-profile.md`. This file is how that profile gets built the first time (and refreshed later) from the user's actual writing, so drafts sound like them instead of like a generic LinkedIn thought leader.

Run this when:
- `references/voice-profile.md` still contains `<...>` template placeholders (first-time setup), OR
- the user says "build my voice profile," "refresh my voice from my latest posts," or "you don't sound like me yet."

## What you produce

A fully filled-in `references/voice-profile.md` for this user: their core throughline, 4 to 6 signature moves WITH real example lines quoted from their posts, their tone dials, the hard rules (kept as-is by default), and 3 to 6 of their real posts as reference samples. No placeholders left behind.

## Preferred method: read their posts in the browser

1. **Pair Chrome.** `mcp__Claude_in_Chrome__list_connected_browsers` should return a browser. If empty, call `switch_browser` and ask the user to click Connect in Chrome (60 to 120s). The user must already be logged into linkedin.com.
2. **Open their activity feed.** Navigate to `https://www.linkedin.com/in/me/recent-activity/all/`. This lists their own posts and reposts, newest first.
3. **Collect ~12 to 20 of their ORIGINAL posts.** Ignore reposts and pure link-shares with no commentary. The feed server-renders the post list after a few seconds; split on "Feed post number" and read each post's text. If the tab freezes in the background, use the frozen-tab workarounds (synchronous `javascript_tool` innerText reads, reload-sampling) described in `references/apple-notes-sync.md`. Accumulate the post text in `localStorage` and read it out in chunks if results truncate.
4. **Prefer range over recency.** Grab a spread of post types if you can see them: an announcement, a lessons-learned reflection, an opinion/hot-take, an analysis post, an event recap. Range teaches the skill the user's full register, not just one mode.

If Chrome cannot be paired, fall back: ask the user to paste 8 to 12 of their own posts into chat. That is enough to build a solid profile.

## Turning posts into the profile

Read the collected posts and infer, with evidence:

- **Core throughline.** What one or two impulses run through almost everything? (e.g. "proud to be building the future" + "make the complicated thing make sense.") State it in one or two sentences.
- **Signature moves.** Identify the 4 to 6 recurring, identifiable habits. For each, write what it is in one line AND quote 1 to 3 REAL lines from their posts that show it. Common ones to look for: how they open (revelation, scene, hot take, named anchor), whether they translate jargon into plain value, whether they tie work to a bigger mission, how they structure for skim (numbered lessons, bullets, emoji markers), how warm/specific they are (tagging people, concrete dates and numbers), and how they close (warm reflection vs engagement-bait question).
- **Tone dials.** Energy level, confidence (do they post "hot takes"?), emoji habits (count and whether decorative or markers), occasional emphasis caps, sentence-length rhythm.
- **Reference posts.** Pick 3 to 6 of their strongest/most representative posts and paste them verbatim under labeled headers.

## Hard rules: keep them, but check fit

The hard rules in `voice-profile.md` (no em dashes, sentence case, no LinkedIn hashtags, scroll-stop first line, no embellishment, casual over polished) are this skill's defaults and generally make posts better. Keep them by default even if the user's own past posts break them (many people's natural drafts use em dashes; the skill's job is to clean that up). Only relax a rule if the user explicitly asks (e.g. "I do want hashtags on LinkedIn").

## Write it back and confirm

1. Write the filled-in profile to `references/voice-profile.md` (overwrite the template).
2. Sweep the file for em dashes and en dashes (`—` `–`) and remove any, including in quoted reference posts' surrounding text. Leave the user's quoted posts verbatim inside the blockquotes.
3. Show the user a short summary: the core throughline you found, the signature moves, and 2 to 3 example lines you keyed on. Ask if it sounds like them. Adjust from their feedback. This is cheap to confirm and expensive to get wrong, since every future draft keys off this file.

## Refreshing later

The user's voice evolves (new job, new focus). When they ask to refresh, re-read their most recent ~15 posts and update the moves, tone dials, and reference samples. Keep anything still true; replace what has drifted. Note in the summary what changed.
