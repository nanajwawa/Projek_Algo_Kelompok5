import pandas as pd
import os
import csv

# Menampilkan header aplikasi
def header(isi='', homepage=0):
    os.system('cls')
    
    with open('header.txt', 'r', encoding='utf-8') as file:
        filetxt = file.read()
    print(filetxt)
    
    width = (67 - len(isi)) // 2
    print(" " * width + isi + " " * width)
    print('=' * 66)
    
    if homepage == 1:
        kalimat_welcome = "Selamat Datang di aplikasi SIPERPUS! :)"
        width = (67 - len(kalimat_welcome)) // 2
        print(" " * width + kalimat_welcome + " " * width)
        
        kalimat_pilih_opsi= "Untuk masuk silahkan pilih opsi dibawah ini"
        width = (67 - len(kalimat_pilih_opsi)) // 2
        print(" " * width + kalimat_pilih_opsi + " " * width)
        
        print("[1] Log in\n[2] Keluar Aplikasi")
        
        while True:
            pilihan = input("Pilih menu: ")
            if pilihan == '1':
                login()
                break
            elif pilihan == '2':
                keluar_aplikasi()
                break
            else:
                print('Maaf, silahkan masukkan pilihan yang tersedia.')


# Fitur login
df = pd.read_csv('DaftarPengguna.csv')
daftar_pengguna = df.set_index("username")

def login():
    print("\n===== LOGIN =====")
    masukkan_password = True

    while True:
        print("Masukkan username: ")
        username = input ("")
        if username in daftar_pengguna.index:
            while(masukkan_password):
                print("Masukkan password: ")
                password = input ("")
                if password == str (daftar_pengguna.loc[username, "password"]):
                    role_pengguna = daftar_pengguna.loc[username, "role"]
                    print(f'\nAnda masuk sebagai {role_pengguna}')
                    
                    if role_pengguna == 'admin':
                        print("Selamat datang Admin!")
                    elif role_pengguna == 'siswa':
                        print("Selamat datang Siswa!")
                print("Login berhasil!")
                masukkan_password = False
                break
            else:
                print("Password salah, silahkan coba lagi.")
        else:
            print('\n| Maaf, username tidak valid\n| Silahkan coba lagi.')
        if masukkan_password == False:
            break

def keluar_aplikasi():
    print("Terima kasih telah menggunakan aplikasi SIPERPUS!")
    exit()

header(isi="SISTEM PENGELOLAAN PERPUSTAKAAN", homepage=1)