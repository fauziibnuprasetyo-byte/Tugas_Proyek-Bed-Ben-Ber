import sqlite3
import datetime
import os
import csv

DB = "uks.db"

# =======================
# DAFTAR OBAT
# =======================
DAFTAR_OBAT = [
    "Paracetamol",
    "Bodrex",
    "Antimo",
    "Oralit",
    "Tolak Angin",
    "Minyak Kayu Putih",
    "Obat Maag",
    "Tidak pakai obat"
]

# =======================
# SETUP DATABASE
# =======================
conn = sqlite3.connect(DB)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS kunjungan (
id INTEGER PRIMARY KEY AUTOINCREMENT,
tanggal TEXT,
nama TEXT,
kelas TEXT,
keluhan TEXT,
tindakan TEXT
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

