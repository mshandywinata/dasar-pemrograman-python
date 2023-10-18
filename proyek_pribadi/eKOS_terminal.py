import os

border = "============================="

pengguna = {
    "nama": "",
    "kata_sandi": "",
    "nomor_kamar": 0
}

def daftar():
    os.system("cls")
    
    print(f'''
{border}
[DAFTAR]
{border}
''')
    
    nama = input("Nama: ")
    while True:
        kata_sandi = input("Kata Sandi: ")
        ulang_kata_sandi = input("Ulang Kata Sandi: ")
        
        if kata_sandi != ulang_kata_sandi:
            os.system("cls")
            print("KATA SANDI TIDAK COCOK!")
            os.system("pause")
            os.system("cls")
            continue
        else:
            os.system("cls")
            print(f"Selamat datang {nama}, kamu telah terdaftar!")
            os.system("pause")
            masuk()

def masuk():
    os.system("cls")
    
    print(f'''
{border}
[MASUK]
{border}
    ''')
    
    nama = input("Nama: ")
    kata_sandi = input("Kata Sandi: ")
    

def main():
    os.system("cls")
    print(f'''
{border}
SELAMAT DATANG DI EKOS
{border}

Aplikasi manajemen kos digital.

[MENU]
[1] Masuk
[2] Daftar
[3] Keluar
    ''')

    while True:
        input_menu = input('Pilihan: ')
        if input_menu == "1":
            masuk()
        elif input_menu == "2":
            daftar()
        elif input_menu == "3":
            keluar()
        else:
            input_tidak_valid()
            
main()
