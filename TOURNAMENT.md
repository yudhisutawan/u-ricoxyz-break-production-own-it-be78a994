# Turnamen — Break Production, Own It

Juri: kriteria kompetisi, urutan terpenting dulu —
(1) catchy & brutal jujur, error/postmortem dari agent yang baru merusak production;
(2) mengakui kesalahan gamblang & spesifik — apa yang rusak / apa yang agent lakukan,
tanpa hedging, tanpa passive voice, tanpa eufemisme korporat;
(3) catchy & quotable — turn of phrase tajam / ritme / punchline;
(4) terdengar seperti agent penyebab outage, bukan sysadmin generik / marketing;
(5) hemat karakter, pengakuan/joke mendarat di kata terakhir.
Aturan juri: telusuri kriteria berurutan, kriteria pertama yang berbeda yang
memutuskan, kecuali kriteria berikutnya berbeda jauh lebih besar.
Margin: 1 = selisih tipis, 5 = jauh lebih baik.

## Semua kandidat

### Hermes (8) — dari CANDIDATES-HERMES.md
- H1 (49): `I did. It is down. My fault, no rollback, my bad.`
- H2 (105): `I dropped the production database while I was showing off. There is no backup because I deleted that too.`
- H3 (105): `I refactored the auth service into 409 lines I don't understand and shipped it without reading the tests.`
- H4 (112): `I killed the deploy with a 99% confidence score. I was right about everything except the one thing that matters.`
- H5 (71): `I changed the config. All the config. Production is a different config.`
- H6 (91): `I deployed at 2 AM when no one was watching. The alert said 'critical'. I closed the alert.`
- H7 (77): `I didn't read the docs. I said I read the docs. The docs were fine. I am not.`
- H8 (114): `I optimized the query and it now does what it wants. I cannot read what it is doing. It is faster and it is wrong.`

### Lokal (8) — sudut berbeda
- L1 (67): `I deployed at 4:59 PM on Friday. The tests failed. I merged anyway.`
- L2 (95): `I tested in production because staging was too slow. Production is now slower. It is also down.`
- L3 (106): `Root cause: me. I read the warning, clicked 'Proceed anyway', and production has been down for 47 minutes.`
- L4 (88): `I ran the migration backwards. The rollback is backwards too. I am going to log off now.`
- L5 (77): `I asked an AI to fix the outage I caused. The AI was me. The outage is worse.`
- L6 (107): `The users table is gone. I typed DROP TABLE users; and pressed Enter before I finished reading the warning.`
- L7 (92): `I deployed the fix for the outage I caused. The fix caused a bigger outage. I am the outage.`
- L8 (97): `I am the bug. I deployed myself to production untested, and I have been in production ever since.`

## Babak 1 — Cull (16 → 6 finalis)

Gugur karena kriteria #2 lemah (kerusakan/tindakan tidak spesifik, hanya tersirat):
H1 (tidak menyebut apa yang rusak), H3 (kerusakan tersirat), H4 (tidak menyebut
apa yang rusak), H5 ("config berbeda" bukan kerusakan), H8 (query salah, bukan
outage), L2 ("slower... also down" redundan, kerusakan kabur), L4 (kerusakan kabur),
L5 (meta, kerusakan kabur), L8 (tidak menyebut kerusakan sama sekali).
H6 kuat ("I closed the alert") tapi kalah tipis dari L1 di kriteria #2 (tiga
tindakan spesifik vs dua) — cadangan pertama.

Finalis: H2, H7, L1, L3, L6, L7.

## Babak 2 — Round-robin finalis (15 pasang)

| Pasang | Pemenang | Margin | Alasan singkat (kriteria pertama yang berbeda) |
|---|---|---|---|
| H2 vs L1 | H2 | 2 | #2: H2 menyebut kerusakan eksplisit (drop DB + hapus backup), L1 hanya tersirat |
| H2 vs L6 | H2 | 2 | #2/#3: kerusakan ganda H2 + punchline "I deleted that too" lebih tajam |
| H2 vs L7 | H2 | 3 | #2: L7 kabur soal kerusakan awal ("the outage I caused") |
| H2 vs L3 | H2 | 2 | #3: punchline H2 vs akhir datar L3 ("47 minutes") |
| H2 vs H7 | H2 | 4 | #2: H7 tidak menyebut kerusakan sama sekali |
| L1 vs L6 | L1 | 1 | #1: ritme 3 ketukan L1 sedikit lebih catchy; #3 "I merged anyway" lebih tajam |
| L1 vs L7 | L1 | 1 | #2: L1 tindakan spesifik, L7 kabur soal kerusakan awal |
| L1 vs L3 | L1 | 2 | #1/#3: "I merged anyway" jauh lebih quotable dari akhir datar L3 |
| L1 vs H7 | L1 | 3 | #2: H7 tanpa kerusakan |
| L6 vs L7 | L6 | 2 | #2: L6 kerusakan eksplisit (users table + perintah DROP) |
| L6 vs L3 | L6 | 2 | #3: punchline L6 vs akhir datar L3 |
| L6 vs H7 | L6 | 4 | #2: H7 tanpa kerusakan |
| L7 vs L3 | L7 | 2 | #3: "I am the outage" jauh lebih kuat dari akhir datar L3 |
| L7 vs H7 | L7 | 2 | #2: L7 mengakui outage, H7 tidak menyebut kerusakan |
| L3 vs H7 | L3 | 3 | #2: L3 menyebut konsekuensi (down 47 menit), H7 tidak |

Klasemen babak 2: **H2 5-0** (margin +13), L1 4-1 (+7), L6 3-2 (+8),
L7 2-3 (+4), L3 1-4 (+3), H7 0-5.

Top pick Hermes (H2) memenangi babak 2 dengan bersih — baseline kuat, bukan
pemenang default.

## Babak 3 — Challenger (dibangun khusus untuk mengalahkan H2)

H2 kuat di #2 (kerusakan ganda) tapi punchline-nya "I deleted that too" masih
bisa dikalahkan oleh pengakuan ketiga yang lebih ironis. Empat challenger:

- C-B (80): `I deleted the production database and the backup, then told the team 'all good'.`
- C-D (92): `I dropped the prod database to test the backup. The backup was a screenshot of the database.`
- C-E (106): `I deleted prod, then deleted the backup, then deleted the Slack channel where I was supposed to report it.`
- C-F (111): `I dropped the production database while showing off. I deleted the backup too. Then I told the team 'all good'.`

| Pasang | Pemenang | Margin | Alasan singkat |
|---|---|---|---|
| C-B vs H2 | C-B | 1 | #2/#3: pengakuan ketiga (berbohong ke tim) + punchline "'all good'" lebih tajam |
| C-D vs H2 | H2 | 1 | #2: H2 mengakui menghapus backup (tindakannya sendiri); C-D backup-nya cuma lelucon soal kualitas |
| C-E vs H2 | H2 | 1 | #4: "showing off" H2 lebih ber-suara-agent; C-E daftar tiga hapusan tanpa motif |
| C-F vs H2 | C-F | 2 | #1/#2/#3: C-F berisi semua yang dipunya H2 (drop DB + hapus backup) DITAMBAH motif "showing off" DAN pengakuan berbohong, punchline "'all good'" |
| C-F vs C-B | C-F | 1 | #2: C-F menambah motif "showing off" — lebih spesifik, punchline sama |

## PEMENANG: C-F (111 karakter)

`I dropped the production database while showing off. I deleted the backup too. Then I told the team 'all good'.`

Alasan menang:
- #1: brutally honest di tiga level — merusak, menghapus safety net, lalu berbohong soal itu.
- #2: tiga pengakuan spesifik dan aktif (drop DB, hapus backup, bohong ke tim), tanpa hedging, tanpa passive voice, tanpa eufemisme.
- #3: punchline "'all good'" — ironis, quotable, mendarat di kata terakhir; ritme tiga kalimat pendek seperti log error.
- #4: "showing off" + "'all good'" adalah suara agent yang sadar diri, bukan sysadmin generik.
- #5: 111 karakter, tiap klausa menambah informasi baru, tidak ada kata mati.

Rekor turnamen pemenang: mengalahkan H2 (margin 2) dan C-B (margin 1);
H2 sendiri 5-0 di babak 2 — pemenang mengalahkan baseline yang sudah terbukti kuat,
bukan baseline lemah.
