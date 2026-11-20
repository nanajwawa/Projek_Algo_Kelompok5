# ---------------------- DENDA ----------------------
# Memasukkan pandas dan os sebagai library
import pandas as pd
import os 

# ---------------------- MENYIAPKAN FILE CSV ----------------------
# Membuat file csv data denda
File_csv = "data_denda_siperpus.csv"
Nama_kolom = ["ID_PEMINJAMAN", "TOTAL_DENDA", "STATUS_DENDA"]

def siapkan_file_csv_denda(): 
    # Membaca data file csv jika suda ada
    if os.path.exists(File_csv):
        df = pd.read_csv(File_csv)
    # Jika belum ada, maka membuat dataframe kosong 
    else:
        df = pd.DataFrame(columns=Nama_kolom)
    return df
# Menyimpan dataframe ke file csv data denda
def simpan_data_denda(df):
    df.to_csv(File_csv, index=False)

# ---------------------- FUNGSI MENU DENDA ----------------------
# ================== FUNGSI MENU: CREAT DATA ==================
def tambah_denda(df):
    print("\n--- TAMBAH DATA DENDA ---")
    id_pinjam = input("Masukkan ID Peminjaman          : ")

    # Validasi data harus diisi 
    if id_pinjam == "":
        print("ID Peminjaman tidak boleh kosong!")
        return
    # Validasi data tidak boleh sama agar tidak ada data yang duplicate
    if id_pinjam in df ["ID_PEMINJAMAN"].values:
        print("ID Peminjaman sudah terdaftar!")
        return

    # Menghitung denda otomatis
    jumlah_hari_terlambat = int(input("Masukkan Keterlambatan (hari) : "))
    denda_per_hari = 500
    total_denda = jumlah_hari_terlambat * denda_per_hari
    status = "Belum Lunas"

    data_baru = {
        "ID PEMINJAMAN": [id_pinjam],
        "TOTAL DENDA": [total_denda],
        "STATUS": [status]
    }
    
    df_baru = pd.DataFrame(data_baru)
    
    df = pd.concat([df, df_baru], ignore_index=True)
    simpan_data_denda(df)
    print("\nBerhasil menambahkan data denda.")
    return df

# ================== FUNGSI MENU: READ DATA ==================
def lihat_denda(df):
    print("\n--- DAFTAR DENDA PERPUSTAKAAN ---")
    # Validasi jika belum ada data denda
    if df.empty:
        print("Belum ada data denda saat ini.")
    else:
        print(df.to_string(index=False))

# ================== FUNGSI MENU: UPDATE DATA ==================
def ubah_denda(df):
    print("\n--- PERBARUI DATA DENDA ---")
    lihat_denda(df)
    if df.empty:
        return df

    id_cari = input("\nMasukkan ID Pinjam yang ingin diubah: ")
    
    if id_cari in df['ID PEMINJAMAN'].astype(str).values:
        index_baris = df[df['ID PEMINJAMAN'].astype(str) == id_cari].index[0]
        
        print("[1] Perbarui Keterlambatan Hari")
        print("[2] Ubah Status Pembayaran (Lunas)")
        pilihan = input("Pilih bagian yang ingin diubah (1/2): ")
        
        if pilihan == "1":
                hari_baru = int(input("Masukkan jumlah keterlambatan baru (hari): "))
                df.loc[index_baris, 'Keterlambatan_Hari'] = hari_baru
                df.loc[index_baris, 'Total_Denda'] = hari_baru * 500
                print("Keterlambatan dan total denda berhasil diperbarui!")
        elif pilihan == "2":
            df.loc[index_baris, 'Status'] = "Lunas"
            print("Status denda berhasil diubah menjadi Lunas!")
        else:
            print("Pilihan tidak valid.")
            
        simpan_data_denda(df)
    else:
        print(f"Data dengan ID Pieminjaman '{id_cari}' tidak ditemukan.")
    
    return df

# ================== FUNGSI MENU: DELETE DATA ==================
def hapus_denda(df):
    """D (Delete): Menghapus data denda yang sudah dibayar/selesai."""
    print("\n--- HAPUS DATA DENDA ---")
    lihat_denda(df)
    if df.empty:
        return df

    id_cari = input("\nMasukkan ID Peminjaman yang ingin dihapus datanya: ")
    
    if id_cari in df['ID PEMINJAMAN'].astype(str).values:
        index_baris = df[df['ID PEMINJAMAN'].astype(str) == id_cari].index[0]
        
        konfirmasi = input(f"Yakin ingin menghapus data {id_cari}? (y/n): ")
        if konfirmasi.lower() == 'y':
            df = df.drop(index_baris).reset_index(drop=True)
            simpan_data_denda(df)
            print("Data denda berhasil dihapus!")
        else:
            print("Penghapusan dibatalkan.")
    else:
        print(f"Data dengan ID Peminjaman '{id_cari}' tidak ditemukan.")
        
    return df

# ---------------------- FUNGSI UNTUK MENJALANKAN PROGRAM ----------------------
def main():
    df = siapkan_file_csv_denda()

# ---------------------- TAMPILAN MENU UTAMA DENDA ----------------------
    while True:
        print("\n================================")
        print("           MENU DENDA           ")
        print("================================")
        print("[1] Tambah Data Denda")
        print("[2] Lihat Data Denda")
        print("[3] Ubah/Perbarui Denda")
        print("[4] Hapus Data Denda")
        print("[5] Keluar")
        
        pilihan = (input("Pilih menu 1/2/3/4/5: "))
        
        if pilihan == "1":
            df = tambah_denda(df)
        elif pilihan == "2":
            lihat_denda(df)
        elif pilihan == "3":
            df = ubah_denda(df)
        elif pilihan == "4":
            df = hapus_denda(df)
        elif pilihan == "5":
            print("\nSelesai")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih angka 1/2/3/4/5.")

# ---------------------- MENJALANKAN PROGRAM ----------------------
if __name__ == "__main__":
    main()