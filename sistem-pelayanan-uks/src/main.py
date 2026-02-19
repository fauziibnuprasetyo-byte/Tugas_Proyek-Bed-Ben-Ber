import sqlite3
import datetime
import os
import csv

DB = "uks.db"

# =======================
#     DAFTAR OBAT
# =======================
DAFTAR_OBAT = [
    "Paracetamol",
    "Ibuprofen",
    "Antasida DOEN",
    "Oralit",
    "Cetirizine",
    "Dextromethorphan",
    "Ambroxol",
    "Vitamin C",
    "Vitamin B Complex",
    "Tidak pakai obat"
]

# =======================
#     SETUP DATABASE
# =======================
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS kunjungan (
id INTEGER PRIMARY KEY AUTOINCREMENT,
Tanggal TEXT,
Nama TEXT,
kelas TEXT,
Keluhan TEXT,
Tindakan TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS stok (
obat TEXT PRIMARY KEY,
jumlah INTEGER
)
""")

for obat in DAFTAR_OBAT:
    cur.execute("INSERT OR IGNORE INTO stok VALUES (?, ?)", (obat, 20))

conn.commit()

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# fitur tambah_kunjungan
def tambah_kunjungan():
    clear()
    print("=== TAMBAH DATA UKS ===")
    nama = input("Nama   : ")
    kelas = input("Kelas  : ")
    keluhan = input("Keluhan: ")

    print("\nPilih tindakan/obat (bisa lebih dari satu).")
    print("Contoh: 1,3,5\n")

    for i, obat in enumerate(DAFTAR_OBAT, 1):
        cur.execute("SELECT jumlah FROM stok WHERE obat=?", (obat,))
        stok = cur.fetchone()[0]
        # Jika indeks 8 (Tidak pakai obat), tidak perlu tampilkan stok
        if obat == "Tidak pakai obat":
            print(f"{i}. {obat}")
        else:
            print(f"{i}. {obat} (stok: {stok})")

    pilihan = input("\nMasukkan nomor (pisahkan dengan koma): ")
    daftar_nomor = pilihan.split(",")
    obat_terpilih = []
    rekomendasi_tambahan = ""

    for nomor in daftar_nomor:
        try:
            idx = int(nomor.strip()) - 1
            obat = DAFTAR_OBAT[idx]
            
            # LOGIKA BARU: Jika pilih nomor 8 (Tidak pakai obat)
            if obat == "Tidak pakai obat":
                rekomendasi_tambahan = input("Masukkan rekomendasi tindakan (misal: Istirahat 30 menit): ")
                obat_terpilih.append(f"Tanpa Obat ({rekomendasi_tambahan})")
                continue # Lanjut ke nomor berikutnya tanpa cek stok

            # Cek Stok untuk obat beneran
            cur.execute("SELECT jumlah FROM stok WHERE obat=?", (obat,))
            stok = cur.fetchone()[0]

            if stok <= 0:
                print(f"\n❌ Stok {obat} habis! Proses dibatalkan.")
                input("Tekan Enter...")
                return

            obat_terpilih.append(obat)
            # Update stok hanya untuk obat beneran
            cur.execute("UPDATE stok SET jumlah = jumlah - 1 WHERE obat=?", (obat,))

        except (ValueError, IndexError):
            print(f"\n❌ Nomor {nomor} tidak valid!")
            input("Tekan Enter...")
            return

    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    tindakan = "Tindakan: " + ", ".join(obat_terpilih)

    cur.execute("""
    INSERT INTO kunjungan (tanggal, nama, kelas, keluhan, tindakan)
    VALUES (?, ?, ?, ?, ?)
    """, (tanggal, nama, kelas, keluhan, tindakan))

    conn.commit()
    print("\n✅ Data berhasil disimpan!")
    input("Tekan Enter...")

    for obat in obat_terpilih:
        cur.execute("UPDATE stok SET jumlah = jumlah - 1 WHERE obat=?", (obat,))

    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    tindakan = "Diberi: " + ", ".join(obat_terpilih)

    cur.execute("""
    INSERT INTO kunjungan (tanggal, nama, kelas, keluhan, tindakan)
    VALUES (?, ?, ?, ?, ?)
    """, (tanggal, nama, kelas, keluhan, tindakan))

    conn.commit()
    print("\n✅ Data & stok tersimpan!")
    input("Tekan Enter...")

#fitur lihat_kunjungan
def lihat_kunjungan():
    clear()
    print("=== DATA KUNJUNGAN ===\n")

    cur.execute("SELECT * FROM kunjungan ORDER BY id DESC")
    data = cur.fetchall()

    if not data:
        print("Belum ada data.")
    else:
        for d in data:
            print(d)

    input("\nTekan Enter...")

#fitur export_excel
def export_excel():
    clear()
    print("=== EXPORT DATA KE EXCEL ===\n")

    cur.execute("SELECT * FROM kunjungan ORDER BY id DESC")
    data = cur.fetchall()

    if not data:
        print("Tidak ada data untuk diekspor!")
        input("Tekan Enter...")
        return

    filename = "laporan_uks.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Tanggal", "Nama", "Kelas", "Keluhan", "Tindakan"])
        writer.writerows(data)

    print(f"✅ Data berhasil diekspor ke: {filename}")
    input("\nTekan Enter...")

#fitur lihat_stok
def lihat_stok():
    clear()
    print("=== STOK OBAT ===\n")

    cur.execute("SELECT * FROM stok")
    data = cur.fetchall()

    for obat, jumlah in data:
        print(f"{obat}: {jumlah}")

    input("\nTekan Enter...")

#fitur tambah_stok
def tambah_stok():
    clear()
    print("=== TAMBAH STOK OBAT ===\n")

    cur.execute("SELECT * FROM stok")
    data = cur.fetchall()

    for i, (obat, jumlah) in enumerate(data, 1):
        print(f"{i}. {obat} (stok: {jumlah})")

    pilihan = int(input("\nPilih nomor obat: ")) - 1
    tambahan = int(input("Jumlah tambahan stok: "))

    obat_dipilih = data[pilihan][0]

    cur.execute("UPDATE stok SET jumlah = jumlah + ? WHERE obat=?",
                (tambahan, obat_dipilih))
    conn.commit()

    print("✅ Stok berhasil ditambahkan!")
    input("Tekan Enter...")

while True:
    clear()
    print("=== UKS SIMPLE SYSTEM ===")
    print("1. Tambah Kunjungan")     
    print("2. Lihat Kunjungan")     
    print("3. Lihat Stok")          
    print("4. Tambah Stok")       
    print("5. Export Excel")        
    print("0. Keluar")

    p = input("Pilih: ")

    if p == "1":
        tambah_kunjungan()
    elif p == "2":
        lihat_kunjungan()
    elif p == "3":
        lihat_stok()
    elif p == "4":
        tambah_stok()
    elif p == "5":
        export_excel()
    elif p == "0":
        break
