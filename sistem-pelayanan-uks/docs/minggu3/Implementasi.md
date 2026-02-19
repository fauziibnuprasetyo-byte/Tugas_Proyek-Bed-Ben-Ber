# Dokumentasi Implementasi Kode - Minggu 3

## 📅 Periode
Minggu ke-3 Pengembangan Sistem Pelayanan UKS

## 👥 Tim Pengembang
- Hafidz Ubaidillah
- Fauzi Ibnu Prasetyo
- Zubair Aqwam Ibadurrohman

## 🎯 Tujuan
Mengimplementasikan sistem pelayanan UKS berdasarkan analisis kebutuhan yang telah dilakukan pada minggu 2.

## 🛠️ Teknologi yang Digunakan
- **Bahasa Pemrograman**: Python 3.x
- **Database**: SQLite3
- **Library**: 
  - sqlite3 (database management)
  - datetime (timestamp)
  - csv (export data)
  - os (system operations)

## 📊 Struktur Database

### Tabel: kunjungan
| Field | Tipe | Keterangan |
|-------|------|------------|
| id | INTEGER | Primary Key, Auto Increment |
| Tanggal | TEXT | Format: YYYY-MM-DD HH:MM |
| Nama | TEXT | Nama siswa |
| kelas | TEXT | Kelas siswa |
| Keluhan | TEXT | Keluhan kesehatan |
| Tindakan | TEXT | Tindakan/obat yang diberikan |

### Tabel: stok
| Field | Tipe | Keterangan |
|-------|------|------------|
| obat | TEXT | Primary Key, Nama obat |
| jumlah | INTEGER | Jumlah stok tersedia |

## 💊 Daftar Obat yang Tersedia
1. Paracetamol
2. Ibuprofen
3. Antasida DOEN
4. Oralit
5. Cetirizine
6. Dextromethorphan
7. Ambroxol
8. Vitamin C
9. Vitamin B Complex
10. Tidak pakai obat (dengan rekomendasi tindakan)

## ✨ Fitur yang Diimplementasikan

### 1. Tambah Kunjungan
- Input data siswa (nama, kelas, keluhan)
- Pemilihan obat/tindakan (multiple selection)
- Validasi stok obat
- Update stok otomatis
- Opsi tanpa obat dengan rekomendasi tindakan

### 2. Lihat Kunjungan
- Menampilkan semua data kunjungan
- Urutan dari yang terbaru

### 3. Lihat Stok
- Menampilkan stok semua obat
- Real-time update

### 4. Tambah Stok
- Menambah stok obat yang ada
- Validasi input

### 5. Export Excel
- Export data ke format CSV
- Nama file: laporan_uks.csv
- Include semua field data

## 🔄 Alur Kerja Sistem

```
[Start] → [Menu Utama]
    ↓
    ├─→ [1] Tambah Kunjungan
    │       ↓
    │   Input Data → Pilih Obat → Cek Stok → Simpan → Update Stok
    │
    ├─→ [2] Lihat Kunjungan
    │       ↓
    │   Query Database → Tampilkan Data
    │
    ├─→ [3] Lihat Stok
    │       ↓
    │   Query Stok → Tampilkan
    │
    ├─→ [4] Tambah Stok
    │       ↓
    │   Pilih Obat → Input Jumlah → Update
    │
    ├─→ [5] Export Excel
    │       ↓
    │   Query Data → Write CSV → Simpan File
    │
    └─→ [0] Keluar
```

## 📝 Catatan Implementasi

### Keputusan Desain
1. **SQLite dipilih** karena ringan, tidak perlu server terpisah, dan cocok untuk aplikasi skala kecil
2. **CLI Interface** untuk kemudahan penggunaan dan fokus pada logika bisnis
3. **CSV Export** untuk kompatibilitas dengan Excel dan aplikasi spreadsheet lainnya

### Tantangan yang Dihadapi
1. Manajemen stok obat yang real-time
2. Handling multiple selection untuk obat
3. Validasi input pengguna

### Solusi yang Diterapkan
1. Update stok langsung setelah transaksi
2. Split string dengan koma untuk multiple selection
3. Try-except untuk validasi input

## 🐛 Known Issues
1. Duplikasi kode pada fungsi tambah_kunjungan (perlu refactoring)
2. Belum ada validasi untuk input kosong
3. Error handling masih minimal

## 📈 Hasil Implementasi
- ✅ Semua fitur utama berhasil diimplementasikan
- ✅ Database berfungsi dengan baik
- ✅ Export data berhasil
- ✅ Manajemen stok berjalan
- ⚠️ Perlu perbaikan pada validasi dan error handling

## 🔜 Rencana Perbaikan
1. Fix duplikasi kode
2. Tambah validasi input
3. Improve error handling
4. Tambah fitur pencarian data
5. Improve UI/UX

---
**Dokumentasi dibuat**: Minggu 3
**Status**: Implementasi Selesai, Siap untuk Testing
