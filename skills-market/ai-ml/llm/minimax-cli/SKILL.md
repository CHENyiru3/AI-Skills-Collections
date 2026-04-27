---
name: minimax-cli
domain: ai-ml
description: Use the MiniMax `mmx` CLI as a unified multimodal generation and utility tool. Use this skill whenever the user asks to use MiniMax, mmx, MiniMax CLI, or wants terminal-driven text chat, image generation, video generation, text-to-speech, music generation or covers, image understanding, web search, quota checks, or MiniMax authentication/configuration.
version: 1.0.0
category: llm
---

# MiniMax CLI

Use `mmx` for MiniMax's multimodal command-line workflows: text, image, video, speech, music, vision, search, quota, and configuration. Prefer this skill when the user wants a direct MiniMax result from the terminal or wants MiniMax wired into an agent workflow.

## Prerequisites

- Node.js 18+.
- CLI installed:

```bash
npm install -g mmx-cli
mmx --version
```

- Authentication configured with a MiniMax token plan:

```bash
mmx auth login --method api-key --api-key sk-xxxxx
mmx auth status
mmx quota
```

MiniMax keys are region-specific. If `mmx quota` reports `invalid api key`, check whether the account belongs to the CN platform:

```bash
mmx config set --key region --value cn
mmx quota
```

Global defaults use `https://api.minimax.io`; CN defaults use `https://api.minimaxi.com`.

## Safety And Secret Handling

- Do not print or paste full API keys in final answers, logs, docs, commits, or examples.
- Prefer persistent config (`~/.mmx/config.json`) or environment variables over putting keys in shell history.
- Use `mmx config show` and `mmx auth status` for masked verification.
- Use `--dry-run` when constructing expensive media commands before execution.
- For long-running or costly video/music work, confirm prompt, model, output path, and whether the user wants synchronous waiting or async task IDs.

## Command Selection

| User intent | Command family | Good default |
|---|---|---|
| Chat, coding text, structured text | `mmx text chat` | `--message`, optional `--system`, `--output json` for parsing |
| Text-to-image | `mmx image generate` | `--prompt`, `--aspect-ratio`, `--out` or `--out-dir` |
| Text/image-to-video | `mmx video generate` | `--prompt`, optional `--first-frame`, `--download`, `--async` |
| Video task status/download | `mmx video task get`, `mmx video download` | Use task IDs and file IDs from earlier output |
| Text-to-speech | `mmx speech synthesize` | `--text` or `--text-file`, `--voice`, `--out` |
| Voice list | `mmx speech voices` | Filter with `--language` |
| Music generation | `mmx music generate` | Require lyrics, `--lyrics-file`, `--lyrics-optimizer`, or `--instrumental` |
| Music cover | `mmx music cover` | `--audio` or `--audio-file`, `--prompt`, optional lyrics |
| Image understanding | `mmx vision describe` | `--image`, optional question via `--prompt` |
| Web search | `mmx search query` | `--q`, use `--output json` for downstream parsing |
| Usage/budget | `mmx quota` or `mmx quota show` | Use before expensive media generation |
| Tool schema export | `mmx config export-schema` | Use for agent/tool integration |

Run `mmx --help` or `mmx <resource> <command> --help` for current flags before using an unfamiliar mode.

## Text

Use `mmx text chat` for conversational and structured text generation.

```bash
mmx text chat --message "What is MiniMax?"
mmx text chat --system "You are a concise coding assistant." --message "Write fizzbuzz in Python"
mmx text chat --model MiniMax-M2.7-highspeed --message "Summarize this API" --output json
```

For multi-turn context, repeat `--message`; prefix roles when needed:

```bash
mmx text chat \
  --message "user:Hi" \
  --message "assistant:Hello. What do you need?" \
  --message "Draft a short release note."
```

For agent workflows, prefer `--output json` when another tool will parse the result.

## Image

Use `mmx image generate` for text-to-image. Choose deterministic options when reproducibility matters.

```bash
mmx image generate --prompt "A clean icon of a desktop AI companion" --aspect-ratio 1:1 --out icon.jpg
mmx image generate --prompt "Wide scientific poster background" --width 1920 --height 1080 --seed 42 --out poster.jpg
mmx image generate --prompt "Character concept sheet" --n 3 --out-dir ./generated --out-prefix character
```

Notes:
- `--width` and `--height` override `--aspect-ratio`; dimensions must be multiples of 8 in the supported range.
- Use `--response-format base64` when returned CDN URLs are unreachable.
- Use `--prompt-optimizer` when the user gives a rough prompt and wants MiniMax to refine it.

## Video

Use `mmx video generate` for video generation. Decide whether the user wants to wait for a finished file or receive a task ID.

```bash
mmx video generate --prompt "Ocean waves at sunset. Static camera." --download sunset.mp4
mmx video generate --prompt "A robot painting in a studio." --async --quiet
```

Image-conditioned modes:

```bash
mmx video generate --prompt "Slow camera push-in" --first-frame start.jpg --download clip.mp4
mmx video generate --prompt "Walk forward" --first-frame start.jpg --last-frame end.jpg --download walk.mp4
mmx video generate --prompt "A detective walking through neon rain" --subject-image character.jpg --download detective.mp4
```

Task management:

```bash
mmx video task get --task-id 106916112212032 --output json
mmx video download --file-id 176844028768320 --out video.mp4
```

Use `--async` for agents, CI, or long tasks. Use `--download` when the user wants a local file and is willing to wait.

## Speech

Use `mmx speech synthesize` for TTS.

```bash
mmx speech synthesize --text "Hello, world." --out hello.mp3
echo "Breaking news." | mmx speech synthesize --text-file - --out news.mp3
mmx speech synthesize --text "Stream me" --stream | mpv --no-terminal -
```

Inspect voices before choosing one:

```bash
mmx speech voices --language english
mmx speech voices --output json
```

Common controls: `--voice`, `--speed`, `--volume`, `--pitch`, `--format`, `--sample-rate`, `--subtitles`, and repeated `--pronunciation from/to` entries.

## Music

Use `mmx music generate` for new music. The command requires lyrics, a lyrics file, lyric optimization, or instrumental mode.

```bash
mmx music generate --prompt "Cinematic orchestral, building tension" --instrumental --out bgm.mp3
mmx music generate --prompt "Upbeat pop about summer" --lyrics-optimizer --out summer.mp3
mmx music generate --prompt "Warm morning folk" --lyrics-file lyrics.txt --vocals "male and female duet" --bpm 95 --out duet.mp3
```

Use structured prompt flags instead of cramming every detail into one prompt when the user specifies musical constraints:

```bash
mmx music generate \
  --prompt "Opening theme for a science podcast" \
  --instrumental \
  --genre "ambient electronic" \
  --mood "curious, polished" \
  --instruments "soft synth, piano, light percussion" \
  --bpm 88 \
  --out theme.mp3
```

Use `mmx music cover` when the user provides reference audio:

```bash
mmx music cover --prompt "Jazz, piano, slow" --audio-file original.mp3 --lyrics-file lyrics.txt --out jazz-cover.mp3
mmx music cover --prompt "Indie folk, acoustic guitar, warm male vocal" --audio https://example.com/song.mp3 --out cover.mp3
```

## Vision

Use `mmx vision describe` for image understanding, OCR-style questions, and visual inspection.

```bash
mmx vision describe --image photo.jpg
mmx vision describe --image chart.png --prompt "Extract the axis labels and summarize the trend."
mmx vision describe --file-id file-123456789 --prompt "Extract the text."
```

## Search

Use `mmx search query` when the user specifically wants MiniMax-backed search or the workflow needs a MiniMax API result rather than browser scraping.

```bash
mmx search query --q "MiniMax AI latest release" --output json
```

For high-stakes or rapidly changing facts, still verify with authoritative sources when the user needs correctness beyond a single search result.

## Quota And Configuration

Check quota before expensive media generation:

```bash
mmx quota
mmx quota --output json
```

Useful config commands:

```bash
mmx config show
mmx config set --key region --value cn
mmx config set --key output --value json
mmx config set --key timeout --value 600
mmx config export-schema
mmx config export-schema --command "video generate"
```

Use `mmx update` to update the CLI when the user asks for current MiniMax CLI behavior or a command appears missing.

## Agent Workflow

1. Verify readiness with `mmx --version`, `mmx auth status`, and, for real API use, `mmx quota`.
2. Choose the command family from the user's intended output modality.
3. Run `mmx <resource> <command> --help` if the exact flags matter.
4. Prefer explicit output paths for generated assets.
5. Prefer JSON output for downstream parsing.
6. Use `--dry-run` for complex or expensive commands while composing.
7. Keep API keys masked and do not commit `~/.mmx/config.json`, generated secrets, or private media unless explicitly requested.
