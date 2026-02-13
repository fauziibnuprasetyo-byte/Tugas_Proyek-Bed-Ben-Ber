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