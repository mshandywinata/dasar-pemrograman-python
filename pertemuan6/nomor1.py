# NOMOR 1

# 1. Buatlah sebuah program untuk melakukan pengecekan nilai yang di input oleh user, apabila
# nilai >= 90 maka bernilai A, apabila 90 < nilai >= 80 bernilai B, apabila 80 < nilai <= 70
# maka bernilai C, dan apabila nilai < 70 dari maka nilainya D.

nilai = input("Masukkan Nilai: ")

if nilai.isdigit():
    nilai = int(nilai)
    
    if nilai >= 90:
        print("Nilai Anda A")
    elif 90 > nilai >= 80:
        print("Nilai Anda B")
    elif 80 > nilai >= 70:
        print("Nilai Anda C")
    else:
        print("Nilai Anda D")
else:
    print("⚠️  ⚠️  Maaf, silahkan masukkan input berupa angka! 🔢🔢")
    
# statement diubah dari soal yaitu:
# 90 < nilai >= 80 dan 80 < nilai <= 70
# karena jika inputan (misal) nilai 89
# maka ouputnya akan "C"
