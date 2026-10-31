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

- 79 reproduzierbare Git-Checkouts
- 60 unveraenderte Checkouts mit `source = existing`
- Git-Fetch und Synchronisierung ueber HTTPS
- Git-Push ueber eine separate SSH-`pushurl`
- vorherige Verzeichnisse der aktuellen Runde unter
  `state/mods-backup/preferred-2026-10-31/`
- vorherige Verzeichnisse der `minetest-mods`-Runde unter
  `state/mods-backup/minetest-mods-2026-10-31/`
- vorherige Verzeichnisse der anhand von Maintainer-Hinweisen gefundenen Runde
  unter `state/mods-backup/hinted-2026-10-31/`
- vorheriges `3d_armor`-Verzeichnis unter
  `state/mods-backup/3d-armor-2026-10-31/`
- vorherige Verzeichnisse der ersten Runde unter
  `state/mods-backup/confirmed-2026-10-31/`

## Anhand von Maintainer-Hinweisen uebernommene Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `postool` | `https://github.com/SwissalpS/postool` | `0dc16fd9d7784f742657f8bfd0aac6c0ba3f17b7` |
| `scifi_nodes` | `https://github.com/D00Med/scifi_nodes` | `2eb584147218f59262fdb035f6af5810dda675bb` |
| `vizlib` | `https://github.com/OgelGames/vizlib` | `690402e1f54cd7e4262e16dc64a47770f15bed25` |
| `metatool` | `https://github.com/S-S-X/metatool` | `638768f198718e156f6427bc3d79e4b90112b211` |

`metatool` enthaelt auch `containertool`, `luatool`, `magic_pen`, `sharetool`
und `tubetool`. `replacer` war bereits zuvor als eigener Checkout gepinnt.

## Aus `minetest-mods` uebernommene Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `3d_armor` | `https://github.com/minetest-mods/3d_armor` | `a4f311cbcf8125b4b83ba884d1d0d12f018021da` |
| `anvil` | `https://github.com/minetest-mods/anvil` | `9bc6f63af822269c16db69cc0f8e4710207aa1a7` |
| `areas` | `https://github.com/minetest-mods/areas` | `0dc1c67fff21142e6f2081a9280a6b63d65b4901` |
| `digilines` | `https://github.com/minetest-mods/digilines` | `3f6e553b7c7fe7017a96527b9cb26f367cb6f8b7` |
| `drawers` | `https://github.com/minetest-mods/drawers` | `5c8aa86f481852cc59b678023193135d5ab9963d` |
| `mesecons` | `https://github.com/minetest-mods/mesecons` | `aca87dbd448637d2dc80e59e909425932acd6c84` |
| `moreblocks` | `https://github.com/minetest-mods/moreblocks` | `8c3de6c948f07d589fe92c2c96628b843cba28b6` |
| `moreores` | `https://github.com/minetest-mods/moreores` | `73c8696c82ab43d36560d3818ca105d9773c8461` |
| `pkarcs` | `https://github.com/minetest-mods/pkarcs` | `f26a3dc2361b4e6e2bd2e5670b5f6cd0f64c9225` |
| `player_monoids` | `https://github.com/minetest-mods/player_monoids` | `bd082d25dae879fb3fabe4d9b518685b94679275` |
| `pontoons` | `https://github.com/minetest-mods/pontoons` | `a9fbd4028f5b111d57c41147d460b29fbe27f897` |
| `spawn_command` | `https://github.com/minetest-mods/spawn_command` | `78af69d4e16067a3b3697160ad9f4df099f0e5f6` |
| `towercrane` | `https://github.com/minetest-mods/towercrane` | `7106c56a9807c9ec7781ed9460a7c77a2c6754f5` |
| `unified_inventory` | `https://github.com/minetest-mods/unified_inventory` | `3679debe1404fd04b5a8ef3b585ac18bb5ccc60e` |
| `unifiedbricks` | `https://github.com/minetest-mods/unifiedbricks` | `b6e70bcb5999d73d934d16a6fb12fc48bd9020fb` |
| `woodcutting` | `https://github.com/minetest-mods/woodcutting` | `b265a9707a1ea60e0ecc79ab6da808a300ca2dff` |

## Aus der bevorzugten ContentDB-Runde uebernommene Checkouts

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
