---
title: Universal MCP Hub
emoji: 🔐
colorFrom: blue
colorTo: indigo
sdk: docker
app_port: 7860
pinned: false
---

# Universal MCP Hub on PyFundaments

Universal MCP-Server basierend auf [PyFundaments](https://github.com/VolkanSah/PyFundaments).

## Setup

1. Fork diesen Space
2. Trage deine API-Keys als **Space Secrets** ein (Settings → Variables and secrets)
3. Space startet automatisch

## Verfügbare Tools (je nach konfigurierten Keys)

| Secret | Tool | Beschreibung |
|--------|------|--------------|
| `ANTHROPIC_API_KEY` | `anthropic_complete` | Claude Modelle |
| `OPENROUTER_API_KEY` | `openrouter_complete` | 100+ Modelle via OpenRouter |
| `HF_TOKEN` | `hf_inference` | HuggingFace Inference API |
| `BRAVE_API_KEY` | `brave_search` | Web-Suche |
| `TAVILY_API_KEY` | `tavily_search` | KI-optimierte Suche |
| *(immer aktiv)* | `list_active_tools` | Zeigt aktive Tools |
| *(immer aktiv)* | `health_check` | Health-Check |

## MCP Client Konfiguration (SSE)

```json
{
  "mcpServers": {
    "pyfundaments-hub": {
      "url": "https://DEIN_USERNAME-pyfundaments-mcp-hub.hf.space/sse"
    }
  }
}
```

## Architektur

```
main.py (Wächter)
  └── initialisiert fundaments
  └── übergibt an app/mcp.py
        └── registriert nur Tools mit vorhandenen Keys
        └── startet SSE auf Port 7860
```

**Kein Key = kein Tool = kein Crash.** Der Wächter entscheidet was läuft.
