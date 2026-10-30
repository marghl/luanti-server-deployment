# Lokale Geheimnisse

In diesem Verzeichnis duerfen lokal Dateien mit Passwoertern und Tokens liegen.
Alle Dateien ausser dieser Anleitung werden von Git ignoriert.

Geheimnisse niemals in Compose-Dateien, Images, `.env.example` oder Git
eintragen.

Erwartete Dateien:

- `server.conf`: allgemeine Luanti-Geheimnisse wie `default_password`
- `mapserver.conf`: interne Mapserver-URL und gemeinsamer API-Schluessel
- `lorebridge.conf`: gemeinsamer LoreBridge-API-Schluessel
- `mediawiki.env`: Datenbankzugang fuer MediaWiki und MariaDB

`mediawiki.env` wird auf dem Zielsystem aus `mediawiki.example.env` erzeugt.
Die `LocalSettings.php` liegt ohne eingebettete Geheimnisse versioniert unter
`config/mediawiki/` und liest sensible Werte aus der Umgebung.
