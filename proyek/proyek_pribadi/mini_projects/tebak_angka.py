# mengimpor library random
import random as rand

# meminta input batasan angka (dari 0)
top_range = input("Ketikan sebuah angka: ")

# memeriksa inputan
if top_range.isdigit():
    # mengubah inputan ke tipe data int
    top_range = int(top_range)
    
    # program keluar jika inputan lebih kecil atau sama dengan 0
    if top_range <= 0:
        print("Ketikan angka yang lebih besar dari 0!")
        quit()
# kode ini akan dieksekusi jika inputan bukanlah angka
else:
    print("Tolong ketikan angka saja!")
    quit()
    
# memasukkan batasan angka dann inisiasi variabel banyaknya percobaan
random_number = rand.randint(0, top_range)
guesses = 0

# perulangan ini akan terus berlanjut jika tebakan masih salah
while True:
    # menambah banyaknya percobaan
    guesses += 1
    # meminta inputan tebakan angka
    user_guess = input("Tebak angkanya: ")
    # memeriksa tebakan
    if user_guess.isdigit():
        # mengubah inputan ke tipe data int
        user_guess = int(user_guess)
    # kode ini akan dieksekusi jika inputan bukanlah angka
    else:
        print("Tolong ketikan angka saja!")
        continue
    # memeriksa apakah tebakan benar dan mengakhiri perulangan
    if user_guess == random_number:
        print("Tebakanmu benar!")
        break
    # memberi petunjuk (lebih besar atau lebih kecil) terhadap tebakan jika salah
    elif user_guess > random_number:
        print("Angka tebakanmu terlalu besar!")
    else:
        print("Angka tebakanmu terlalu kecil!")

# menampilkan berapa banyak user telah mencoba untuk menebak
print(f"Kamu berhasil menebaknya setelah sebanyak {guesses} percobaan")
