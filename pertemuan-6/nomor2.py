# Buatlah sebuah program yang melakukan pengecekan input dari user dengan kondisi:
# • Cek angka yang di input user, apabila bernilai ganjil maka output-nya “Angka
# <input_angka> merupakan angka ganjil”
# • Apabila bernilai ganjil maka output-nya “Angka <input_angka> merupakan angka
# genap”
# • Apabila user memasukan nilai selain angka, maka output yang dihasilkan “Maaf
# silahkan masukan angka”

angka = input("Masukkan Angka: ")

if angka.isdigit():
    angka = int(angka)
    if angka % 2 != 0:
        print(f"Angka {angka} merupakan angka ganjil")
    else:
        print(f"Angka {angka} merupakan angka genap")
else:
    print("⚠️  ⚠️  Maaf, silahkan masukkan input berupa angka! 🔢🔢")
