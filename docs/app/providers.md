## Datei: `app/providers.py`

**Beschreibung:** Dieses Modul verwaltet die Anbindung an verschiedene LLM-Provider (Anthropic, Gemini, OpenRouter, HuggingFace) und implementiert eine automatische Ausfallsteuerung (Fallback-Chain).

### Hauptfunktionen:

* **`BaseProvider` & Subklassen**: Eine Basisklasse definiert die HTTP-Logik (`_post`), während spezifische Provider-Klassen (z. B. `GeminiProvider`) nur die jeweilige API-Antwort verarbeiten.
* **`initialize()`**: Registriert beim Systemstart alle Provider, für die ein gültiger API-Key in der Umgebung (ENV) gefunden wurde.
* **`llm_complete()`**: Die Kernfunktion für Textgenerierung. Sie versucht, eine Anfrage über den gewählten Provider zu stellen, und springt bei Fehlern automatisch zum nächsten Provider in der Fallback-Kette.
* **`search()`**: Ein Platzhalter für zukünftige Web-Such-Provider (z. B. Brave oder Tavily).
* **Registry-Helper (`list_active_llm`, `get`)**: Gibt Informationen darüber aus, welche Provider aktuell einsatzbereit und konfiguriert sind.

### Kern-Logik:

Das Modul nutzt eine **Fallback-Chain-Logik**. Schlägt ein Aufruf fehl, wird in der Konfiguration (`.pyfun`) nachgeschaut, welcher Ersatz-Provider (`fallback_to`) genutzt werden soll. Ein "Visited"-Set verhindert dabei Endlosschleifen. Das Prinzip lautet: Keine Keys vorhanden = keine Provider registriert = kein Systemabsturz.
