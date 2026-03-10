## Datei: `app/db_sync.py`

**Beschreibung:** Dieses Modul verwaltet den internen Zustand des Hubs über eine lokale SQLite-Datenbank. Es dient als persistenter Zwischenspeicher (IPC) für App-spezifische Daten und Tool-Antworten, getrennt von der Hauptdatenbank des Systems.

### Hauptfunktionen:

* **`initialize()`**: Setzt den Datenbankpfad (inkl. Sonderlogik für HuggingFace Spaces) und initialisiert die Tabellen.
* **Key/Value Store (`write`, `read`, `delete`)**: Ermöglicht es anderen Modulen, einfache Daten (wie Statusmeldungen oder Konfigurationen) JSON-serialisiert in der Tabelle `hub_state` zu speichern.
* **Tool-Caching (`cache_write`, `cache_read`)**: Speichert Tool-Antworten in `tool_cache`, um redundante API-Aufrufe zu vermeiden und Kosten zu sparen. Beinhaltet eine automatische Begrenzung der maximalen Einträge.
* **`query()`**: Erlaubt die Ausführung von SQL-Abfragen, beschränkt diese jedoch strikt auf **READ-ONLY** (nur `SELECT`), um die Datenintegrität zu wahren.

### Kern-Logik:

Das Modul folgt einer strikten **Table Ownership**: Es verwaltet ausschließlich `hub_state` und `tool_cache`. Der Zugriff auf systemkritische Tabellen (wie Benutzer oder Sessions) ist untersagt. Zudem ist es "Sandboxed" konzipiert, sodass es keinen direkten Zugriff auf globale Umgebungsvariablen benötigt, sondern alles über `config.py` bezieht.
