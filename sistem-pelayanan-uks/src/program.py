import sqlite3
import datetime
import os
import csv

DB_NAME = "uks.db"

# ==========================
# SETUP DATABASE
# ==========================

conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS kunjungan_uks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tanggal TEXT,
    nama TEXT,
    kelas TEXT,
    keluhan TEXT,
    tindakan TEXT
)
""")
conn.commit()

# ==========================
# FUNGSI SISTEM
# ==========================

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def tambah_data():
    clear_screen()
    print("=== TAMBAH DATA KUNJUNGAN UKS ===")
    nama = input("Nama siswa   : ")
    kelas = input("Kelas        : ")
    keluhan = input("Keluhan      : ")
    tindakan = input("Tindakan     : ")

    tanggal = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO kunjungan_uks (tanggal, nama, kelas, keluhan, tindakan)
    VALUES (?, ?, ?, ?, ?)
    """, (tanggal, nama, kelas, keluhan, tindakan))

    conn.commit()
    print("\nData berhasil disimpan!")
    input("\nTekan Enter untuk kembali ke menu...")

def lihat_data():
    clear_screen()
    print("=== DATA KUNJUNGAN UKS ===\n")

    cursor.execute("SELECT * FROM kunjungan_uks")
    data = cursor.fetchall()

    if not data:
        print("Belum ada data.")
    else:
        for row in data:
            print(f"ID       : {row[0]}")
            print(f"Tanggal  : {row[1]}")
            print(f"Nama     : {row[2]}")
            print(f"Kelas    : {row[3]}")
            print(f"Keluhan  : {row[4]}")
            print(f"Tindakan : {row[5]}")
            print("-" * 40)

    input("\nTekan Enter untuk kembali ke menu...")

def cari_data():
    clear_screen()
    print("=== CARI DATA SISWA ===")
    keyword = input("Masukkan nama atau kelas: ")

    cursor.execute("""
    SELECT * FROM kunjungan_uks 
    WHERE nama LIKE ? OR kelas LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))

    hasil = cursor.fetchall()

    clear_screen()
    print("=== HASIL PENCARIAN ===\n")

    if not hasil:
        print("Data tidak ditemukan.")
    else:
        for row in hasil:
            print(f"ID       : {row[0]}")
            print(f"Tanggal  : {row[1]}")
            print(f"Nama     : {row[2]}")
            print(f"Kelas    : {row[3]}")
            print(f"Keluhan  : {row[4]}")
            print(f"Tindakan : {row[5]}")
            print("-" * 40)

    input("\nTekan Enter untuk kembali ke menu...")

def export_csv():
    clear_screen()
    print("=== EXPORT DATA KE EXCEL (CSV) ===")

    cursor.execute("SELECT * FROM kunjungan_uks")
    data = cursor.fetchall()

    if not data:
        print("Tidak ada data untuk diekspor!")
        input("\nTekan Enter untuk kembali ke menu...")
        return

    filename = "laporan_uks.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Tanggal", "Nama", "Kelas", "Keluhan", "Tindakan"])
        writer.writerows(data)

    print(f"Data berhasil diekspor ke: {filename}")
    input("\nTekan Enter untuk kembali ke menu...")

# ==========================
# MENU UTAMA
# ==========================

def menu():
    while True:
        clear_screen()
        print("===================================")
        print(" SISTEM PENCATATAN KESEHATAN UKS ")
        print("===================================")
        print("1. Tambah Data Kunjungan")
        print("2. Lihat Semua Data")
        print("3. Cari Data")
        print("4. Export ke Excel (CSV)")
        print("0. Keluar")
        print("===================================")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            cari_data()
        elif pilihan == "4":
            export_csv()
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk kembali...")

# Jalankan program
menu()
conn.close()

