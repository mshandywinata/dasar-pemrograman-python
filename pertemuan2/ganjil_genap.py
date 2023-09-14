# mengelompokkan anngka ganjil dan genap

print("""
      
PROGRAM MENENTUKAN GENAP ATAU GANJIL SUATU ANGKA

""")

angka = int(input("Masukkan angka: ")) # meminta input angka

if angka % 2 == 0: # menentukan apakah angka habis dibagi 2
    print(f"Angka {angka} adalah angka genap") # kode ini akan berjalan jika kondisi terpenuhi

else:
    print(f"Angka {angka} adalah angka ganjil") # kode ini akan berjalan jika kondisi tidak terpenuhi
