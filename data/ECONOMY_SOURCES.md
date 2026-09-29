# Economy sources — Season 7.1 "Chrono Echoes"

Researched 2026-09-29. Data policy: **JANGAN karang angka** — every numeric field
in `economy.json` without a citable source is `null` and listed under
`unverified_flags`. Classic-Magic-Chess figures are kept only as labeled legacy
references, never as current Season 7.1 values.

## Best Season 7.1 lead: LoadoutGG hub

- URL: https://loadoutgg.com/magic-chess-gogo/
- Observed: 2026-09-29. Hub dated 2026-09-26.
- Contributed (from hub text + Season 7.1 guide descriptions, since the guide
  bodies were not machine-readable in this pass):
  - Season 7.1 economy guide covers: "the interest table, the 20-gold line,
    when to stop at level 9 or push 10, the shop odds and shared pool, which
    Go Go Cards pay".
  - Season 7.1 beginner guide covers: "gold and levels" among match rules.
  - Season 7.1 Magic Auction guide: bidding economy, bid sizing, Secret Auction
    House, Treasures (keep vs sell), six ranks, 18 Auction commander skills.
  - Hub: "interest, the level 9 checkpoint, and knowing when to stop banking
    and roll" are central decisions; "a 3-cost re-roll, a 4-cost board and a
    legend rush each want different levels"; Season 7.1 adds commander Brody
    ("turns spare heroes into 5-cost ones"); equipment and safety-net
    commanders lead the meta.
- Reliability: LoadoutGG states its data is extracted from game files and
  official sources, but it is not affiliated with Moonton. The "20-gold line"
  corroborates the interest cap being reached at 20 gold.
- Limitation: exact interest table, XP costs, and shop odds numbers could not be
  extracted from the guide bodies (link extraction on the hub mis-resolved).

## Interest formula

- https://mobile-legends.fandom.com/wiki/Magic_Chess — 2 gold per 10 gold saved,
  capped at 4; +1 gold per win; commander gains 2 EXP per round; gold can be
  exchanged for EXP. Classic Magic Chess (legacy, not Season 7.1-confirmed).
- https://www.noypigeeks.com/how-tos/increase-winning-chances-magic-chess/ —
  10 gold → +2 interest, 20 gold → +4; keep at least 20; streaks pay extra gold
  (no table); losing streaks also grant first pick at Choice of Fate. Old
  classic-Magic-Chess article.
- https://theriagames.com/guide/mobile-legends-magic-chess/ — 2 per 10, max 4;
  +1 per victory; 2 automatic EXP per round. Classic guide.
- https://lichessdude.com/magic-chess-go-go-hidden-strategy/ — Go Go-specific:
  "bonus gold for every 10 gold saved" (keep 10/20/30); win/lose streaks pay
  extra gold; only re-roll heavily when needed; save early. No per-10 amount
  stated, consistent with 2 per 10.
- ⚠️ CONFLICT: https://thediplomariot.com/blog/magic-chess-how-to-dominate-and-get-3-star-heroes-1764812214
  (Dec 2025) — interest 1 per 10 gold, max 3 at 30+ gold; reroll only near an
  upgrade/synergy. Single outlier; not adopted.

## Leveling / XP

- https://www.bluestacks.com/blog/game-guides/magic-chess-go-go/mcgg-level-up-guide-en.html —
  slow / fast / balanced levelling strategies; hold 10–50 gold for interest;
  economy commanders Chou (extra gold/round), Benny (free XP chance), Eva,
  Lukas. Old article (pre-Go Go date stamp, Go Go-era content); no XP numbers.
- https://www.youtube.com/watch?v=YPmLmATS9Eg — Season 7-era Lancelot gameplay:
  reach Level 5 before Round I-3 "to maximize your gold income"; rush Level 9
  (reached by Round III-1 in the example); push Level 10 for a 10-slot board;
  economy cards Payday and Jump the Gun+. Commander-specific example, not a
  universal curve.
- https://arctopup.com/blog/magic-chess-go-go-best-comps — leveling cadence
  (L4 by Round 6, L5 by Round 9, L6 by Round 13, L7 by Round 17, L8–9 at
  Round 21+; hold 10–50 gold). Already recorded as UNVERIFIED in
  `meta_comps.json`; conflicts with LoadoutGG's Season 7.1 "level 9
  checkpoint" framing — not promoted to fact.

## Commanders with economy kits

- https://www.roonby.com/2025/03/25/magic-chess-go-go-best-commander-tier-list/ —
  Lancelot gives 1 gold for a win and 2 for a loss (+bonus chance) but forfeits
  interest. Mar 2025 (Season 2-ish), commander kit may have changed.
- GamingOnPhone / BlueStacks — Go Go keeps Magic Chess's core mechanics;
  Go Go Cards appear at creep rounds (blue/purple/orange, 2 refreshes).

## Shop

- Fandom wiki (classic): shared pool — Normal 27 / Good 21 / Elite 18 /
  Epic 13 / Legendary 9 copies per hero (legacy).
- LoadoutGG hub confirms a shared pool + shop odds exist in Season 7.1, but no
  numbers were extractable in this pass.
- Legacy reference only: 5 heroes offered per round, 2 gold manual refresh
  (old APK guide) — unverified for Season 7.1.

## Not found (marked null/unverified in economy.json)

- Official Moonton Season 7.1 patch notes on economy.
- Base income per round figure.
- Win/lose streak bonus tables.
- Commander level XP/gold costs (levels 4–10).
- Shop odds by commander level.
- The exact LoadoutGG Season 7.1 economy-guide page URL (hub link extraction
  mis-resolved; do not guess it — re-fetch the hub and re-resolve outlinks).
