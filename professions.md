# Berufs- und Lernsystem

Diese Datei gibt einen menschenlesbaren Überblick über das Berufs- und
Lernsystem des Servers. Sie beschreibt die fachliche Idee und den aktuellen
Stand, ohne die technischen Konfigurationsdateien zu ersetzen.

## Grundidee

Spieler lernen durch passende Tätigkeiten. Dabei sammeln sie Erfahrung in
einzelnen Tätigkeitszweigen und steigen innerhalb dieser Zweige im Rang auf.
Zusätzliche Qualifikationen oder Lizenzen weisen eine Ausbildung, Einweisung
oder Prüfung nach.

Das System verbindet deshalb zwei unterschiedliche Arten von Fortschritt:

- **Rang:** entsteht vor allem durch praktische Erfahrung.
- **Qualifikation oder Lizenz:** wird durch eine Ausbildung, Prüfung oder
  vergleichbare Freigabe erworben.

Eine Fähigkeit kann nur einen bestimmten Rang, nur eine Qualifikation oder
beides gleichzeitig verlangen.

## Freies Lernen und Spezialisierung

Jeder Spieler darf grundsätzlich alle Zweige lernen. Es gibt keine feste
Klassenwahl und keine harte Obergrenze für die Zahl der Berufe.

Breite Grundkenntnisse sollen gut erreichbar sein. Hohe Ränge werden dagegen
zunehmend aufwendig. Dadurch entsteht eine natürliche Spezialisierung, ohne
Spieler dauerhaft von anderen Lernwegen auszuschließen.

Als langfristige Orientierung gilt:

- Pfuscher und Lehrling sollen in vielen Zweigen erreichbar sein.
- Gesellenränge stellen eine erste deutliche Spezialisierung dar.
- Meister sollen selten und besonders wertvoll sein.
- Ingenieursränge bilden sehr aufwendige Spitzenqualifikationen.

Diese Verteilung wird durch steigenden Aufwand erzeugt, nicht durch starre
Verbote.

## Grundzweige

Das System beginnt mit fünf breiten Tätigkeitszweigen:

### Handwerk

Handwerk umfasst das Herstellen und Bearbeiten von Werkzeugen, Bauteilen und
Gebrauchsgegenständen. Der erste spielbare Test konzentriert sich auf diesen
Zweig.

### Bauwesen

Bauwesen umfasst geplantes Bauen, konstruktive Arbeiten und später mögliche
Spezialisierungen wie Straßenbau, Tiefbau oder Festungsbau.

### Bergbau

Bergbau umfasst das Erschließen von Lagerstätten, den Abbau von Gestein und
Erzen sowie später den Betrieb technischer Bergbausysteme.

### Landwirtschaft

Landwirtschaft umfasst Anbau, Pflege und Ernte von Nutzpflanzen. Spätere
Spezialisierungen können beispielsweise Ackerbau, Gartenbau oder
Pflanzenzucht sein.

### Forstwirtschaft

Forstwirtschaft umfasst nachhaltige Holzgewinnung, Aufforstung und den Umgang
mit unterschiedlichen Baumarten.

## Ränge

Die gegenwärtige Testfassung verwendet in allen fünf Grundzweigen zunächst
dieselben drei Ränge:

| Rang | Vorläufige XP-Schwelle |
| --- | ---: |
| Pfuscher | 0 |
| Lehrling | 100 |
| Geselle | 300 |

Die Werte dienen dem Testbetrieb und stellen noch kein endgültiges Balancing
dar. Meister- und Ingenieursränge werden später ergänzt.

## Qualifikationen und Lizenzen

Qualifikationen bleiben von den Erfahrungsrängen getrennt. Dadurch kann ein
Spieler viel praktische Erfahrung besitzen, aber für eine besondere Maschine
oder eine sicherheitsrelevante Tätigkeit weiterhin eine Einweisung benötigen.

Die erste Testqualifikation ist **Werkzeugkunde**. Sie wird momentan durch
einen Administrator vergeben. Später kann die Ausbildung durch ein externes
System erfolgen; Epic ist dafür ein mögliches Beispiel, aber keine feste
Abhängigkeit des Berufssystems.

## Aktueller Handwerkstest

Nur der Zweig Handwerk besitzt derzeit konkrete XP-Quellen und
Berechtigungsprüfungen. Handwerks-XP entstehen beim Herstellen von:

- Holzbrettern
- Stöcken
- Fackeln
- Holzwerkzeugen
- Truhen

Viele identische Wiederholungen geben innerhalb eines Zeitfensters zunehmend
weniger Erfahrung. Damit soll einfaches Massen-Crafting als alleinige
Fortschrittsquelle unattraktiv werden.

### Holzwerkbank

Die Holzwerkbank ist das erste Testgerät:

- Herstellung ab Handwerksrang Lehrling
- Benutzung ab Lehrling mit Werkzeugkunde
- Platzieren für alle Spieler erlaubt

Sie verarbeitet einen Holzblock zu vier Übungsbauteilen.

### Moreblocks-Kreissäge

Wenn Moreblocks installiert ist, gelten für dessen Kreissäge dieselben
Voraussetzungen wie für die Holzwerkbank. Die Kreissäge ersetzt die Werkbank
nicht; beide bleiben verfügbar.

Treppen und Platten bleiben grundlegende Inhalte und dürfen ohne Berufsrang
hergestellt werden.

## Abhängige und kombinierte Zweige

Spätere Zweige dürfen Voraussetzungen besitzen und tiefer im Lernmodell
beginnen. Ein fortgeschrittener Zweig kann Erfahrung und Abschlüsse aus
mehreren Grundzweigen verbinden.

Ein mögliches Beispiel ist ein Bergbaumeister-Zweig, der fortgeschrittenes
Bauwesen, Bergbauerfahrung und eine Untertagebau-Qualifikation voraussetzt.
Dieser Zweig könnte Fähigkeiten für Minenplanung, Minecarts, Förderanlagen
und Liftsysteme eröffnen.

Das Erfüllen der Voraussetzungen verleiht nicht automatisch einen hohen Rang
im neuen Zweig. Es öffnet lediglich den neuen Lernweg, der anschließend eigene
Erfahrung besitzt.

## Einbindung des Modsets

Langfristig können Tätigkeiten und Berechtigungen aus dem gesamten Modset in
das Lernsystem einfließen. Dabei sollen allgemeine Material- und
Gegenstandsgruppen möglichst viele Mods gemeinsam abdecken. Große Systeme wie
Moreblocks, Technic, Pipeworks, Farming oder Minecarts können bei Bedarf eigene
Adapter erhalten.

Die technische Umsetzung soll Regeln beim Serverstart vorbereiten, damit eine
Spieleraktion nur die tatsächlich passenden Zweige prüft. Auch bei vielen
Zweigen dürfen nicht sämtliche Berufsregeln für jeden abgebauten oder
platzierten Block durchsucht werden.

XP-Meldungen und Speichervorgänge sollen bei zunehmender Zahl von Tätigkeiten
gebündelt werden. Dadurch bleibt das System auch mit vielen Berufszweigen und
mehr als zehn gleichzeitig aktiven Spielern tragfähig.

## Aktueller Projektstand

- Fünf Grundzweige sind angelegt.
- Handwerk ist als erster vertikaler Test spielbar.
- Werkzeugkunde ist die erste Qualifikation.
- Holzwerkbank und optionale Moreblocks-Kreissäge sind integriert.
- Deutsche und englische Texte sind vorhanden.
- Die Mod ist im Docker-Branch `testing` eingebunden.
- Die weiteren vier Grundzweige besitzen noch keine XP-Quellen oder Rechte.

Neue Zweige, konkrete XP-Quellen, Voraussetzungen und Berechtigungen werden
schrittweise geplant, umgesetzt und zunächst im Branch `testing` erprobt. Erst
nach erfolgreichem Test werden sie für eine Übernahme nach `main` vorgesehen.

## Verhältnis zu den Konfigurationsdateien

Diese Datei erklärt das fachliche Modell. Die Konfigurationsdateien sind die
technische Dokumentation und die verbindliche maschinenlesbare Definition des
jeweiligen Stands.

Bei einer Änderung des Systems sollen deshalb beide Ebenen gepflegt werden:

1. Die Konfiguration beschreibt exakt, was der Server ausführt.
2. Diese Datei erklärt verständlich, was Spieler und Administratoren davon
   erwarten können.
