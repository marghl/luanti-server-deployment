# Inventarisierung der uebernommenen Mods

Stand: 2026-10-31

## Ausgangslage

- 117 Checkouts mit `source = existing`
- 256 Modnamen in diesen Checkouts
- 114 von 117 Checkout-Namen besitzen einen exakten Namenskandidaten in
  ContentDB.
- Ohne exakten ContentDB-Namen: `hyperloop`, `lore`, `world_layers`

Ein gleicher Name allein reicht nicht zum Eintragen von `source = git`.
Repository, enthaltene Modnamen und der konkrete Commit muessen zusaetzlich
gegen die lokale Sicherung geprueft werden.

## Inhaltlich bestaetigte Kandidaten

Bei diesen Kandidaten stimmt der lokale Inhalt mit dem angegebenen Commit
ueberein. Von ContentDB an `mod.conf` angehaengte Felder wie `release` und
`author` werden beim Vergleich ignoriert beziehungsweise gesondert bewertet.

| Checkout | Repository | Commit | Befund |
| --- | --- | --- | --- |
| `basic_materials` | `https://github.com/mt-mods/basic_materials` | `f626da067a39206b7d60c1122843cd951ffb7081` | HEAD stimmt ueberein; nur ContentDB-Felder in `mod.conf` zusaetzlich |
| `cartographer` | `https://codeberg.org/HuguesRoss/cartographer` | `c51eb2168bb6d22fb8921d040f253eb8871df7bd` | HEAD stimmt ueberein; nur ContentDB-Felder in `mod.conf` zusaetzlich |
| `lighting_monoid` | `https://github.com/t-affeldt/lighting_monoids` | `7ac833bb19127921fa9a8c6805b954a3581815a9` | HEAD stimmt ueberein; nur ContentDB-Releasefeld zusaetzlich |
| `pipeworks` | `https://github.com/mt-mods/pipeworks` | `5dfd572eacee4c3c1ed8b827f4a67c46b022b242` | HEAD stimmt ueberein; nur ContentDB-Felder in `mod.conf` zusaetzlich |
| `lore` | `https://github.com/marghl/lore.git` | `93b8c9d79c1a55403d33b3dd9481e13477252fde` | lokale Quellarbeitskopie stimmt bis auf nicht ausgelieferte Hilfsdateien ueberein |
| `world_layers` | `https://github.com/marghl/world_layers.git` | `9f9e2aa5f2ff4a7b2cdc98f9e4b38fe5a2292fd9` | lokale Quellarbeitskopie stimmt ueberein |

## Eindeutiger Kandidat, Commit noch offen

| Checkout | Kandidat | Befund |
| --- | --- | --- |
| `hyperloop` | `https://github.com/joe7575/Minetest-Hyperloop` | Repository ist durch README und Autor eindeutig; aktuelles HEAD weicht in `booking_node.lua` und `map.lua` ab, daher muss der zu ContentDB-Release `35865` gehoerende Commit ermittelt werden. |
| `cartographer_minetest_game` | `https://gitlab.com/Df458/cartographer-mtg` | Repository steht in lokaler `.cdb.json`; anonymer Git-Zugriff war bei der Pruefung nicht moeglich. Lokaler ContentDB-Release ist `11904`. |

## ContentDB-Namenskonflikte

Diese Checkouts haben mehr als einen gleichnamigen oder im Modpack enthaltenen
ContentDB-Kandidaten und benoetigen eine genauere Inhaltspruefung:

- `cottages`: `Emojiminetest/cottages` oder `Sokomine/cottages`
- `homedecor_modpack`: Hauptkandidat `mt-mods/homedecor_modpack`, daneben
  Treffer fuer enthaltene Einzelmods
- `moreblocks`: `Calinou/moreblocks` oder `rheo/moreblocks`
- `nether`: `Hybrid Dog/nether` oder `PilzAdam/nether`
- `protector`: `TenPlus1/protector` oder `sorcerykid/protector`
- `simple_working_villages`: Hauptmod und separat veroeffentlichtes `modutil`
- `stamina`: `TenPlus1/stamina` oder `sofar/stamina`
- `technic_plus`: Modpacktreffer fuer `technic_plus` und `wrench`

## Naechster Arbeitsschritt

Zuerst die sechs inhaltlich bestaetigten Kandidaten in echte Git-Checkouts
ueberfuehren und erneut im laufenden Server testen. Danach die eindeutigen
ContentDB-Namenskandidaten in kleinen Gruppen vergleichen. Bestehende
Verzeichnisse werden erst ersetzt, wenn Repository und Commit nachweislich zum
gesicherten Inhalt passen.
