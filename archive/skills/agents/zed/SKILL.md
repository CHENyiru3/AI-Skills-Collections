---
name: zed
domain: agents
description: >-
  Configure Zed editor settings, keybindings, agent profiles, and AI
  integrations. Use when modifying Zed configuration, setting up agent profiles
  such as plan mode, configuring language servers, themes, or AI models.
  Keywords: zed, editor, settings, keybindings, keymap, LSP, language server,
  theme, agent, configure, model, MiniMax.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Editor, Zed, AI-Agent, Configuration, Keybindings]
    related_skills: [claude-code, codex]
---

# Zed Editor Configuration

Configure Zed editor's agent system, settings, and keybindings.

## Configuration Files

| File | Purpose |
|------|---------|
| `~/.config/zed/settings.json` | Main editor settings, agent profiles, theme, fonts |
| `~/.config/zed/keymap.json` | Custom keybindings (optional) |
| `~/.config/zed/prompts/` | Custom agent system prompts |
| `~/.config/zed/themes/` | Custom themes |

## Agent Profiles

### Basic Structure

```json
"agent": {
  "default_profile": "plan",
  "profiles": {
    "my-profile": {
      "name": "my-profile",
      "mode": "write",
      "system_prompt": "file://~/.config/zed/prompts/my-prompt.md"
    }
  }
}
```

### Agent Modes

Zed supports **agent modes** that control tool capabilities:

| Mode | Tools | Purpose |
|------|-------|---------|
| `write` | Full access (read_file, edit_file, create_directory, delete_path, etc.) | File modification |
| `ask` | read_file, grep, find_path, list_directory only | Read-only analysis |
| `minimal` | read_file, list_directory only | Safest, restricted |

### Model Configuration

Configure custom AI models via `openai_compatible`:

```json
"language_models": {
  "openai_compatible": {
    "MyModel": {
      "api_url": "https://api.example.com/v1",
      "available_models": [
        {
          "name": "my-model",
          "max_tokens": 200000,
          "max_output_tokens": 32000,
          "capabilities": {
            "tools": true,
            "images": false,
            "parallel_tool_calls": false,
            "chat_completions": true
          }
        }
      ]
    }
  }
}
```

### Tool Permissions

```json
"tool_permissions": {
  "tools": {
    "terminal": {
      "default": "allow"
    }
  }
}
```

## Custom System Prompts

Create prompt files in `~/.config/zed/prompts/`:

```markdown
# My Custom Prompt

You are a specialized coding assistant. Your role is to...

## Communication Style

- Be concise
- No comments in code by default

## Your Process

1. Understand requirements
2. Explore the codebase
3. Implement solution
```

Reference in profile:
```json
"system_prompt": "file://~/.config/zed/prompts/my-prompt.md"
```

## Keybindings

Create `~/.config/zed/keymap.json`:

```json
[
  {
    "context": "Editor",
    "bindings": {
      "cmd-shift-p": "agent::Toggle"
    }
  }
]
```

**Note**: Keybinding actions for agents vary by version. If errors occur, use the command palette instead.

## Common Tasks

### Set Default Agent Profile

```json
"agent": {
  "default_profile": "my-profile"
}
```

### Create Plan Mode Profile

```json
"profiles": {
  "plan": {
    "name": "plan",
    "mode": "ask",
    "system_prompt": "file://~/.config/zed/prompts/plan-mode.md",
    "enable_all_context_servers": false,
    "context_servers": {}
  }
}
```

### Configure External Agent Server

```json
"agent_servers": {
  "my-agent": {
    "type": "registry"
  }
}
```

### Theme Configuration

```json
"theme": {
  "mode": "dark",
  "light": "One Light",
  "dark": "Ayu Dark"
}
```

### Font Settings

```json
"ui_font_size": 16,
"buffer_font_size": 15
```

### SSH Connections

```json
"ssh_connections": [
  {
    "host": "my-server",
    "args": [],
    "projects": [
      {
        "paths": ["/remote/path"]
      }
    ]
  }
]
```

## Verification

After modifying settings:

1. **Restart Zed** or wait for settings to reload
2. **Check command palette** (`Cmd+Shift+P`) for agent options
3. **Test agent** by invoking from the agent panel

## Troubleshooting

### Keybinding Errors

If keymap shows errors, remove the file and use the command palette instead:
```bash
rm ~/.config/zed/keymap.json
```

### Profile Not Loading

- Verify JSON syntax is valid
- Check file paths use `file://` prefix
- Ensure profile name matches `default_profile` reference

### Model Not Available

- Verify `api_url` is correct
- Check `capabilities` match model support
- Ensure model name matches exactly
