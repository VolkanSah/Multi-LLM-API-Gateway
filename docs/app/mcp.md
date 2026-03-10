## Datei: `app/mcp.py`

**Beschreibung:** Dieses Modul implementiert den **Model Context Protocol (MCP)** Server auf Basis von `FastMCP`. Es dient als Kommunikations-Schnittstelle (SSE) und registriert die Tools, die für LLMs oder andere Clients verfügbar gemacht werden.

### Hauptfunktionen:

* **`initialize()`**: Erstellt die MCP-Instanz, lädt die Konfiguration und stößt die Registrierung der Tool-Kategorien (LLM, Search, System) an.
* **`handle_request()`**: Der zentrale Einstiegspunkt für eingehende Anfragen vom Quart-Webserver. Hier können Logging, Authentifizierung oder Rate-Limiting für den gesamten MCP-Traffic implementiert werden.
* **`_register_llm_tools()`**: Registriert das `llm_complete`-Tool, sofern aktive LLM-Provider vorhanden sind. Die Logik wird dabei komplett an `tools.py` delegiert.
* **`_register_search_tools()`**: Registriert das `web_search`-Tool für Internetabfragen (sobald Provider konfiguriert sind).
* **`_register_system_tools()`**: Stellt "einfache" Tools bereit, die keine API-Keys benötigen, wie `list_active_tools`, `health_check` und `get_model_info`.

### Kern-Logik:

Die Datei folgt dem **Delegations-Prinzip**: `mcp.py` definiert lediglich *was* nach außen hin als Tool sichtbar ist, führt aber selbst keine Logik aus. Die tatsächliche Arbeit wird an `tools.py` und `providers.py` weitergereicht. Durch diesen Aufbau bleibt die MCP-Schnittstelle stabil, auch wenn du im Hintergrund neue Provider hinzufügst.

