# Mod-Inventar

Stand: 2026-11-01

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

- 116 reproduzierbare Git-Checkouts
- 25 unveraenderte Checkouts mit `source = existing`
- Git-Fetch und Synchronisierung ueber HTTPS
- Git-Push ueber eine separate SSH-`pushurl`
- vorherige Verzeichnisse der zuletzt vorgegebenen aktiven Checkouts unter
  `state/mods-backup/provided-active-2026-10-31/`
- vorherige Verzeichnisse der direkt vorgegebenen Repositories unter
  `state/mods-backup/provided-2026-10-31/`
- vorherige Verzeichnisse der aktuellen Runde unter
  `state/mods-backup/preferred-2026-10-31/`
- vorherige Verzeichnisse der `minetest-mods`-Runde unter
  `state/mods-backup/minetest-mods-2026-10-31/`
- vorherige Verzeichnisse der anhand von Maintainer-Hinweisen gefundenen Runde
  unter `state/mods-backup/hinted-2026-10-31/`
- vorheriges `3d_armor`-Verzeichnis unter
  `state/mods-backup/3d-armor-2026-10-31/`
- vorherige Verzeichnisse von `adaptation_modpack` und `morelights` unter
  `state/mods-backup/adaptation-morelights-2026-10-31/`
- vorherige Verzeichnisse der ersten Runde unter
  `state/mods-backup/confirmed-2026-10-31/`

## Anhand direkter Hinweise uebernommene Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `christmas` | `https://github.com/Extex101/christmas` | `dc3bfb042053259cc7900d68fda73a8c6d4d86f1` |
| `moretorches` | `https://github.com/Skandarella/moretorches` | `e1838a98f75e5d5c54d84bbed722e226a2c4e94c` |
| `mtzip` | `https://github.com/BuckarooBanzay/mtzip` | `1095e0f7aee72d0ce2ec906bec93bc07bb128db0` |
| `nextgen_bedrock` | `https://github.com/starninjas/nextgen_bedrock` | `13fd95be3bd83408840c4fb6668df79cddfb1345` |
| `ostereier` | `https://github.com/Ineva-A/ostereier` | `227d4dfec31314820e91ed514acb9fd75ce1904c` |
| `over_door_windows` | `https://github.com/TumeniNodes/over_door_windows` | `979b4304d871a0a017b3a1d8774e7d4d56954717` |
| `placeholder` | `https://github.com/BuckarooBanzay/placeholder` | `51735a19e5903b92c3a7d5ee77d264e415627ed2` |
| `regional_weather` | `https://github.com/t-affeldt/regional_weather` | `e1616762104d1fae38c9974d95d64592cb5d5561` |
| `steampunk_blimp` | `https://github.com/APercy/steampunk_blimp` | `0e6fb3ff773c9b782fc83bfb3630fd921f8c982a` |
| `tape_measure` | `https://github.com/OgelGames/tape_measure` | `562fc127742165b116f1fcec995e9c9537073899` |
| `tinted_glass` | `https://github.com/C-C-Minetest-Server/tinted_glass` | `bd5783f82ee6f0fc0de113199d002d9034ba5cba` |
| `tubelib2` | `https://github.com/joe7575/tubelib2` | `29edfd69e93d1cbdacdc32897c68d5e30de13d2b` |
| `vines` | `https://github.com/bas080/vines` | `e41377aa90d091dbae520751165052880b95ce28` |
| `worldedit` | `https://github.com/Uberi/Minetest-WorldEdit` | `62ffafe3bcb386600c431ef3840d91c3c8f85639` |
| `wrench` | `https://github.com/mt-mods/wrench` | `b8079abcf7c303e18f0c140c997fb5a6f76851b6` |
| `xdecor` | `https://codeberg.org/Wuzzy/xdecor-libre` | `43a77535eab1148937e4b2ea1263d2a60700e362` |

`prefab` war bereits auf das angegebene `mt-mods`-Repository gepinnt. Das
zuvor in `technic_plus` enthaltene `wrench` wurde auf den inhaltsgleichen
Commit `b8079abcf7c303e18f0c140c997fb5a6f76851b6` aus dem eigenstaendigen
Repository `mt-mods/wrench` umgestellt. `concrete`, der zweite Mod aus
`technic_plus`, wurde deaktiviert.

## Zuvor anhand direkter Hinweise uebernommene Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `airutils` | `https://github.com/APercy/airutils` | `5c21c9249a5de3e976fb2720d34b04f7a969233d` |
| `blockexchange` | `https://github.com/blockexchange/blockexchange` | `9820672d5d6e32ac9efbfb87479ca1d0503d7345` |
| `bucket_wooden` | `https://gitlab.com/h2mm/wooden_bucket` | `0203ec94fc1e36a86d4dbb5e5b64ffeb6882db57` |
| `climate_api` | `https://github.com/t-affeldt/climate_api` | `85e4553f2aa0a98b093141e29576e347f9b13e76` |
| `composting` | `https://github.com/sfence/composting` | `91a4b0d318a0db6676b969732791887ea366b7c1` |
| `cottages` | `https://github.com/C-C-Minetest-Server/cottages` | `3fd1977b6d72f25633d7773f73cc7f2e3aed433e` |
| `darkage` | `https://github.com/adrido/darkage` | `494f81c37593ec21f803bbcced70dcdc3e95a045` |
| `dialog_redo` | `https://github.com/MT-Companion/dialog_redo` | `63690ceef042a6ca3d262666a10ceb562b5c3f4f` |
| `digicontrol` | `https://github.com/OgelGames/digicontrol` | `85c71f9f6cfa2fcb9b16c73d3d5954e1872bb391` |
| `doc` | `https://codeberg.org/Wuzzy/minetest_doc` | `a713574f227f17e7f8b4be569d969031766d24fc` |
| `elevator` | `https://github.com/tigris-mt/elevator` | `9d3c23fad754409b33305dacd40deb0a6ad43aec` |
| `epic` | `https://github.com/buckaroobanzay/epic` | `8c207629fdc6234a57e7d66272caa373c6b8b57e` |
| `fakelib` | `https://github.com/OgelGames/fakelib` | `562dc359f00227daf0ee56dbba9c36a240c59d4c` |
| `hunger_ng` | `https://git.0x7be.net/dirk/hunger_ng` | `7b2cfc0fb1e0cdea5e6e9e48f98829b8d623ded4` |
| `leafstride` | `https://github.com/EmptyStar/leafstride` | `5db4b4a60b6f91522e1a0b19709a436e37641f98` |
| `luanti_utils` | `https://github.com/bas080/luanti_utils` | `bc4f2a885f413b0f76b71b80274507e96cb40772` |
| `minecart` | `https://github.com/joe7575/minecart` | `3fb88ace3d3cb170f2624f01eabb7043163bb262` |
| `moretools` | `https://github.com/sfence/moretools` | `ade5fc43559ac7fd0ec1439c19347e8cb58706da` |

Die lokalen Inhalte dieser Checkouts wurden vor der Umstellung mit den
angegebenen Commits verglichen. Bei `digicontrol` und `fakelib` enthaelt das
Repository lediglich zusaetzliche Entwicklungsdateien, die im installierten
ContentDB-Paket fehlen.

## Weitere anhand direkter Hinweise uebernommene Checkouts

| Checkout | Repository | Commit |
| --- | --- | --- |
| `adaptation_modpack` | `https://github.com/sfence/adaptation_modpack` | `3fc5886b0c743a6c8b32a210fe9ba4b3881ef07e` |
| `morelights` | `https://github.com/random-geek/morelights` | `f4aa82a31e8d479b3b16ad6766d15370c1fec729` |
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
| `professions` | `https://github.com/marghl/professions.git` | `96addcfdb35a17d3512e42ee8feaf1e22816492c` |
| `world_layers` | `https://github.com/marghl/world_layers.git` | `9f9e2aa5f2ff4a7b2cdc98f9e4b38fe5a2292fd9` |

## Bevorzugte Quellen, bewusst nicht ersetzt

Diese Checkouts erfuellen zwar die Autor-Praeferenz, der lokale Spielcode
stimmt aber mit keinem erreichbaren Commit ueberein oder das bevorzugte
Repository ist nicht belastbar erreichbar. Sie bleiben deshalb auf
`source = existing`:

| Checkout | Grund |
| --- | --- |
| `animalworld` | vier lokale Orang-Utan-Sounds fehlen in allen Commits des `mt-mods`-Repositories |
| `livingcavesmobs` | lokale Kollisionsbox in `moth.lua` weicht vom gesamten erreichbaren Repositoryverlauf ab |
| `livingjungle` | mehrere lokale Code-, Textur- und Uebersetzungsdateien weichen ab |
| `marinara` | erreichbares `TenPlus1`-Repository stimmt in 69 Dateien nicht mit dem lokalen Stand ueberein |
| `technic_plus` | kein belastbar erreichbares bevorzugtes Repository unter dem naheliegenden Paketnamen gefunden |

Alle nicht von `mt-mods`, `TenPlus1` oder `Sokomine` stammenden Kandidaten
wurden entsprechend der Vorgabe nicht weiter bearbeitet.
