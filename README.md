# Sistem Pelayanan UKS 🏥

Halo! Ini adalah program sederhana untuk membantu petugas UKS mencatat kunjungan siswa dan mengelola stok obat.

## Tentang Proyek Ini

Program ini dibuat untuk mempermudah pekerjaan petugas UKS di sekolah. Dengan program ini, petugas bisa:
- Mencatat siswa yang datang ke UKS
- Mencatat obat apa yang diberikan
- Melihat stok obat yang tersedia
- Membuat laporan dalam bentuk Excel

## Tim Pembuat (Kelompok Bed-Ben-Ber)
1. Hafidz Ubaidillah
2. Fauzi Ibnu Prasetyo
3. Zubair Aqwam Ibadurrohman

## Apa Saja yang Bisa Dilakukan?

✅ Catat kunjungan siswa (nama, kelas, keluhan)  
✅ Pilih obat yang diberikan (bisa lebih dari 1)  
✅ Lihat semua data kunjungan  
✅ Cek stok obat  
✅ Tambah stok obat  
✅ Export data ke Excel (CSV)  

## Obat yang Tersedia

Program ini punya 10 pilihan obat:
1. Paracetamol (untuk demam, sakit kepala)
2. Ibuprofen (untuk nyeri, demam)
3. Antasida DOEN (untuk sakit perut)
4. Oralit (untuk diare)
5. Cetirizine (untuk alergi)
6. Dextromethorphan (untuk batuk)
7. Ambroxol (untuk batuk berdahak)
8. Vitamin C
9. Vitamin B Complex
10. Tidak pakai obat (cukup istirahat/kompres)

## Cara Install dan Jalankan

### Yang Dibutuhkan
- Python versi 3.7 ke atas (kalau belum punya, download di python.org)
- Komputer Windows, Linux, atau Mac

### Langkah-langkah

1. Download atau clone project ini
```bash
git clone [url-repository]
cd sistem-pelayanan-uks
```

2. Cek apakah Python sudah terinstall
```bash
python --version
```
Kalau di Linux/Mac, coba:
```bash
python3 --version
```

3. Gak perlu install apa-apa lagi! Semua library yang dipakai sudah ada di Python

### Cara Menjalankan Program

1. Buka terminal/command prompt
2. Masuk ke folder src
```bash
cd sistem-pelayanan-uks/src
```

3. Jalankan programnya
```bash
python main.py
```
Atau kalau di Linux/Mac:
```bash
python3 main.py
```

4. Nanti akan muncul menu seperti ini:
```
=== UKS SIMPLE SYSTEM ===
1. Tambah Kunjungan
2. Lihat Kunjungan
3. Lihat Stok
4. Tambah Stok
5. Export Excel
0. Keluar
```

5. Ketik angka menu yang mau dipilih, tekan Enter
6. Untuk keluar, ketik 0

## Cara Pakai Setiap Fitur

### 1. Tambah Kunjungan
Untuk mencatat siswa yang datang ke UKS:
- Ketik nama siswa
- Ketik kelas (contoh: 10A, 11B, 12C)
- Ketik keluhannya (contoh: sakit kepala, demam, dll)
- Pilih obat yang mau dikasih
  - Bisa pilih lebih dari 1 obat, pisahkan pakai koma
  - Contoh: ketik `1,3,8` untuk kasih Paracetamol, Antasida, dan Vitamin C
  - Kalau cuma istirahat tanpa obat, pilih nomor 10
- Data otomatis tersimpan dengan tanggal dan jam

### 2. Lihat Kunjungan
Untuk lihat semua data siswa yang pernah datang:
- Data yang paling baru akan muncul di atas
- Bisa lihat semua info: nama, kelas, keluhan, obat yang dikasih

### 3. Lihat Stok
Untuk cek berapa banyak obat yang masih ada:
- Akan muncul daftar semua obat dan jumlahnya
- Stok otomatis berkurang kalau ada yang pakai obat

### 4. Tambah Stok
Untuk nambah obat yang habis atau mau ditambah:
- Pilih obat yang mau ditambah
- Ketik berapa banyak yang mau ditambah
- Stok langsung bertambah

### 5. Export Excel
Untuk bikin laporan:
- Semua data kunjungan akan disimpan ke file CSV
- Nama filenya: `laporan_uks.csv`
- File ini bisa dibuka pakai Excel atau Google Sheets
- File akan tersimpan di folder yang sama dengan program

## Kalau Ada Masalah

**Program gak bisa jalan?**
- Pastikan Python sudah terinstall
- Cek lagi apakah sudah masuk ke folder `sistem-pelayanan-uks/src`
- Coba jalankan ulang

**Ada error database?**
- File database (uks.db) akan otomatis dibuat sendiri
- Kalau masih error, coba hapus file uks.db dan jalankan lagi

**Export Excel gagal?**
- Pastikan file laporan_uks.csv tidak sedang dibuka di Excel
- Kalau masih gagal, coba tutup Excel dulu

## Isi Folder Project

```
sistem-pelayanan-uks/
├── docs/                    # Semua dokumentasi
│   ├── minggu1/            # Hasil observasi dan wawancara
│   ├── minggu2/            # Analisis kebutuhan dan flowchart
│   ├── minggu3/            # Dokumentasi coding
│   └── minggu4/            # Dokumentasi testing
├── src/                     # Kode programnya
│   ├── main.py             # File utama (yang dijalankan)
│   └── uks.db              # Database (otomatis dibuat)
└── README.md               # File ini
```

## Catatan Penting

- Stok awal setiap obat adalah 20
- Database otomatis dibuat pas pertama kali jalan
- Jangan tutup program secara paksa (Ctrl+C) biar data gak rusak
- File export akan ditimpa kalau export lagi

## Timeline Pengerjaan

- ✅ Minggu 1: Observasi ke UKS dan wawancara
- ✅ Minggu 2: Bikin flowchart dan analisis kebutuhan
- ✅ Minggu 3: Coding program
- ⏳ Minggu 4: Testing dan presentasi

---

