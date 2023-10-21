angka = int(input("Masukkan bil. ganjil dan > 50: "))

while angka % 2 == 0 or angka <= 50:
    angka = int(input("Salah, inputkan lagi: "))

print("benar!")