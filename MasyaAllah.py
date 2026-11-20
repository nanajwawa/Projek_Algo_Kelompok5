import csv
import os
from datetime import datetime, date


# ==================================
# FUNGSI MEMBUAT FILE CSV
# ==================================

def siapkan_file():

    if not os.path.exists("buku.csv"):
        with open("buku.csv", "w", newline="") as file:
            tulis = csv.writer(file)
            tulis.writerow(["id_buku", "judul", "stok"])

    if not os.path.exists("peminjaman.csv"):
        with open("peminjaman.csv", "w", newline="") as file:
            tulis = csv.writer(file)
            tulis.writerow([
                "id_peminjaman"
                "id_buku"
                "nama_siswa"
                "tanggal_pinjam"
                "tanggal_kembali"
                "status"
            ])


# ==================================
# FUNGSI SISWA MENGAJUKAN PEMINJAMAN
# ==================================

def pinjam_buku_siswa():

    print("\n=== MENU PEMINJAMAN BUKU ===")

nama = input("Masukkan nama siswa: ")
    
    # Menampilkan daftar buku
lokasi_file = os.path.join(os.path.dirname(__file__), "buku.csv")

with open(lokasi_file, "r", newline="", encoding="utf-8-sig") as file:
    baca = csv.DictReader(file)

    print("\nDaftar Buku:")
    
    for buku in baca:
            print(
                buku["id_buku"],
                "-",
                buku["judul"],
                "- Stok:",
                buku["stok"]
            )
id_buku = input("\nMasukkan ID buku yang ingin dipinjam: ")

# Memeriksa ketersediaan buku
buku_ditemukan = False

with open("file handling/buku.csv", "r", newline="", encoding="utf-8-sig") as file:
        baca = csv.DictReader(file)

        for buku in baca:
            if buku["id_buku"] == id_buku:
                buku_ditemukan = True

                if int(buku["stok"]) > 0:
                    stok_tersedia = True
                else:
                    stok_tersedia = False
                break
def i():
    if not buku_ditemukan:
        print("Buku tidak ditemukan!")
        return

    if not stok_tersedia:
        print("Maaf, stok buku sedang habis!")
        return

tanggal_pinjam = date.today()

print("\nTanggal pinjam:", tanggal_pinjam)

tanggal_kembali = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")

def durasi_pinjam_buku():
        if len(tanggal_kembali) == 10 and tanggal_kembali[4] == "-" and tanggal_kembali[7] == "-":

            tanggal_kembali: date = datetime.strptime(
                tanggal_kembali, "%Y-%M-%D"
            ).date()

            durasi = (tanggal_kembali - tanggal_pinjam).days
        else:
            print("Format tanggal tidak valid!")
            return

        if durasi <= 0:
            print("Tanggal pengembalian harus setelah tanggal pinjam!")
            return


# Membuat ID peminjaman
with open("file handling/peminjaman.csv", "r", newline="") as file:
        baca = list(csv.DictReader(file))
        jumlah = len(baca)

id_peminjaman = "P" + str(jumlah + 1).zfill(3)

def pinjam_buku_siswa():
# Menyimpan data peminjaman
    with open("peminjaman.csv", "a", newline="") as file:
        tulis = csv.writer(file)

    class id_buku:
        ...

    class nama:
        ...

    class tanggal_pinjam:
        ...

    class tanggal_kembali:
        ...

    tulis.writerow([
        id_peminjaman,
        id_buku,
        nama,
        tanggal_pinjam,
        tanggal_kembali,
        "menunggu diambil"
    ])

    print("\nPengajuan peminjaman berhasil!")
    print("ID Peminjaman:", id_peminjaman)
    print("Status: menunggu diambil")



# ==================================
# FUNGSI ADMIN MENYETUJUI PEMINJAMAN
# ==================================

    def pinjam_buku_admin():

        print("\n=== MENU PERSETUJUAN PEMINJAMAN ===")

    id_peminjaman = input(
        "Masukkan ID peminjaman: "
    )

    data_peminjaman = []
    ditemukan = False

    # Membaca seluruh data peminjaman
    with open("peminjaman.csv", "r", newline="") as file:
        baca = csv.DictReader(file)

        for data in baca:

            if data["id_peminjaman"] == id_peminjaman:
                ditemukan = True

                if data["status"] == "menunggu diambil":
                    data["status"] = "sedang dipinjam"
                    print("Peminjaman berhasil disetujui!")

                else:
                    print("Peminjaman sudah diproses!")
            
            data_peminjaman.append(data)

    if not ditemukan:
        print("ID peminjaman tidak ditemukan!")
        return

    # Memperbarui isi file CSV
    with open("peminjaman.csv", "w", newline="") as file:

        kolom = [
            "id_peminjaman",
            "id_buku",
            "nama_siswa",
            "tanggal_pinjam",
            "tanggal_kembali",
            "status"
        ]

        tulis = csv.DictWriter(file, fieldnames=kolom)

        tulis.writeheader()
        tulis.writerows(data_peminjaman)


# ==================================
# MENU UTAMA PEMINJAMAN
# ==================================

    def menu_peminjaman():

        siapkan_file()

    print("\n===== LOGIN PEMINJAMAN =====")

    username = input("Masukkan username: ")
    password = input("Masukkan Password: ")

    if username == "admin" and password == "admin123":
        print("\nLogin berhasil sebagai Admin!")
        pinjam_buku_admin()

    elif username == "siswa" and password == "siswa123":
        print("\nLogin berhasil sebagai Siswa!")
        pinjam_buku_siswa()

    else:
        print("\nUsername atau password salah!")


# Menjalankan program
    menu_peminjaman()

    import csv
    import os


# ==================================
# FUNGSI PENGEMBALIAN BUKU
# ==================================

    def kembalikan_buku():

        print("\n=== MENU PENGEMBALIAN BUKU ===")

    id_peminjaman = input("Masukkan ID peminjaman: ")

    data_peminjaman = []
    ditemukan = False
    id_buku_dikembalikan = None

    # Membaca seluruh data peminjaman
    with open("peminjaman.csv", "r", newline="") as file:
        baca = csv.DictReader(file)

        for data in baca:

            if data["id_peminjaman"] == id_peminjaman:
                ditemukan = True

                if data["status"] == "sedang dipinjam":
                    data["status"] = "sudah dikembalikan"
                    id_buku_dikembalikan = data["id_buku"]
                    print("Buku berhasil dikembalikan!")

                elif data["status"] == "sudah dikembalikan":
                    print("Buku ini sudah dikembalikan sebelumnya!")

                else:
                    print("Buku belum diambil / peminjaman belum disetujui!")

            data_peminjaman.append(data)

    if not ditemukan:
        print("ID peminjaman tidak ditemukan!")
        return

    # Memperbarui isi file peminjaman.csv
    with open("peminjaman.csv", "w", newline="") as file:

        kolom_peminjaman = [
            "id_peminjaman",
            "id_buku",
            "nama_siswa",
            "tanggal_pinjam",
            "tanggal_kembali",
            "status"
        ]

        tulis = csv.DictWriter(file, fieldnames=kolom_peminjaman)

        tulis.writeheader()
        tulis.writerows(data_peminjaman)

    # Menambah kembali stok buku di buku.csv jika pengembalian berhasil
    if id_buku_dikembalikan is not None:
        data_buku = []

        with open("buku.csv", "r", newline="") as file:
            baca_buku = csv.DictReader(file)

            for buku in baca_buku:
                if buku["id_buku"] == id_buku_dikembalikan:
                    buku["stok"] = str(int(buku["stok"]) + 1)

                data_buku.append(buku)

        with open("buku.csv", "w", newline="") as file:

            kolom_buku = [
                "id_buku",
                "judul",
                "stok"
            ]

            tulis_buku = csv.DictWriter(file, fieldnames=kolom_buku)

            tulis_buku.writeheader()
            tulis_buku.writerows(data_buku)

        print("Stok buku berhasil diperbarui!")


# ==================================
# MENU PENGEMBALIAN
# ==================================

    def menu_pengembalian():

        while True:

            print("\n===== MENU PENGEMBALIAN =====")
            print("1. Kembalikan Buku")
            print("2. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                kembalikan_buku()

            elif pilihan == "2":
                print("Kembali ke menu utama.")
                break

        else:
            print("Pilihan tidak valid!")


# Menjalankan program
    menu_pengembalian()
