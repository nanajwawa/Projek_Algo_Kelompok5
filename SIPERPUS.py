import os #Memanggil library OS untuk berinteraksi dengan sistem operasi, seperti membaca lokasi file, memeriksa keberadaan file, dan membersihkan layar.
import csv #Memanggil library untuk membaca dan menulis file CSV.
from datetime import datetime, date #datetime digunakan untuk mengubah teks menjadi tanggal, sedangkan date digunakan untuk mengambil tanggal hari ini.
import pandas as pd #untuk mengolah data berbentuk tabel.

# Menentukan lokasi folder tempat file .py berada agar pembacaan file selalu akurat
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
#_file_mendapatkan alamat lengkap lokasi file Python yang sedang dijalankan.
#dirname Digunakan untuk mengambil alamat folder dari lokasi file Python tersebut
#Menyimpan lokasi folder utama program ke dalam variabel BASE_DIR
FILE_HEADER = os.path.join(BASE_DIR, "header.txt") #agar program dapat menemukan file header.txt di folder yang sama dengan program Python
FILE_PENGGUNA = os.path.join(BASE_DIR, "DaftarPengguna.csv")
FILE_PENGGUNA = os.path.join(BASE_DIR, "DaftarPengguna.csv")
FILE_BUKU = os.path.join(BASE_DIR, "buku.csv") #os.path.join, agar penyusunan alamat file menyesuaikan sistem operasi dan program tidak perlu menuliskan alamat folder secara manual.
FILE_PEMINJAMAN = os.path.join(BASE_DIR, "peminjaman.csv")
FILE_DENDA = os.path.join(BASE_DIR, "data_denda_siperpus.csv")

KOLOM_DENDA = ["ID_PEMINJAMAN", "KETERLAMBATAN_HARI", "TOTAL_DENDA", "STATUS_DENDA"]
#Membuat daftar nama kolom yang akan digunakan pada tabel denda.

# =====================================================================
# 1. INISIALISASI SELURUH FILE PENDUKUNG
# =====================================================================
def siapkan_semua_file():
    # 1. Siapkan header.txt jika belum ada
    if not os.path.exists(FILE_HEADER): #memeriksa apakah file header sudah tersedia.
        with open(FILE_HEADER, "w", encoding="utf-8") as file: 
            #encoding, mengatur format karakter agar teks dapat dibaca dengan baik.
            #as file memberikan nama file untuk objek file yang sedang dibuka.
            file.write("=" * 67 + "\n")
            file.write("                 APLIKASI SIPERPUS (PERPUSTAKAAN)                  \n")
            file.write("=" * 67 + "\n")

    # 2. Siapkan DaftarPengguna.csv jika belum ada (dengan akun default)
    if not os.path.exists(FILE_PENGGUNA):
        df_user = pd.DataFrame([
            {"username": "admin", "password": "123", "role": "admin"},
            {"username": "siswa", "password": "123", "role": "siswa"}
        ])
        df_user.to_csv(FILE_PENGGUNA, index=False)

    # 3. Siapkan buku.csv jika belum ada
    if not os.path.exists(FILE_BUKU):
        with open(FILE_BUKU, "w", newline="", encoding="utf-8") as file: #newline="" mencegah munculnya baris kosong tambahan ketika menulis CSV pada beberapa sistem.
            tulis = csv.writer(file)
            tulis.writerow(["id_buku", "judul", "stok"])
            # Contoh 2 buku awal agar bisa langsung dites
            tulis.writerow(["B001", "Algoritma & Pemrograman", "5"])
            tulis.writerow(["B002", "Basis Data Dasar", "3"])

    # 4. Siapkan peminjaman.csv jika belum ada
    if not os.path.exists(FILE_PEMINJAMAN):
        with open(FILE_PEMINJAMAN, "w", newline="", encoding="utf-8") as file:
            tulis = csv.writer(file)
            tulis.writerow([
                "id_peminjaman",
                "id_buku",
                "nama_siswa",
                "tanggal_pinjam",
                "tanggal_kembali",
                "status"
            ])

    # 5. Siapkan data_denda_siperpus.csv jika belum ada
    if not os.path.exists(FILE_DENDA):
        df_denda = pd.DataFrame(columns=KOLOM_DENDA) #columns=KOLOM_DENDA berarti nama kolom diambil dari daftar yang sebelumnya dibuat.
        df_denda.to_csv(FILE_DENDA, index=False)


# =====================================================================
# 2. HEADER & SISTEM LOGIN / REGISTER
# =====================================================================
def tampilkan_header(isi="", homepage=0):
    os.system("cls" if os.name == "nt" else "clear")
    #os.name merupakan operator kondisi singkat (ternary).
    #os.system() menjalankan perintah sistem operasi.

    with open(FILE_HEADER, "r", encoding="utf-8") as file:
        filetxt = file.read()
    print(filetxt)

    if isi:
        width = max(0, (67 - len(isi)) // 2)
        print(" " * width + isi)
        print("=" * 67)

    if homepage == 1:
        kalimat_welcome = "Selamat Datang di aplikasi SIPERPUS! :)"
        width = max(0, (67 - len(kalimat_welcome)) // 2)
        print(" " * width + kalimat_welcome)

        kalimat_pilih_opsi = "Untuk masuk silahkan pilih opsi dibawah ini"
        width = max(0, (67 - len(kalimat_pilih_opsi)) // 2)
        print(" " * width + kalimat_pilih_opsi)

        print("\n[1] Log in")
        print("[2] Register Akun Siswa")
        print("[3] Keluar Aplikasi")

        while True:
            pilihan = input("\nPilih menu (1/2/3): ").strip()
            if pilihan == "1":
                login()
                break
            elif pilihan == "2":
                register()
                break
            elif pilihan == "3":
                keluar_aplikasi()
                break
            else:
                print("Maaf, silahkan masukkan pilihan yang tersedia.")


def register():
    print("\n===== REGISTER AKUN SISWA =====")
    df = pd.read_csv(FILE_PENGGUNA, dtype=str)

    username = input("Buat username baru : ").strip()
    if not username:
        print("Username tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)
        return

    if username in df["username"].values:
        print("Username sudah digunakan! Silahkan pilih username lain.")
        input("Tekan Enter untuk kembali...")
        tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)
        return

    password = input("Buat password baru : ").strip()
    if not password:
        print("Password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)
        return

    akun_baru = pd.DataFrame([{"username": username, "password": password, "role": "siswa"}])
    df = pd.concat([df, akun_baru], ignore_index=True)
    df.to_csv(FILE_PENGGUNA, index=False)

    print(f"\nRegistrasi berhasil! Silahkan login dengan username '{username}'.")
    input("Tekan Enter untuk melanjutkan ke halaman Login...")
    tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)


def login():
    df = pd.read_csv(FILE_PENGGUNA, dtype=str)
    daftar_pengguna = df.set_index("username")

    print("\n===== LOGIN =====")
    while True:
        username = input("Masukkan username: ").strip()
        if username in daftar_pengguna.index:
            while True:
                password = input("Masukkan password: ").strip()
                if password == str(daftar_pengguna.loc[username, "password"]):
                    role_pengguna = daftar_pengguna.loc[username, "role"]
                    print(f"\nLogin berhasil! Anda masuk sebagai {role_pengguna.upper()}.")
                    input("Tekan Enter untuk masuk ke Dashboard...")

                    if role_pengguna == "admin":
                        menu_admin()
                    elif role_pengguna == "siswa":
                        menu_siswa(username)
                    return
                else:
                    print("Password salah, silahkan coba lagi.")
        else:
            print("\n| Maaf, username tidak valid\n| Silahkan coba lagi.\n")


def keluar_aplikasi():
    print("\nTerima kasih telah menggunakan aplikasi SIPERPUS!")
    exit()


# =====================================================================
# 3. FUNGSI PEMINJAMAN & PENGEMBALIAN BUKU
# =====================================================================
def ubah_stok_buku(id_buku_target, perubahan):
    """Menambah (+1) atau mengurangi (-1) stok buku di buku.csv."""
    data_buku = []
    berhasil = False

    with open(FILE_BUKU, "r", newline="", encoding="utf-8-sig") as file:
        baca = csv.DictReader(file)
        for buku in baca:
            if buku["id_buku"] == id_buku_target:
                stok_baru = int(buku["stok"]) + perubahan
                if stok_baru >= 0:
                    buku["stok"] = str(stok_baru)
                    berhasil = True
                else:
                    print("Stok buku tidak mencukupi!")
                    return False
            data_buku.append(buku)

    if berhasil:
        with open(FILE_BUKU, "w", newline="", encoding="utf-8") as file:
            kolom = ["id_buku", "judul", "stok"]
            tulis = csv.DictWriter(file, fieldnames=kolom)
            tulis.writeheader()
            tulis.writerows(data_buku)

    return berhasil


def pinjam_buku_siswa(nama_default=""):
    print("\n=== MENU PEMINJAMAN BUKU ===")
    nama = input(f"Masukkan nama siswa [{nama_default}]: ").strip()
    if not nama:
        nama = nama_default

    # Menampilkan daftar buku
    with open(FILE_BUKU, "r", newline="", encoding="utf-8-sig") as file:
        daftar_buku = list(csv.DictReader(file))

    if not daftar_buku:
        print("Belum ada data buku di perpustakaan.")
        return

    print("\nDaftar Buku:")
    for buku in daftar_buku:
        print(f"{buku['id_buku']} - {buku['judul']} - Stok: {buku['stok']}")

    id_buku = input("\nMasukkan ID buku yang ingin dipinjam: ").strip()

    buku_ditemukan = False
    stok_tersedia = False

    for buku in daftar_buku:
        if buku["id_buku"] == id_buku:
            buku_ditemukan = True
            if int(buku["stok"]) > 0:
                stok_tersedia = True
            break

    if not buku_ditemukan:
        print("Buku tidak ditemukan!")
        return

    if not stok_tersedia:
        print("Maaf, stok buku sedang habis!")
        return

    tanggal_pinjam = date.today()
    print("\nTanggal pinjam:", tanggal_pinjam)

    while True:
        tanggal_kembali_str = input("Masukkan batas tanggal pengembalian (YYYY-MM-DD): ").strip()
        if not validasi_tanggal_valid(tanggal_kembali_str):
            print("Format tanggal tidak valid atau tanggal tidak ada di kalender! Gunakan YYYY-MM-DD.")
            continue

        tanggal_kembali = ubah_ke_date(tanggal_kembali_str)
        durasi = (tanggal_kembali - tanggal_pinjam).days
        if durasi <= 0:
            print("Tanggal pengembalian harus setelah tanggal pinjam!")
            continue
        if durasi > 7:
            print("Maksimal peminjaman adalah 7 hari!")
            continue
        break

    # Membuat ID peminjaman otomatis
    with open(FILE_PEMINJAMAN, "r", newline="", encoding="utf-8-sig") as file:
        jumlah = len(list(csv.DictReader(file)))

    id_peminjaman = "P" + str(jumlah + 1).zfill(3)

    with open(FILE_PEMINJAMAN, "a", newline="", encoding="utf-8") as file:
        tulis = csv.writer(file)
        tulis.writerow([
            id_peminjaman,
            id_buku,
            nama,
            tanggal_pinjam,
            tanggal_kembali,
            "menunggu diambil"
        ])

    print("\nPengajuan peminjaman berhasil!")
    print("ID Peminjaman :", id_peminjaman)
    print("Status        : menunggu diambil")


def lihat_semua_peminjaman():
    print("\n=== DAFTAR TRANSAKSI PEMINJAMAN ===")
    df = pd.read_csv(FILE_PEMINJAMAN, dtype=str)
    if df.empty:
        print("Belum ada data peminjaman.")
    else:
        print(df.to_string(index=False))


def pinjam_buku_admin():
    lihat_semua_peminjaman()
    print("\n=== MENU PERSETUJUAN PEMINJAMAN ===")

    id_peminjaman = input("Masukkan ID peminjaman: ").strip()

    data_peminjaman = []
    ditemukan = False

    with open(FILE_PEMINJAMAN, "r", newline="", encoding="utf-8-sig") as file:
        baca = csv.DictReader(file)
        for data in baca:
            if data["id_peminjaman"] == id_peminjaman:
                ditemukan = True
                if data["status"] == "menunggu diambil":
                    if ubah_stok_buku(data["id_buku"], -1):
                        data["status"] = "sedang dipinjam"
                        print("Peminjaman berhasil disetujui!")
                        print(f"Stok buku '{data['id_buku']}' berkurang 1.")
                else:
                    print(f"Peminjaman tidak dapat disetujui (Status saat ini: {data['status']}).")
            data_peminjaman.append(data)

    if not ditemukan:
        print("ID peminjaman tidak ditemukan!")
        return

    with open(FILE_PEMINJAMAN, "w", newline="", encoding="utf-8") as file:
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


def kembalikan_buku():
    lihat_semua_peminjaman()
    print("\n=== MENU PENGEMBALIAN BUKU ===")

    id_peminjaman = input("Masukkan ID peminjaman: ").strip()

    data_peminjaman = []
    ditemukan = False
    id_buku_dikembalikan = None

    with open(FILE_PEMINJAMAN, "r", newline="", encoding="utf-8-sig") as file:
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

    with open(FILE_PEMINJAMAN, "w", newline="", encoding="utf-8") as file:
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

    if id_buku_dikembalikan is not None:
        if ubah_stok_buku(id_buku_dikembalikan, +1):
            print(f"Stok buku '{id_buku_dikembalikan}' bertambah 1!")


# =====================================================================
# 4. FUNGSI KELOLA DENDA (CRUD PANDAS)
# =====================================================================
def baca_data_denda():
    if os.path.exists(FILE_DENDA):
        return pd.read_csv(FILE_DENDA, dtype={"ID_PEMINJAMAN": str, "STATUS_DENDA": str})
    return pd.DataFrame(columns=KOLOM_DENDA)


def simpan_data_denda(df):
    df.to_csv(FILE_DENDA, index=False)


def tambah_denda(df):
    print("\n--- TAMBAH DATA DENDA ---")
    id_pinjam = input("Masukkan ID Peminjaman          : ").strip()

    if id_pinjam == "":
        print("ID Peminjaman tidak boleh kosong!")
        return df

    if id_pinjam in df["ID_PEMINJAMAN"].astype(str).values:
        print("ID Peminjaman sudah terdaftar di data denda!")
        return df

    try:
        jumlah_hari_terlambat = int(input("Masukkan Keterlambatan (hari) : "))
        if jumlah_hari_terlambat <= 0:
            print("Keterlambatan harus lebih dari 0 hari!")
            return df
    except ValueError:
        print("Input harus berupa angka!")
        return df

    denda_per_hari = 500
    total_denda = jumlah_hari_terlambat * denda_per_hari
    status = "Belum Lunas"

    data_baru = pd.DataFrame([{
        "ID_PEMINJAMAN": id_pinjam,
        "KETERLAMBATAN_HARI": jumlah_hari_terlambat,
        "TOTAL_DENDA": total_denda,
        "STATUS_DENDA": status
    }])

    df = pd.concat([df, data_baru], ignore_index=True)
    simpan_data_denda(df)
    print(f"\nBerhasil menambahkan data denda (Total: Rp{total_denda}).")
    return df


def lihat_denda(df):
    print("\n--- DAFTAR DENDA PERPUSTAKAAN ---")
    if df.empty:
        print("Belum ada data denda saat ini.")
    else:
        print(df.to_string(index=False))


def ubah_denda(df):
    print("\n--- PERBARUI DATA DENDA ---")
    lihat_denda(df)
    if df.empty:
        return df

    id_cari = input("\nMasukkan ID Peminjaman yang ingin diubah: ").strip()

    if id_cari in df["ID_PEMINJAMAN"].astype(str).values:
        index_baris = df[df["ID_PEMINJAMAN"].astype(str) == id_cari].index[0]

        print("[1] Perbarui Keterlambatan Hari")
        print("[2] Ubah Status Pembayaran (Lunas)")
        pilihan = input("Pilih bagian yang ingin diubah (1/2): ").strip()

        if pilihan == "1":
            try:
                hari_baru = int(input("Masukkan jumlah keterlambatan baru (hari): "))
                df.loc[index_baris, "KETERLAMBATAN_HARI"] = hari_baru
                df.loc[index_baris, "TOTAL_DENDA"] = hari_baru * 500
                print("Keterlambatan dan total denda berhasil diperbarui!")
            except ValueError:
                print("Input harus berupa angka!")
        elif pilihan == "2":
            df.loc[index_baris, "STATUS_DENDA"] = "Lunas"
            print("Status denda berhasil diubah menjadi Lunas!")
        else:
            print("Pilihan tidak valid.")

        simpan_data_denda(df)
    else:
        print(f"Data dengan ID Peminjaman '{id_cari}' tidak ditemukan.")

    return df


def hapus_denda(df):
    print("\n--- HAPUS DATA DENDA ---")
    lihat_denda(df)
    if df.empty:
        return df

    id_cari = input("\nMasukkan ID Peminjaman yang ingin dihapus datanya: ").strip()

    if id_cari in df["ID_PEMINJAMAN"].astype(str).values:
        index_baris = df[df["ID_PEMINJAMAN"].astype(str) == id_cari].index[0]
        konfirmasi = input(f"Yakin ingin menghapus data {id_cari}? (y/n): ").strip()
        if konfirmasi.lower() == "y":
            df = df.drop(index_baris).reset_index(drop=True)
            simpan_data_denda(df)
            print("Data denda berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Data dengan ID Peminjaman '{id_cari}' tidak ditemukan.")

    return df


def menu_denda():
    df = baca_data_denda()
    while True:
        print("\n================================")
        print("           MENU DENDA           ")
        print("================================")
        print("[1] Tambah Data Denda")
        print("[2] Lihat Data Denda")
        print("[3] Ubah/Perbarui Denda")
        print("[4] Hapus Data Denda")
        print("[5] Kembali ke Menu Admin")

        pilihan = input("Pilih menu (1/2/3/4/5): ").strip()

        if pilihan == "1":
            df = tambah_denda(df)
        elif pilihan == "2":
            lihat_denda(df)
        elif pilihan == "3":
            df = ubah_denda(df)
        elif pilihan == "4":
            df = hapus_denda(df)
        elif pilihan == "5":
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih angka 1-5.")


# =====================================================================
# 5. DASHBOARD MENU ADMIN & SISWA
# =====================================================================
def menu_admin():
    while True:
        tampilkan_header(isi="DASHBOARD ADMIN SIPERPUS", homepage=0)
        print("[1] Lihat Semua Transaksi Peminjaman")
        print("[2] Setujui Peminjaman Buku")
        print("[3] Proses Pengembalian Buku")
        print("[4] Kelola Data Denda")
        print("[5] Logout")

        pilihan = input("\nPilih menu (1-5): ").strip()

        if pilihan == "1":
            lihat_semua_peminjaman()
        elif pilihan == "2":
            pinjam_buku_admin()
        elif pilihan == "3":
            kembalikan_buku()
        elif pilihan == "4":
            menu_denda()
        elif pilihan == "5":
            print("\nLogout berhasil!")
            input("Tekan Enter untuk kembali ke halaman utama...")
            tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk melanjutkan...")


def menu_siswa(username):
    while True:
        tampilkan_header(isi=f"DASHBOARD SISWA ({username.upper()})", homepage=0)
        print("[1] Ajukan Peminjaman Buku")
        print("[2] Lihat Riwayat Peminjaman")
        print("[3] Logout")

        pilihan = input("\nPilih menu (1-3): ").strip()

        if pilihan == "1":
            pinjam_buku_siswa(nama_default=username)
        elif pilihan == "2":
            lihat_semua_peminjaman()
        elif pilihan == "3":
            print("\nLogout berhasil!")
            input("Tekan Enter untuk kembali ke halaman utama...")
            tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk melanjutkan...")


# =====================================================================
# MENJALANKAN PROGRAM UTAMA
# =====================================================================
if __name__ == "__main__":
    siapkan_semua_file()
    tampilkan_header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)
