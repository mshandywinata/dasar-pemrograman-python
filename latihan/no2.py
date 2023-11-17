kesempatan = 3
daftarAngka = []

while kesempatan > 0:
    angka = int(input("Input: "))
    
    if angka not in daftarAngka or angka < min(daftarAngka):
        daftarAngka.append(angka)
        kesempatan = 3
    else:
        kesempatan -= 1

hasil = 1
for i in daftarAngka:
    hasil *= i
    
print(f"Hasil perkalian nilai yang mengecil: {hasil}")