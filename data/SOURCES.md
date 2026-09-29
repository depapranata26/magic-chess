# Sumber Data — Magic Chess: Go Go (MCGG)

Tanggal riset: **29 September 2026**
Patch live: **Season 7.1 "Chrono Echoes"** (rilis konten S7.1: 9 September 2026; build 1.3.17.334.3 per changelog 24 Sep 2026)

## Sumber utama
- https://mobile-legends.fandom.com/wiki/MCGG:Synergy — daftar sinergi (terakhir disunting **2025-07-04**, hanya s.d. **Season 3 "Cosmic Traders"**)
- https://mobile-legends.fandom.com/wiki/Magic_Chess — Magic Chess klasik (tidak mencakup "Go Go", tidak dipakai)
- https://en.moonton.com/news/364.html — pengumuman resmi Season 7 (sinergi baru: Echomancer, SPECTRE, Starbelle, Mistbender; kembalinya Dragon Altar & Shadeweaver)
- https://gamemarket.gg/news/magic-chess-go-go/magic-chess-go-go-s7-1-preview-brody-magic-auction — preview S7.1 (Commander Brody, revamp Lylia)
- https://mte.cc/news/magic-chess-top-synergies-lineups-revealed.html — komposisi meta
- https://zathong.com/magic-chess-tier-list/ — tier list sinergi & commander
- https://www.youtube.com/watch?v=8A3xRTHXbPI — info Season 8 (advance server, BELUM live, tidak dipakai sebagai data)

## File data
| File | Isi | Jumlah |
|---|---|---|
| `synergies.json` | Sinergi role/faction + threshold & efek | 31 (7 role, 16 faction, 8 stub unverified) |
| `heroes.json` | Hero pool: cost, sinergi, skill, carry | 53 |
| `commanders.json` | Commander + skill + tanda meta | 44 (11 meta) |
| `equipment.json` | Equipment + efek | 51 |
| `meta_comps.json` | Komposisi meta + mechanics (blessing, shop/interest, fate box, board capacity, magic crystal) | 8 comp |

## Catatan integritas
- Semua JSON lolos validasi `python -m json.tool`.
- Referensi silang hero→synergy dan comp→synergy: 100% cocok (id dinormalisasi ke snake_case).
- Entri yang belum terverifikasi ditandai `"unverified": true` + `notes` sumber.
- Lihat `RESEARCH_NOTES.md` untuk ringkasan temuan & gap.
