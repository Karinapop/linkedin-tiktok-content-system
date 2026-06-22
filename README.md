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

## Requirements

- **Claude Code** (or another Claude client that supports skills).
- **macOS** with **Apple Notes** (the source-of-truth note is local).
- **Chrome** with the Claude in Chrome extension, logged into LinkedIn (and TikTok, optionally). Used to read your posts, scrape trends, and land LinkedIn drafts.
- Optional: an X/grok integration for the social pulse, and a scheduled-task runner for the daily sync.

## Install

1. Copy this folder into your Claude skills directory, e.g.:
   ```bash
   cp -r linkedin-tiktok-content-system ~/.claude/skills/idea-to-linkedin-tiktok
   ```
   (The skill's `name` is `idea-to-linkedin-tiktok`; the folder name can be anything.)
2. Restart Claude / reload skills so it picks up the new skill.
3. Run the one-time setup below.

## First-time setup

See **[SETUP.md](SETUP.md)** for the full walkthrough. In short:

1. **Build your voice profile.** Ask Claude: *"build my voice profile from my LinkedIn."* It connects to your LinkedIn in Chrome, reads ~15 of your recent posts, and fills in `references/voice-profile.md`. (Or paste 8 to 12 of your own posts into chat.)
2. **Create your Content Ideas note** in Apple Notes and tell Claude *"find my Content Ideas note ID"* to wire it up in `references/apple-notes-sync.md`.
3. **Confirm your handles** (LinkedIn profile, optional TikTok handle).

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
