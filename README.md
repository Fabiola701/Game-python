# Game-python
# Final Project Computer Programming
# 🎮 NEON ASCENT: Protokol Peninggalan Cyber

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-success.svg)]()

> Sebuah text-based RPG bertemakan cyberpunk yang dimainkan di terminal. Jelajahi dunia neon, kuasai kekuatan cyber, dan temukan Peninggalan yang hilang sebelum megakorporasi OmniCore mendapatkannya!

---

## 📖 Daftar Isi

- [Tentang Proyek](#-tentang-proyek)
- [Fitur Utama](#-fitur-utama)
- [Struktur Data yang Digunakan](#-struktur-data-yang-digunakan)
- [Cara Bermain](#-cara-bermain)
- [Instalasi](#-instalasi)
- [Versi File](#-versi-file)
- [Kontribusi Tim](#-kontribusi-tim)
- [Screenshot](#-screenshot)
- [Lisensi](#-lisensi)

---

## 🌟 Tentang Proyek

**Neon Ascent** adalah proyek tugas akhir mata kuliah Pemrograman Komputer yang mengimplementasikan berbagai konsep dasar Python dalam bentuk game interaktif.

### Tujuan Pembelajaran

Proyek ini dibuat untuk mendemonstrasikan pemahaman tentang:
- ✅ Tipe data Python (Tuple, List, Set, Dictionary)
- ✅ Control flow (If-Else, While, For loops)
- ✅ Function dan modularitas
- ✅ File handling (save/load game)
- ✅ Konsep OOP dasar
- ✅ Error handling

---

## ⚡ Fitur Utama

### Gameplay Features
- **Sistem Pertarungan Interaktif** - Lawan musuh dengan 4 kekuatan cyber unik
- **Eksplorasi Area** - Jelajahi 5 lokasi berbeda dengan random encounters
- **Puzzle Hacking** - Pecahkan firewall dengan strategi yang tepat
- **Sistem Inventori** - Kumpulkan dan gunakan item untuk bertahan hidup
- **Multiple Endings** - Cerita berakhir berbeda berdasarkan gaya bermain Anda

### Technical Features
- **Save/Load System** - Simpan progres ke file `.txt`
- **Slow Typing Effect** - Efek mengetik seperti terminal hacker asli
- **ASCII Art** - Interface visual menarik di terminal
- **Random Encounters** - Setiap playthrough terasa berbeda

---

## 🗂️ Struktur Data yang Digunakan

### 1️⃣ **TUPLE** - Data Immutable
```python
STAT_DASAR = ("Cyber-Runner", 100, "Pemula")
# (kelas, hp_maks, pangkat)
```
**Digunakan untuk:** Statistik dasar yang tidak berubah sepanjang game

### 2️⃣ **LIST** - Data Dinamis
```python
kekuatan_terbuka = ["Pyrobyte", "Cryostream"]
inventori = ["Stimpack Neural"]
```
**Digunakan untuk:** Kekuatan dan item yang dapat bertambah/berkurang

### 3️⃣ **SET** - Data Unik
```python
musuh_dikalahkan = set()
area_terjelajahi = set()
```
**Digunakan untuk:** Tracking pencapaian tanpa duplikasi

### 4️⃣ **DICTIONARY** - Data Terstruktur
```python
data_pemain = {
    "username": "",
    "hp": 100,
    "xp": 0,
    "kredit": 50,
    "area_sekarang": "Lab Rahasia",
    "penggunaan_kekuatan": {...}
}
```
**Digunakan untuk:** Menyimpan statistik pemain yang kompleks

---

## 🎮 Cara Bermain

### Instalasi & Menjalankan Game

1. **Clone repository**
```bash
git clone https://github.com/username/neon-ascent.git
cd neon-ascent
```

2. **Jalankan game**
```bash
python neon_ascent.py
```

### Kontrol Game

#### Menu Utama
- `1` - Mulai game baru
- `2` - Muat game tersimpan
- `3` - Keluar

#### Dalam Game
- `1` - Lihat status karakter
- `2` - Jelajahi area (main quest)
- `3` - Kunjungi pasar gelap (beli item)
- `4` - Cari Peninggalan Cyber (boss fight)
- `5` - Simpan game
- `6` - Keluar game

### 🔥 Kekuatan Cyber

| Kekuatan | Icon | Deskripsi |
|----------|------|-----------|
| **Pyrobyte** | 🔥 | Serangan api yang kuat |
| **Cryostream** | ❄️ | Membekukan musuh |
| **Aerosurge** | 🌪️ | Serangan kecepatan tinggi |
| **Terracode** | 🪨 | Pertahanan kuat |

### 🎯 Tips Bermain

1. **Jelajahi semua area** untuk mendapatkan XP dan kredit
2. **Simpan game secara berkala** untuk menghindari kehilangan progres
3. **Gunakan Stimpack** sebelum boss fight
4. **Buka semua 4 kekuatan** sebelum menghadapi final boss
5. **Kekuatan yang sering digunakan** menentukan ending Anda!

---

## 📦 Instalasi

### Requirements
- Python 3.7 atau lebih baru
- OS: Windows, MacOS, atau Linux
- Terminal yang mendukung UTF-8

### Library yang Dibutuhkan
Semua library adalah Python standard library:
- `random` - Untuk random encounters dan damage
- `time` - Untuk delay dan efek typing
- `os` - Untuk file handling

**Tidak perlu instalasi tambahan!** ✨

---

## 📁 Versi File

Repository ini memiliki beberapa versi file untuk memudahkan pembelajaran:

| File | Deskripsi | Lines of Code |
|------|-----------|---------------|
| `neonAscent.py` | Versi lengkap dengan semua fitur | ~500 baris |
| `neonAscent_o.py` | Hanya fitur inti (combat + exploration) | ~300 baris |

### 💡 Mengapa Ada Beberapa Versi?

Karena ini adalah **proyek kelompok**, kami membagi kode menjadi versi yang lebih kecil agar:
- ✅ Setiap anggota tim bisa fokus menjelaskan bagian tertentu
- ✅ Lebih mudah dipresentasikan ke dosen (tidak terlalu panjang)
- ✅ Teman-teman bisa memahami konsep secara bertahap
- ✅ Memudahkan debugging dan testing

**Rekomendasi untuk presentasi:**
1. Jelaskan konsep dari `neon_ascent_simple.py` (struktur dasar)
2. Demo fitur lengkap dari `neon_ascent_full.py`
3. Diskusi implementasi detail dari `neon_ascent_core.py`

---

## 👥 Kontribusi Tim

| Nama | NIM | Kontribusi |
|------|-----|------------|
| Fabiola Walean | 105022510040 | Game logic & combat system |
| Marselino & Fabiola | - | File handling & save system |
| Marselino | - | UI/UX & ASCII art |
| Gabrilian | -| Testing & documentation |

---

## 📸 Screenshot

```
    ███╗   ██╗███████╗ ██████╗ ███╗   ██╗
    ████╗  ██║██╔════╝██╔═══██╗████╗  ██║
    ██╔██╗ ██║█████╗  ██║   ██║██╔██╗ ██║
    ██║╚██╗██║██╔══╝  ██║   ██║██║╚██╗██║
    ██║ ╚████║███████╗╚██████╔╝██║ ╚████║
    ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
         ASCENT: Protokol Peninggalan Cyber
```

---

## 🏆 Konsep Programming yang Diimplementasikan

### 🔁 Control Flow
- **While Loop**: Menu utama dan game loop
- **For Loop**: Menampilkan list kekuatan dan inventori
- **If-Else**: Decision making dalam combat dan exploration
- **Try-Except**: Error handling untuk input user

### 📊 Data Structures
- **Tuple**: Menyimpan konstanta game
- **List**: Inventori dan kekuatan yang dinamis
- **Set**: Tracking achievement unik
- **Dictionary**: Data pemain yang kompleks

### 🔧 Functions
- `cetak_lambat()` - Typing effect
- `simpan_game()` / `muat_game()` - File persistence
- `pertarungan()` - Combat system
- `jelajahi_area()` - Exploration mechanics
- `tentukan_akhir()` - Multiple endings logic

### 📁 File Handling
- Menyimpan game state ke `.txt` file
- Parsing data dengan format custom
- Error handling untuk file operations

---

## 🚀 Cara Menjelaskan ke Teman/Dosen

### 1. **Penjelasan Umum** (5 menit)
"Ini adalah text-based RPG di mana pemain menjelajahi dunia cyberpunk. Game ini mendemonstrasikan penggunaan berbagai tipe data Python dan control flow."

### 2. **Demo Fitur** (5 menit)
- Jalankan game
- Tunjukkan combat system
- Simpan dan load game
- Tunjukkan multiple endings

### 3. **Penjelasan Teknis** (10 menit)
- Tunjukkan penggunaan Tuple untuk konstanta
- Jelaskan List untuk inventori dinamis
- Demonstrasi Set untuk tracking musuh
- Diskusi Dictionary untuk data kompleks
- Jelaskan While dan For loops dalam game flow

### 4. **Q&A** (5 menit)

---

## 📝 Lisensi

Proyek ini dibuat untuk keperluan akademik. Bebas digunakan untuk pembelajaran.

---

## 🌐 Kontak & Link

- 📧 Email: [waleanfabiola@gmail.com]
- 🔗 GitHub: [[https://github.com/username/neon-ascent](https://github.com/Fabiola701)]
- 📱 Instagram: [@lalaaawn]

---

## ⭐ Catatan Akhir

> *"Dalam dunia di mana data adalah kekuatan, kode adalah senjata terkuat."*

Terima kasih telah bermain **Neon Ascent**! 🎮✨

**Made with 💙 by [Group 6]**

---

### Members of Group 6:
1. Marselino
2. Gabrilian
3. Fabiola

File ini merupakan bagian dari tugas akhir mata kuliah **Computer Programming**. Kode ini mengimplementasikan konsep-konsep yang telah diajarkan di kelas.

**Verifikasi:** Silakan cek commit history di GitHub untuk melihat proses development.
