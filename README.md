# Instagram Content Starter Kit

A reusable workflow for planning, creating and scheduling original Instagram content with ChatGPT and Metricool. Bring your own niche and accounts.

**Status: early starter kit.** Seven posts were successfully accepted into a real Metricool scheduling queue during development. Successful publication and the recurring workflow have not yet been verified. This is not a hosted service, one-click bot or promise of growth.

## What you need

- Your own professional Instagram account and Metricool connection.
- An AI workspace with image/file creation and the Metricool connector available. Availability and subscriptions vary; verify your account before paying.
- A recurring-task feature if you want unattended weekly runs. This repository does not create or run those tasks for you.
- Python 3.10+ only if using the optional local scripts.

## Start here

1. Copy this repository using **Use this template** (if enabled), or download its ZIP.
2. Copy `templates/brand.example.json` to `brand.json`; replace every placeholder.
3. Connect your own Instagram account in Metricool. Connect Metricool in your AI workspace. Ask it to read the connected brands and confirm your exact handle before any publishing.
4. Upload your completed brand brief and `templates/start-here.md` to a new conversation. Start with three draft posts.
5. Inspect the actual images/video, spelling, crop, caption and alt text. Ask it to schedule **one test post** with an explicit date and timezone.
6. Confirm that post actually appeared on Instagram. A pending queue entry is not proof of publication.
7. Only then activate the adapted `templates/weekly-automation.md` as a recurring task in your own workspace. Explicitly authorize its posting scope and cadence.
8. Keep a publishing log and inspect failures. Do not republish simply because an item disappeared from the pending queue.

## Included

| File | Purpose |
|---|---|
| `templates/brand.example.json` | Niche, audience, tone, visual identity and schedule |
| `templates/start-here.md` | Copyable launch instructions |
| `templates/weekly-automation.md` | Recurring production and scheduling instructions |
| `templates/post-log.csv` | Queue, publication and metric tracking |
| `templates/post.example.json` | Local post specification |
| `scripts/check_post.py` | Validate required inputs and future scheduling time |
| `scripts/render_card.py` | Create an editable SVG typography card |
| `docs/publishing.md` | Connector handoff, duplicate prevention and limitations |
| `docs/publish-repository.md` | Repository publication steps |

## Optional local example

```sh
python3 scripts/render_card.py templates/brand.example.json templates/post.example.json --out output/example.svg
python3 scripts/check_post.py templates/post.example.json
```

The renderer produces an editable **SVG**, not an Instagram upload file. Export it to PNG/JPEG using a design application and inspect the result before uploading. The checker deliberately rejects the example until its caption, date and media paths are filled in. Neither script contacts Instagram or schedules a post.

## What remains manual

Profile name/bio/avatar changes when your connected tools cannot edit them; story polls/questions; and unsupported Instagram music features. Do not mistake a graphic of a sticker for a functional sticker.

As checked on 14 October 2026, Metricool documents audio scheduling for Reels through its web editor with a Facebook-connected Instagram account, but not feed photos/carousels or Stories. Connector exposure may differ from the web editor. Read the current [audio documentation](https://help.metricool.com/how-to-add-audio-to-your-instagram-reels-from-metricool-2o2ks) before promising music automation.

## Privacy and permissions

Use your own authenticated connections. Never put credentials, session cookies, customer data or private account exports into this repository. `brand.json`, logs and generated output are ignored by Git. Public examples contain no real brand IDs or private file references. Do not grant access to unrelated repositories just to use this kit.

## License and provenance

The original files in this kit are MIT licensed; see LICENSE. The workflow was inspired by [Instagram Agent Skill](https://github.com/Jakeschincariol/instagram-agent-skill). No upstream code, private source PDF, competitor artwork or original account content is included in this kit. This is independent of Instagram, Meta, Metricool and OpenAI.
