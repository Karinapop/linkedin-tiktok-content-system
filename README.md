# LinkedIn + TikTok Content System (a Claude skill)

Turn your raw content ideas into ready-to-post content for **LinkedIn and TikTok**, in your own voice, with a popular insight at the core of every post. It runs as a [Claude](https://claude.com/claude-code) **skill**: a folder of instructions Claude loads when you ask it to "turn my ideas into posts."

It is built around three things that make it actually useful instead of generic:

1. **Your voice.** On first run it reads your real LinkedIn posts and builds a voice profile, so drafts sound like you wrote them, not like a LinkedIn thought leader.
2. **A single source of truth.** One Apple Note ("Content Ideas") is the master doc. You paste raw ideas into its INBOX; the skill drains it, drafts each idea, prioritizes everything, tracks what you've published, and writes the organized result back.
3. **A learning loop.** It pulls deep analytics on your published posts (reach, saves, new followers, audience demographics), synthesizes what's working, and applies those learnings to every new draft, weighted toward your newest followers.

## What it produces per idea

- **LinkedIn:** one strongest voice-matched post, saved as a native **draft** in your LinkedIn (via browser automation, never auto-published, no scheduling).
- **TikTok:** 3 to 5 full shootable variants (hook, tight spoken script, caption, hashtags, sound), saved to the note and to disk for you to shoot.

It routes each idea to the right platform(s), keeps two independently-ranked priority lists, and refreshes a daily trends section from ~200 scraped posts across LinkedIn, X, and TikTok.

## Before you start: everything you need to set up

This system drives **your** real accounts and a **local** Apple Note, so it needs you to be logged in everywhere, to install one browser extension, and to grant a couple of macOS permissions. Set all of this up once. Nothing here costs money beyond your normal Claude subscription.

> **Total first-time setup: about 25 to 40 minutes.** After that, each content run is just a few minutes of reviewing drafts.

### 1. Software (install these)

| What | Why | Notes |
| --- | --- | --- |
| **Claude Code** (or a Claude client that supports skills) | Runs the skill itself | The skill is a folder Claude loads |
| **macOS** | Apple Notes (the source-of-truth note) is a local, Mac-only app | This system does not work on Windows/Linux, because it reads/writes Apple Notes locally |
| **Google Chrome** | All browser automation runs through Chrome | Use one Chrome profile for everything below |

### 2. Browser extension (this is the key one)

| Extension | Why | How |
| --- | --- | --- |
| **Claude for Chrome** extension | Lets Claude read your LinkedIn posts, scrape trends across LinkedIn/TikTok/X, and save LinkedIn drafts | Install from the [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn), then in each session click **Connect** in the extension so Claude can drive that tab. The skill checks this with `list_connected_browsers` and will ask you to pair if it isn't connected. |

There is **no Notes extension** to install. Apple Notes is native and is driven by AppleScript (osascript), which needs the macOS **Automation** permission below, not an extension.

### 3. Accounts and logins (all in the SAME Chrome profile)

Log into each of these in the Chrome where the extension is connected, and stay logged in:

| Account | Required? | What it's used for |
| --- | --- | --- |
| **LinkedIn** | **Required** | Reading your posts to build your voice profile, scraping LinkedIn trends, tracking your published-post analytics, and saving your drafts |
| **TikTok** | Recommended | Scraping TikTok trends and tracking your published TikToks. Skip it and TikTok trends fall back to web search (lower quality) |
| **X (Twitter)** | Optional | The live-trend "social pulse." If you skip it, the skill uses web search and/or the grok integration instead |

### 4. macOS permissions and approvals (grant these once)

| Permission | Where | Why |
| --- | --- | --- |
| **Automation → Notes** | System Settings → Privacy & Security → Automation. macOS prompts you the first time the skill runs an AppleScript ("…wants to control Notes" → **Allow**) | So the skill can read and write your Content Ideas note |
| **Claude tool permissions** | Claude prompts you in-session (Bash, the Chrome browser tools, web search) | Approve them, or set them to "always allow," so runs don't stop to ask each time |
| **Chrome "Connect" click** | The Claude for Chrome extension, each session | Re-pairs the browser so Claude can act in your tab |
| **Keep your Mac awake** (only for the optional daily auto-sync) | Energy settings / `caffeinate` | The scheduled morning run needs the Mac awake with Chrome paired |

The core flow does **not** need Accessibility or Screen Recording permissions. Those are only relevant if you later automate GUI-only steps (e.g. dragging a file attachment into a note); this shared version leaves that out.

### 5. Optional integrations

- **grok / X MCP** for the social pulse. Optional; web search is the built-in fallback.
- **A scheduled-task runner** if you want the daily "trends + note sync" to run automatically each morning.

## Install

1. Copy this folder into your Claude skills directory, e.g.:
   ```bash
   cp -r linkedin-tiktok-content-system ~/.claude/skills/idea-to-linkedin-tiktok
   ```
   (The skill's `name` is `idea-to-linkedin-tiktok`; the folder name can be anything.)
2. Restart Claude / reload skills so it picks up the new skill.
3. Run the one-time setup below.

## First-time setup (~25 to 40 min)

See **[SETUP.md](SETUP.md)** for the full walkthrough. In short:

1. **Install + connect the Claude for Chrome extension and log into LinkedIn, TikTok, and X** in that Chrome profile (~10 min, mostly logging in).
2. **Build your voice profile** (~5 to 10 min). Ask Claude: *"build my voice profile from my LinkedIn."* It connects to your LinkedIn in Chrome, reads ~15 of your recent posts, and fills in `references/voice-profile.md`. (Or paste 8 to 12 of your own posts into chat.)
3. **Create your Content Ideas note** in Apple Notes and tell Claude *"find my Content Ideas note ID"* to wire it up in `references/apple-notes-sync.md` (~5 min). Approve the macOS Automation prompt for Notes when it appears.
4. **Confirm your handles** (LinkedIn profile, optional TikTok handle) (~2 min).
5. **Optional:** ask Claude to schedule the daily trends + note sync (~3 min).

## Use

Paste ideas into your note's INBOX (or just say them in chat), then ask Claude things like:

- "Turn my ideas into posts."
- "Bake out these content ideas."
- "Make a LinkedIn post and TikTok script from this idea: ..."
- "Sync my content note / reprioritize my ideas."
- "What should I post next?"

The skill shows you drafts in chat first, you pick and iterate, and on "lock" it saves the LinkedIn post as a draft for you to publish yourself.

## Files

| File | What it is |
| --- | --- |
| `SKILL.md` | The main skill: workflow, drafting rules, the note contract. |
| `references/voice-profile.md` | Your voice profile (a template until you build it). |
| `references/voice-profile-bootstrap.md` | How the skill builds your voice from your real posts. |
| `references/apple-notes-sync.md` | The source-of-truth note: structure, analytics tracking, osascript mechanics. |
| `references/tiktok-script-format.md` | The short, shootable TikTok script format. |
| `references/linkedin-draft-via-browser.md` | Landing a LinkedIn draft via browser automation. |
| `references/linkedin-scheduling-via-browser.md` | Optional native scheduling (off by default). |
| `references/note-surgical-edit-template.py` | Safe surgical-edit pattern for the note. |
| `evals/evals.json` | Sample prompts for testing the skill. |
| `SETUP.md` | One-time personalization walkthrough. |

## Privacy

This skill reads and writes **your** accounts and a local Apple Note. It never auto-publishes: LinkedIn posts are saved as drafts you publish yourself. Your voice profile and content live on your machine. Nothing is sent anywhere except the accounts you point it at.

## License

MIT. See [LICENSE](LICENSE).
