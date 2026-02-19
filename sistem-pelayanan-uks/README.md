# Sistem Pelayanan dan Pencatatan Kesehatan UKS

## 📋 Deskripsi
Sistem digital untuk mengelola pelayanan kesehatan di Unit Kesehatan Sekolah (UKS).

## 👥 Anggota Tim (Kelompok Bed-Ben-Ber)
1. Hafidz Ubaidillah
2. Fauzi Ibnu Prasetyo
3. Zubair Aqwam Ibadurrohman

## 🎯 Fitur yang Direncanakan
1. Pendaftaran pasien siswa
2. Pencatatan rekam medis
3. Manajemen stok obat
4. Laporan statistik kunjungan

## 📅 Timeline
- ✅ Minggu 1: Observasi & wawancara
- ⏳ Minggu 2: Analisis kebutuhan sistem
- ◻️ Minggu 3: Implementasi kode
- ◻️ Minggu 4: Testing & presentasi

## 🚀 Cara Instalasi dan Menjalankan

### Prasyarat
- Python 3.7 atau lebih baru
- Sistem operasi: Windows, Linux, atau MacOS

### Langkah Instalasi

1. Clone atau download repository ini
```bash
git clone [url-repository]
cd sistem-pelayanan-uks
```

2. Pastikan Python sudah terinstall
```bash
python --version
```
atau
```bash
python3 --version
```

3. Tidak perlu install library tambahan (menggunakan library bawaan Python)
   - sqlite3 (built-in)
   - datetime (built-in)
   - csv (built-in)
   - os (built-in)

### Cara Menjalankan

1. Masuk ke folder src
```bash
cd sistem-pelayanan-uks/src
```

2. Jalankan program
```bash
python main.py
```
atau
```bash
python3 main.py
```

3. Program akan menampilkan menu utama:
```
=== UKS SIMPLE SYSTEM ===
1. Tambah Kunjungan
2. Lihat Kunjungan
3. Lihat Stok
4. Tambah Stok
5. Export Excel
0. Keluar
```

### Penggunaan Fitur

#### 1. Tambah Kunjungan
- Masukkan nama siswa, kelas, dan keluhan
- Pilih obat yang diberikan (bisa lebih dari satu, pisahkan dengan koma)
- Contoh: 1,3,5 untuk memilih Paracetamol, Antasida, dan Cetirizine
- Sistem otomatis mengurangi stok obat

#### 2. Lihat Kunjungan
- Menampilkan semua data kunjungan siswa
- Data ditampilkan dari yang terbaru

#### 3. Lihat Stok
- Menampilkan stok semua obat yang tersedia

#### 4. Tambah Stok
- Pilih obat yang ingin ditambah stoknya
- Masukkan jumlah penambahan

#### 5. Export Excel
- Export semua data kunjungan ke file CSV
- File tersimpan dengan nama: laporan_uks.csv
- Bisa dibuka dengan Excel atau aplikasi spreadsheet lainnya

### Troubleshooting

**Program tidak bisa dijalankan?**
- Pastikan Python sudah terinstall dengan benar
- Cek versi Python minimal 3.7
- Pastikan berada di folder yang benar (sistem-pelayanan-uks/src)

**Database error?**
- File uks.db akan otomatis dibuat saat pertama kali menjalankan
- Jika ada masalah, hapus file uks.db dan jalankan ulang program

**Export CSV gagal?**
- Pastikan tidak ada aplikasi lain yang membuka file laporan_uks.csv
- Cek permission write di folder tersebut

## 📁 Struktur Proyek

```
sistem-pelayanan-uks/
├── docs/
│   ├── minggu1/          # Observasi & Wawancara
│   ├── minggu2/          # Analisis Kebutuhan
│   ├── minggu3/          # Dokumentasi Implementasi
│   └── minggu4/          # Testing & Presentasi
├── src/
│   ├── main.py           # File utama program
│   └── uks.db            # Database SQLite (auto-generated)
└── README.md
```