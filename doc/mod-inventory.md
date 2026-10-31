# Mod-Inventar

Stand: 2026-10-31

## Regeln

Fuer die aus der Sicherung uebernommenen Mods werden bei unklarer Herkunft
ausschliesslich diese Quellen bevorzugt:

1. `mt-mods`
2. `TenPlus1`
3. `Sokomine`

`hyperloop` von `joe7575` wurde zusaetzlich ausdruecklich freigegeben. Andere
plausible Quellen bleiben unveraendert auf `source = existing`.

Ein Checkout wird nur auf `source = git` umgestellt, wenn Repository und
Commit durch einen Inhaltsvergleich bestaetigt wurden. ContentDB ergaenzt bei
installierten Paketen teilweise Metadaten wie `release`, `author`, `title`
oder `aliases` in `mod.conf` beziehungsweise `modpack.conf`. Solche Metadaten
gelten nicht als lokale Codeaenderung. Ebenso duerfen reine Entwicklungsdaten,
die ContentDB beim Paketbau auslaesst, im Git-Checkout zusaetzlich vorhanden
sein.

## Ergebnis

- 59 reproduzierbare Git-Checkouts
- 80 unveraenderte Checkouts mit `source = existing`
- Git-Fetch und Synchronisierung ueber HTTPS
- Git-Push ueber eine separate SSH-`pushurl`
- vorherige Verzeichnisse der aktuellen Runde unter
  `state/mods-backup/preferred-2026-10-31/`
- vorherige Verzeichnisse der ersten Runde unter
  `state/mods-backup/confirmed-2026-10-31/`

## In dieser Runde uebernommene Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `ambience` | `https://codeberg.org/tenplus1/ambience.git` | `4587abc9c2f611b71bb4d6313ca5f16a0292032f` |
| `bakedclay` | `https://codeberg.org/tenplus1/bakedclay.git` | `559bf143fc47891149059f972e93d231a5242370` |
| `bonemeal` | `https://codeberg.org/tenplus1/bonemeal.git` | `5b411548d0d33e83a4c931381309a6814041f258` |
| `cblocks` | `https://codeberg.org/tenplus1/cblocks.git` | `295ac2925ad25ffde9a555302c711a8dc55ae03a` |
| `coloredwood` | `https://github.com/mt-mods/coloredwood` | `90d43fdbba541060ae0a90384d55a485d153bb9a` |
| `digistuff` | `https://github.com/mt-mods/digistuff` | `58e302cb3ec8566d1aca8d4daa520ea0207459c3` |
| `dmobs` | `https://codeberg.org/tenplus1/dmobs.git` | `ad7513d9f92bb22b2fa5352985e63c044a6bc254` |
| `factory_bridges` | `https://github.com/mt-mods/factory_bridges` | `51fc78696f5bb4595a33bc3f72e359f8cb760589` |
| `farming` | `https://codeberg.org/tenplus1/farming.git` | `e0df1eb39dca74ce65fd087f9418d18cea218377` |
| `handle_schematics` | `https://github.com/Sokomine/handle_schematics` | `c130ffb71ef7867e23d891b8e412f603a1b43cde` |
| `homedecor_modpack` | `https://github.com/mt-mods/homedecor_modpack` | `992739d532808b6e671a0a4a618f9ed5cb41bdcd` |
| `hyperloop` | `https://github.com/joe7575/Minetest-Hyperloop` | `96fca7e2193f337c7e1e5e29201c3bf650de9900` |
| `invisiblocks` | `https://codeberg.org/tenplus1/invisiblocks.git` | `3abb767a8440b701b42460ff721dd21fc34f2db7` |
| `jumpdrive` | `https://github.com/mt-mods/jumpdrive` | `7799ffa62d6ad93aa666ad35d4eb76f51f6d2a01` |
| `livingnether` | `https://github.com/mt-mods/livingnether` | `3d4c278b86e632ec0c08f19e79e8529090dbe4bb` |
| `markers` | `https://github.com/Sokomine/markers` | `2aa828455862d939d293fb47ebb0fb6263055708` |
| `mg_villages` | `https://github.com/Sokomine/mg_villages` | `11dbd55a534dcce77235d94ba83753caba621fc0` |
| `mobs` | `https://codeberg.org/tenplus1/mobs_redo.git` | `8ba308a589456a6b959e38c13a8226dcf4aae4f5` |
| `mobs_animal` | `https://codeberg.org/tenplus1/mobs_animal.git` | `a0589dd0f26166570d3c085610699661ae8c91f0` |
| `mobs_npc` | `https://codeberg.org/tenplus1/mobs_npc.git` | `4d6096d7576a731aea6369fb8cf0448ca8070cd3` |
| `moretrees` | `https://github.com/mt-mods/moretrees` | `79ea6f7ce71ec7260a81c772df98fb2059673441` |
| `other_worlds` | `https://codeberg.org/tenplus1/other_worlds.git` | `411e997372fe8586ca7f310e57a9cfd4f029a0b0` |
| `prefab` | `https://github.com/mt-mods/prefab` | `71a2b0e2f8960afb02e53edb4fc461aeed6abf9b` |
| `promise` | `https://github.com/mt-mods/promise` | `823f15f3527e29b7a3bb53efb5e3debc6f74e12f` |
| `protector` | `https://codeberg.org/tenplus1/protector.git` | `d72ad456f024c3291e8590a9cdc90ac590d3cddc` |
| `signs_lib` | `https://github.com/mt-mods/signs_lib` | `897b30bce208ac54fcea73f92978785ad38830df` |
| `stairs` | `https://codeberg.org/tenplus1/stairs.git` | `3474fd6d14d9bc5608bfd78671795d0b96adaac5` |
| `stamina` | `https://codeberg.org/tenplus1/stamina.git` | `4b6988d09e13ed746046735f549d1ef7d6ff0b4b` |
| `unified_inventory_plus` | `https://github.com/mt-mods/unified_inventory_plus` | `836ebf5a172e752d5f17865874f5b04d60da3319` |
| `unifieddyes` | `https://github.com/mt-mods/unifieddyes` | `f7ea0d55b01ec14d6f9c001d0386afb5c1a141ee` |
| `xcompat` | `https://github.com/mt-mods/xcompat` | `758684dac8875d06d8c1565e323ee52c9d4daf7f` |

## Bereits zuvor bestaetigte Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `basic_materials` | `https://github.com/mt-mods/basic_materials` | `f626da067a39206b7d60c1122843cd951ffb7081` |
| `cartographer` | `https://codeberg.org/HuguesRoss/cartographer` | `c51eb2168bb6d22fb8921d040f253eb8871df7bd` |
| `lighting_monoid` | `https://github.com/t-affeldt/lighting_monoids` | `7ac833bb19127921fa9a8c6805b954a3581815a9` |
| `pipeworks` | `https://github.com/mt-mods/pipeworks` | `5dfd572eacee4c3c1ed8b827f4a67c46b022b242` |
| `lore` | `https://github.com/marghl/lore.git` | `93b8c9d79c1a55403d33b3dd9481e13477252fde` |
| `world_layers` | `https://github.com/marghl/world_layers.git` | `9f9e2aa5f2ff4a7b2cdc98f9e4b38fe5a2292fd9` |

## Bevorzugte Quellen, bewusst nicht ersetzt

Diese Checkouts erfuellen zwar die Autor-Praeferenz, der lokale Spielcode
stimmt aber mit keinem erreichbaren Commit ueberein oder das bevorzugte
Repository ist nicht belastbar erreichbar. Sie bleiben deshalb auf
`source = existing`:

| Checkout | Grund |
| --- | --- |
| `animalworld` | vier lokale Orang-Utan-Sounds fehlen in allen Commits des `mt-mods`-Repositories |
| `cottages` | lokaler Stand und aktuelles `Sokomine`-Repository besitzen deutlich verschiedene Code- und Verzeichnisstrukturen |
| `livingcavesmobs` | lokale Kollisionsbox in `moth.lua` weicht vom gesamten erreichbaren Repositoryverlauf ab |
| `livingjungle` | mehrere lokale Code-, Textur- und Uebersetzungsdateien weichen ab |
| `marinara` | erreichbares `TenPlus1`-Repository stimmt in 69 Dateien nicht mit dem lokalen Stand ueberein |
| `technic_plus` | kein belastbar erreichbares bevorzugtes Repository unter dem naheliegenden Paketnamen gefunden |

Alle nicht von `mt-mods`, `TenPlus1` oder `Sokomine` stammenden Kandidaten
wurden entsprechend der Vorgabe nicht weiter bearbeitet.
