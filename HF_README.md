---
title: Universal MCP Hub
emoji: 🐢
colorFrom: red
colorTo: yellow
sdk: docker
pinned: false
license: apache-2.0
short_description: Universal MCP Hub (Sandboxed)
---

# Universal MCP Hub (Sandboxed)

> For advanced use, have a look at [PyFundaments.md](PyFundaments.md) and the `docs/` folder.

Universal MCP Server running in **paranoid mode** — built on [PyFundaments](https://github.com/VolkanSah/PyFundaments) and licensed under ESOL.

The goal was simple: too many MCP servers out there with no sandboxing, hardcoded keys, and zero security thought. This one is different. No key = no tool = no crash. The Guardian (`main.py`) controls everything. `app/mcp.py` gets only what it needs, nothing more.

- MCP_HUB Built with Claude (Anthropic) as a typing tool. Architecture, security decisions
- Pyfundaments by Volkan Sah read [ESOL](ESOL)

---

## Setup

1. **Fork** this Space.
2. Enter your API keys as **Space Secrets** (Settings → Variables and secrets).
3. The Space starts automatically — only tools with valid keys will be registered.

---

## Available Tools (Depending on Configured Keys)

| Secret | Tool | Description |
| :--- | :--- | :--- |
| `ANTHROPIC_API_KEY` | `anthropic_complete` | Claude Models |
| `GEMINI_API_KEY` | `gemini_complete` | Google Gemini Models |
| `OPENROUTER_API_KEY` | `openrouter_complete` | 100+ Models via OpenRouter |
| `HF_TOKEN` | `hf_inference` | HuggingFace Inference API |
| `BRAVE_API_KEY` | `brave_search` | Web Search (independent index) |
| `TAVILY_API_KEY` | `tavily_search` | AI-optimized Search |
| *(Always Active)* | `list_active_tools` | Shows all currently active tools |
| *(Always Active)* | `health_check` | System health check |

---

## MCP Client Configuration (SSE)

To connect Claude Desktop or any MCP client to this hub:

```json
{
  "mcpServers": {
    "pyfundaments-hub": {
      "url": "https://YOUR_USERNAME-universal-mcp-hub.hf.space/sse"
    }
  }
}
```

---

## Architecture

```
main.py  ← Guardian: initializes all services, controls what app/ receives
  └── app/mcp.py  ← Sandbox: registers only tools with valid keys
        ├── LLM tools    (Anthropic, Gemini, OpenRouter, HuggingFace)
        ├── Search tools (Brave, Tavily)
        ├── DB tools     (only if DATABASE_URL is set)
        └── System tools (always active)
```

**The Guardian pattern:** `app/mcp.py` never reads `os.environ` directly.
It receives a `fundaments` dict from `main.py` — and only what `main.py` decides to give it.

---

## Security Notes

- All API keys loaded via HuggingFace Space Secrets (env vars) — never hardcoded
- `list_active_tools` returns key **names** only, never values
- DB tools are read-only by design (`SELECT` only, enforced at application level)
- Direct execution of `app/mcp.py` is blocked by design
- Built on PyFundaments — a security-first Python architecture for developers

> PyFundaments is not perfect. But it's more secure than most of what runs in production.

---

## License

Apache License 2.0 + [ESOL 1.1](https://github.com/VolkanSah/ESOL)

---

*"I use AI as a tool, not as a replacement for thinking."* — Volkan Kücükbudak
