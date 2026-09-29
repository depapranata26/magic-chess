# Catatan Riset — Magic Chess: Go Go, Season 7.1 (Chrono Echoes)

Tanggal: 29 September 2026.

## Ringkasan
- Patch live: **Season 7.1 "Chrono Echoes"** (S7.1 rilis 9 Sep 2026: Commander baru **Brody** dengan Abyss Domain, revamp **Lylia** "Little Witch's Shop"; build 1.3.17.334.3).
- **31 sinergi** terdokumentasi: 7 role (Bruiser, Dauntless, Mage, Marksman, Scavenger, Stargazer, Weapon Master), 16 faction, 4 sinergi baru S7 bertipe unknown (Echomancer, SPECTRE, Starbelle, Mistbender).
- **53 hero** di pool (1-gold: 8, 2-gold: 11, 3-gold: 12, 4-gold: 12, 5-gold: 9, 7-gold: 1 — **Alpha**, hero 7-gold pertama, didapat via Hero Chain SPECTRE setelah Alice bintang 2, bukan dari shop).
- **44 commander** (11 bertanda meta: Layla, Zilong, Kagura, Nana, Chou, Guinevere, Popol and Kupa, Lylia, Moskov, Kalea, Luo Yi).
- **51 equipment** + mekanik (blessing +1 synergy count, shop/interest, Fate Box/Go Go Box, board capacity = commander level 3–9, Choice Magic Crystal S7).
- **8 komposisi meta** (semua `unverified: true` — dari guide/video, sebagian board/item tidak lengkap di sumber).

## Temuan penting
1. **Wiki Fandom tidak punya data Season 7.** Halaman MCGG:Synergy terakhir disunting 2025-07-04 dan hanya s.d. Season 3 "Cosmic Traders". Threshold/efek sinergi di file ini = angka Season 3 dari wiki (verbatim, tidak diubah).
2. **4 sinergi baru S7** (Echomancer, SPECTRE, Starbelle, Mistbender) hanya ada deskripsi konsep dari pengumuman resmi Moonton — threshold & efek resmi tidak dipublikasikan; bertipe `"unknown"`, tanpa threshold.
3. **8 sinergi stub** (`astro_power`, `defender`, `dragoncaller`, `enchanted_tales`, `kishin`, `necrokeep`, `swordsman`, `swiftblade`): direferensikan oleh hero pool/komposisi S7 dari artikel & guide, tapi tidak ada di wiki → `unverified: true`, tanpa threshold.
4. **Dragon Altar & Shadeweaver** kembali di S7 (dari Season 1–2); angka Dragon Altar di file = versi Season 2 wiki (2/4/6/10), kemungkinan di-rework di S7.
5. **Alpha (7 gold)**: bukan unit shop normal; sinergi kedua belum terkonfirmasi.

## Belum terverifikasi (prioritas untuk refresh berikutnya)
- Threshold & efek resmi ke-4 sinergi baru S7 (Echomancer, SPECTRE, Starbelle, Mistbender).
- Threshold/efek S7 untuk 8 sinergi stub + Dragon Altar/Shadeweaver versi S7.
- Skill **28 dari 44 commander** (data lama 2025 / halaman wiki 403 / placeholder).
- 16 Magic Crystal = daftar legacy pra-S7; mekanik lengkap Choice Magic Crystal S7 belum terkonfirmasi.
- 5 dari 8 meta comp berasal dari video creator tanpa board/item rinci; 2 comp ("6 Stargazer 3 Necrokeep", "6 Dragon Altar 4 Swordsman") memuat hero yang tidak ada di pool S7.1 (kemungkinan dari guide Magic Chess klasik) — ditandai di `notes` tiap comp.
- Nama skill 9 hero kosong (Paquito, Alice, Uranus, Aldous, Nana, Dyrroth, Angela, Lunox, Karina); cost Cici/Miya & Karina/Luo Yi hasil keputusan antar-sumber yang konflik (tercatat di `notes` tiap hero).
- Season 8 sudah di advance server (bukan live) — jangan pakai datanya sampai rilis resmi.

## Keputusan normalisasi (koordinator)
- Semua synergy id memakai `snake_case` (wiki memakai hyphen pada sebagian: `dragon-altar` → `dragon_altar`, dst.).
- `key_synergies` pada 3 comp diisi dari parsing nama comp ("6 Kishin 3 Phasewarper 3 Shadeweaver" → kishin:6, dst.); comp tanpa angka di nama dibiarkan tanpa key.
