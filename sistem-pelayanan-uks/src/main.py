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







def tambah_kunjungan():
clear()
print("=== TAMBAH DATA UKS ===")

nama = input("Nama : ")
kelas = input("Kelas : ")
keluhan = input("Keluhan: ")

print("\nPilih obat (bisa lebih dari satu).")
print("Contoh: 1,3,5\n")

for i, obat in enumerate(DAFTAR_OBAT, 1):
cur.execute("SELECT jumlah FROM stok WHERE obat=?", (obat,))
stok = cur.fetchone()[0]
print(f"{i}. {obat} (stok: {stok})")

pilihan = input("\nMasukkan nomor (pisahkan dengan koma): ")
daftar_nomor = pilihan.split(",")
