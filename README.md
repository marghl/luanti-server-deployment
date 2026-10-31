# Luanti container deployment

Dieses Repository beschreibt den lokalen Test- und spaeteren Produktivbetrieb
des Luanti-Servers mit Mapserver, Prometheus, Grafana und Reverse Proxy.

## Grundsaetze

- Konfiguration und festgelegte Softwarestaende werden versioniert.
- Welten, Datenbanken, Metriken und Geheimnisse werden nicht versioniert.
- Lokal werden unprivilegierte Host-Ports und Weltkopien verwendet.
- Produktion verwendet feste Image- und Mod-Versionen.

## Compose-Dateien

- `compose.yaml`: gemeinsame Dienstdefinitionen
- `compose.local.yaml`: lokale Ports, Weltkopie und Entwicklungsoptionen
- `compose.production.yaml`: produktive Restart-Regeln und Datenpfade

Die Luanti-Konfiguration wird aus `config/base/` und den einzelnen
Modkonfigurationen unter `config/mods/` erzeugt. Lokal und in Produktion
werden dieselben Dateien aus `generated/` eingebunden. Unterschiede zwischen
Test und Produktion entstehen damit ausschliesslich durch den verwendeten
Git-Branch und lokale Geheimnisse beziehungsweise Laufzeitpfade.

Beim Start werden die nicht versionierten Dateien `secrets/server.conf`,
`secrets/mapserver.conf` und `secrets/lorebridge.conf` an die erzeugte
Serverkonfiguration angehaengt.

Der erste Migrationsschritt startet Luanti 5.17.0 mit der wiederhergestellten
SQLite-Welt. Spiel und Mods werden schreibgeschuetzt eingebunden. Die Welt
unter `state/world` und der Modbestand unter `state/mods` sind separate
Arbeitskopien. Vorhandene Git-Metadaten der Mods bleiben darin erhalten, sodass
ihre Staende direkt mit den jeweiligen Upstreams verglichen werden koennen.

Mapserver 4.10.0 wird aus dem offiziellen Quellcode gebaut. Seine lokale
Konfiguration orientiert sich an der produktiven Instanz, verwendet aber ein
eigenes Geheimnis und getrennte Laufzeitdaten unter `state/mapserver`.
MediaWiki 1.43.11 wird aus dem lokal gepinnten Checkout unter `../mediawiki`
(Tag `1.43.11`, Commit `8c65f3e1545`) gebaut und verwendet MariaDB 11.4.13.
Prometheus und Grafana werden anschliessend ergaenzt. Caddy stellt Mapserver
und MediaWiki bereits ueber einen gemeinsamen Reverse Proxy bereit.

## Lokaler Aufruf

```bash
cp .env.example .env
./scripts/start.sh
./scripts/logs.sh
./scripts/stop.sh
```

Luanti ist lokal auf UDP-Port `30000` erreichbar. Ueber den Reverse Proxy sind
Mapserver unter `http://map.localhost:8080` und MediaWiki unter
`http://wiki.localhost:8080` erreichbar. Fuer die direkte Fehlersuche bleiben
Mapserver unter `http://localhost:8081` und MediaWiki unter
`http://localhost:8082` erreichbar. Die Instanz wird nicht beim
oeffentlichen Serververzeichnis angemeldet (`server_announce = false`).

In Produktion setzt `compose.production.yaml` die Adressen auf
`map.marghl.de` und `wiki.marghl.de`. Caddy veroeffentlicht dort TCP-Port 80
und 443 und verwaltet die TLS-Zertifikate automatisch; Mapserver und MediaWiki
besitzen keine eigenen Host-Ports.

Die produktive Compose-Konfiguration wird explizit ohne lokale Overrides
gestartet:

```bash
./scripts/modconfig.sh generate
docker compose -f compose.yaml -f compose.production.yaml up -d
```

Vor dem ersten Start muessen Podman oder Docker sowie deren Compose-Erweiterung
installiert sein. Danach:

```bash
cp .env.example .env
./scripts/start.sh
./scripts/logs.sh luanti
```

## Verzeichnisse

- `config/`: versionierbare Dienstkonfiguration
- `images/`: selbst gebaute Images
- `scripts/`: Betriebs- und Testbefehle
- `tests/`: Integrations- und Wiederherstellungstests
- `state/`: lokale Laufzeitdaten; wird nicht versioniert
- `secrets/`: lokale Geheimnisse; wird nicht versioniert

## Modkonfiguration

Der Teststand wird nicht direkt in `world.mt` oder `server.conf` gepflegt.
Jeder erkannte Mod besitzt stattdessen ein Verzeichnis unter `config/mods/`:

```text
config/mods/mapserver/
|-- mod.conf
`-- settings.conf
```

Alle Dateien verwenden ausschliesslich `schluessel = wert`; `#` beginnt einen
Kommentar. `mod.conf` legt Aktivierung, Checkout-Verzeichnis, Modpfad,
Abhaengigkeiten und - soweit bereits bekannt - Git-URL und Commit fest.
`settings.conf` dokumentiert die aus `settingtypes.txt` importierten
Standardwerte auskommentiert. Nur nicht auskommentierte Werte werden aktiv.

Die Dateien `generated/server.conf` und `generated/world.mt` werden daraus
erzeugt und sowohl lokal als auch produktiv in den Luanti-Container
eingebunden:

```bash
./scripts/modconfig.sh generate
./scripts/modconfig.sh verify
./scripts/modconfig.sh status
./scripts/modconfig.sh sync --check
./scripts/modconfig.sh sync
```

`./scripts/start.sh` erzeugt die Konfiguration vor jedem Start erneut.
Generierte Dateien sollen nicht von Hand geaendert werden.

`sync --check` prueft die Checkout-Struktur, Git-URLs und lokale Aenderungen,
ohne Dateien anzufassen. `sync` klont fehlende Git-Checkouts und stellt
vorhandene saubere Checkouts exakt auf den in `git_commit` festgelegten Stand.
Mehrere Mods eines Modpacks werden dabei als ein gemeinsamer Checkout
behandelt. Bei lokalen Aenderungen, abweichender Herkunft oder
widerspruechlichen Manifesten wird vor der ersten Aenderung abgebrochen.

Ein `source = existing` markiert einen aus der Sicherung uebernommenen Mod,
dessen Herkunft noch inventarisiert werden muss. Erst nach Eintrag von
`git_url` und `git_commit` ist dieser Checkout reproduzierbar. `sync` laesst
solche Checkouts unveraendert und loescht auch keine unbekannten Verzeichnisse.

Produktive Daten sollen nicht innerhalb dieses Repositories liegen. Ihre
Pfade werden ueber die `.env`-Datei konfiguriert. `SERVICE_UID` und
`SERVICE_GID` muessen der numerischen UID/GID des produktiven Dienstbenutzers
entsprechen, damit Luanti und Mapserver auf die Bind-Mounts zugreifen koennen.

Vor dem Mapserver-Start wird die lokale, ignorierte Konfiguration einmalig aus
der Vorlage erzeugt und ihr Platzhalterschluessel ersetzt:

```bash
cp config/mapserver/mapserver.example.json config/mapserver/mapserver.json
```
