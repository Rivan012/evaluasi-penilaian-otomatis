---
version: alpha
name: EduFuzzy ITS
description: Pedoman desain visual sistem evaluasi short-answer interaktif, memadukan nuansa dark mode presisi dengan estetika akademik modern yang bebas visual slop.
colors:
  primary: "#6D28D9"
  primary-hover: "#5B21B6"
  accent: "#0284C7"
  accent-hover: "#0369A1"
  bg-base: "#0B0813"
  bg-surface: "#171226"
  bg-surface-elevated: "#231B38"
  border: "#3B2D59"
  border-subtle: "#2A2040"
  text-main: "#F8FAFC"
  text-muted: "#94A3B8"
  text-inverse: "#FFFFFF"
  status-success: "#10B981"
  status-warning: "#F59E0B"
  status-danger: "#EF4444"
typography:
  h1:
    fontFamily: "Space Grotesk"
    fontSize: "2.25rem"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  h2:
    fontFamily: "Space Grotesk"
    fontSize: "1.5rem"
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body-md:
    fontFamily: "Space Grotesk"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.5
  body-sm:
    fontFamily: "Space Grotesk"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.4
rounded:
  sm: "6px"
  md: "10px"
  lg: "16px"
  full: "9999px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "16px"
  lg: "24px"
  xl: "32px"
components:
  card:
    backgroundColor: "{colors.bg-surface}"
    textColor: "{colors.text-main}"
    rounded: "{rounded.lg}"
    padding: "24px"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.text-inverse}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.text-inverse}"
    rounded: "{rounded.md}"
    padding: "12px 20px"
  input-field:
    backgroundColor: "{colors.bg-surface-elevated}"
    textColor: "{colors.text-main}"
    rounded: "{rounded.md}"
    padding: "12px 16px"
---

## Overview

EduFuzzy ITS dirancang untuk memberikan pengalaman evaluasi jawaban esai pendek yang fokus, ilmiah, dan memotivasi tanpa distraksi ornamen berlebih (*anti-slop*). Desain berakar pada tipografi geometris yang tegas, fondasi warna gelap dengan kontras rasio tinggi (WCAG AA), dan aksen terukur untuk memperjelas umpan balik evaluasi.

## Colors

- **Deep Space Base (`#0B0813`)**: Latar belakang utama aplikasi yang minim silau dan nyaman untuk sesi belajar panjang.
- **Surface Layer (`#171226`) & Elevated (`#231B38`)**: Menegaskan hierarki visual kartu modul tanpa mengandalkan efek blur berlebihan.
- **Royal Violet (`#6D28D9`)**: Warna primer penanda aksi utama pengerjaan soal dan tombol interaksi sentral.
- **Cyan Accent (`#0284C7`)**: Penanda status data metrik (XP, perolehan level, dan skor rasio).
- **Feedback State**:
  - `status-success` (`#10B981`): Predikat Sangat Baik ($\ge 80$).
  - `status-warning` (`#F59E0B`): Predikat Cukup ($60 - 79$).
  - `status-danger` (`#EF4444`): Predikat Perlu Perbaikan ($< 60$).

## Typography

Menggunakan **Space Grotesk** sebagai tipe huruf tunggal untuk menjaga konsistensi karakter teknis dan keterbacaan:
- **Headings (H1 & H2)**: Menggunakan negative letter-spacing (`-0.02em` s.d. `-0.01em`) untuk menciptakan hierarki yang padat dan terstruktur.
- **Body Text**: Line-height $1.5$ dengan kontras warna terang `#F8FAFC` untuk teks aktif dan `#94A3B8` untuk label pendukung/metadata.
- Tidak menggunakan uppercase ekstrim pada paragraf atau heading deskriptif.

## Layout

- **Sistem Grid Terukur**: Lebar kontainer aplikasi dibatasi maksimal `1120px` agar pengerjaan soal dan pembacaan feedback tetap terfokus di tengah viewport.
- **Rhythm & Hierarchy**: Margin antar seksi konsisten pada skala `32px` (`xl`), sedangkan relasi elemen dalam form kuis terikat pada `16px` (`md`).
- **Mobile First Adaptation**: Menumpuk kartu pertanyaan dan hasil evaluasi secara vertikal pada breakpoint $< 768px$ dengan tap target minimum $44\text{px}$.

## Elevation & Depth

- Kedalaman diproyeksikan melalui kontras warna bidang bertingkat (`bg-base` $\to$ `bg-surface` $\to$ `bg-surface-elevated`), bukan bayangan tebal yang kabur.
- Shadow halus digunakan eksklusif pada kartu evaluasi aktif: `box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.5)`.
- Menghindari pemakaian glow neon berulang pada semua sudut elemen.

## Shapes

- **Radius Terstruktur**:
  - `sm` (`6px`): Badge kecil, indikator progres, dan badge rank.
  - `md` (`10px`): Input field, textarea jawaban, dan tombol aksi.
  - `lg` (`16px`): Kartu wadah pertanyaan, ringkasan skor, dan tabel leaderboard.
  - `full` (`9999px`): Avatar kapsul dan chip filter kategori.

## Components

- **Soal & Input Jawaban**: Bidang textarea yang lapang dengan border kontras statis `#3B2D59` yang beralih lembut ke `#6D28D9` saat `:focus`.
- **Feedback & Score Card**: Hasil evaluasi instan memisahkan skor numerik besar di sisi kiri dengan umpan balik ITS di sisi kanan.
- **Leaderboard Table**: Striping baris tabel minim garis dengan badge posisi (Rank 1–3 diberi aksen khusus, rank lainnya netral).

## Do's and Don'ts

### Do's
- Gunakan warna status (hijau/kuning/merah) hanya ketika menandakan hasil evaluasi skor atau validasi sistem.
- Pastikan teks kunci jawaban pembanding disajikan secara jelas dengan latar kontras tinggi agar siswa mudah membaca perbaikan konsep.
- Jaga interaksi tombol tetap responsif dengan state hover/active yang jelas.

### Don'ts
- Jangan menambahkan animasi pulse atau rotasi terus-menerus tanpa pemicu aksi pengguna.
- Jangan menggunakan efek glassmorphism blur di seluruh kontainer secara serentak.
- Jangan memasukkan emoji dekoratif berlebihan pada judul soal atau label resmi sistem.
