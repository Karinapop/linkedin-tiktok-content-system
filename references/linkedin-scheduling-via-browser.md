# Scheduling approved LinkedIn posts (native scheduler, via browser): OPTIONAL

> **Off by default.** This skill saves locked posts as plain LinkedIn DRAFTS with no schedule (see `references/linkedin-draft-via-browser.md` and SKILL.md Step 6). Do NOT use this scheduler/clock flow by default. Keep this file only for the case where the user explicitly asks to schedule one specific post at a specific time as a one-off.

LinkedIn's personal-profile composer has a **native scheduler** (a clock icon next to the Post button), so approved posts can be queued at set times with no third-party tool. Posts publish from the user's own profile.

Scheduling auto-publishes content on a timer, which is a public-posting action. Only schedule a post the user has explicitly asked to schedule, and always report the exact date/time after queueing. Never schedule silently.

## Cadence (only if the user wants a recurring schedule)

If the user defines a cadence (e.g. Tue/Wed/Thu at 8:30 AM ET, one post per slot), assign approved posts to the next available slots in approval order. Otherwise treat each scheduling request as a one-off at the time the user names.

## Slot assignment

Build the schedule before touching the browser:
1. Find the next target day/time that is at least ~2 hours in the future (LinkedIn requires a minimum ~1 hour lead; give buffer).
2. Assign approved post #1 to that slot, #2 to the next slot, and so on.
3. For a batch, present the schedule as a table: post (idea + chosen variant + first line) → date + time, and report assignments as you queue.

LinkedIn allows scheduling up to roughly 3 months out.

## The browser flow (per approved post)

Preconditions: Chrome paired (`list_connected_browsers`), the user logged into LinkedIn.

1. `tabs_context_mcp { createIfEmpty: true }`, navigate to `https://www.linkedin.com/feed/`.
2. Click **Start a post** to open the composer. Confirm it shows the user's name as author.
3. **Set visibility to Anyone** if their organic posts are public. Click the audience dropdown under their name, choose **Anyone**, confirm it reads "Post to Anyone" before continuing.
4. Click into the text area and `type` the approved post body. Build linearly from the top. Do not use the `End` key (it jumps to end-of-line in LinkedIn's contenteditable and corrupts text); cmd+Z recovers reliably. Resolve any @mentions with the separate-action picker dance (`type("@")` → wait → `type(name)` → wait → screenshot → click the right entry; a real mention renders bold). See linkedin-draft-via-browser.md for the full @mention and URL-preview-cache notes, which apply identically here.
5. Click the **clock / schedule icon** at the bottom-right of the composer (just left of the Post button).
6. In the **Schedule** dialog, set the **Date** and **Time** to the target slot. Confirm the timezone shown is correct. Screenshot to verify both fields before proceeding.
7. Click **Next**. The composer's primary button now reads **Schedule** instead of Post.
8. Click **Schedule**. Confirm the success toast ("Post scheduled") and that the time shown matches the intended slot.
9. Repeat for the next approved post and its slot.

## Verify and hand off

- After all posts are scheduled, open the scheduled-posts view (composer clock icon → "View all scheduled posts") and screenshot it so the user can see the full queue.
- Tell them: each post, its scheduled date/time, and where to edit/cancel any of them. Remind them they can still attach a hero image to a scheduled post by editing it before it goes live.
- Flag anything that didn't resolve (an @mention left as plain text, a visibility setting to double-check).

## Composer mechanics (hard-won; these WILL bite)

- **Cursor-jump corruption.** After a mention resolves, the composer asynchronously resets the caret to just after the last mention entity. Keystrokes sent at the start of a NEW tool batch can land mid-text and silently corrupt it. Rules: (1) type the text that follows a mention in the SAME batch as the picker click; (2) never start a batch with keyboard input, always `left_click` first to place the caret; (3) `cmd+Z` recovers reliably, one step at a time, verify each undo with a screenshot.
- **Escape is dangerous.** With no picker open, Escape triggers the "Save this post as a draft?" close dialog. Only press Escape when a mention picker is visibly open; otherwise clean up stray `@text` with click + backspaces.
- **Mention typeahead limits.** Shows only ~3 results and ranks people/connections first. Some companies never surface. One retrigger attempt (backspace one char, retype) is enough; after that, leave plain text and flag it.
- **The editor ignores mouse-wheel scrolling.** Navigate with `cmd+Up` / `cmd+Down` / arrow keys; the view follows the caret. `End` is forbidden; `cmd+Left` (line start) is safe.
- **Schedule dialog:** clicking the Date field opens a calendar popup that swallows any typing meant for the Time field. Set the date (type it, then click the day in the calendar to commit), THEN triple-click the Time field and type, then click the dropdown suggestion. Verify the dialog's header line before clicking Next.

## Failure modes

- **Time too soon:** if a chosen slot is under LinkedIn's minimum lead time, bump to the next valid slot and tell the user.
- **Visibility left on Connections:** easy to miss. Verify "Post to Anyone" before scheduling if public reach matters.
- **Wrong timezone:** if LinkedIn shows a non-expected timezone, convert the target time to that zone, or flag it.
- **Schedule cap / errors:** if LinkedIn rejects a schedule, fall back to landing that post as a plain draft (see linkedin-draft-via-browser.md) and tell the user which ones need manual scheduling.
