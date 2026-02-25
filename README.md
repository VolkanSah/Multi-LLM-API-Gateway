# Universal MCP Hub (Sandboxed)

> For advanced use, have a look at [PyFundaments.md](PyFundaments.md) and the `docs/` folder.

Universal MCP Server running in **paranoid mode** — built on [PyFundaments](https://github.com/VolkanSah/PyFundaments) and licensed under ESOL.

The goal was simple: too many MCP servers out there with no sandboxing, hardcoded keys, and zero security thought. This one is different. No key = no tool = no crash. The Guardian (`main.py`) controls everything. `app/mcp.py` gets only what it needs, nothing more.

- MCP_HUB Built with Claude (Anthropic) as a typing tool. Architecture, security decisions
- Pyfundaments by Volkan Sah read [ESOL](ESOL)

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

- All API keys loaded via Secrets (env vars) — never hardcoded
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
