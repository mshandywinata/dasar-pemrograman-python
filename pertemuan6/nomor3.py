# Sekolah "Pandai Cerdas" memberikan beasiswa kepada siswa berdasarkan hasil ujian dan
# kondisi keuangan mereka. Jika nilai ujian seorang siswa lebih dari 90 dan kondisi keuangan
# keluarganya kurang dari Rp 2.000.000, maka siswa tersebut akan mendapatkan beasiswa
# penuh. Jika nilai ujian lebih dari 80 tetapi kurang dari atau sama dengan 90, dan kondisi
# keuangan kurang dari Rp 4.000.000, maka siswa tersebut akan mendapatkan beasiswa
# parsial. Selain itu, siswa yang tidak memenuhi salah satu kondisi tersebut tidak akan
# mendapatkan beasiswa. Tuliskan program Python yang memeriksa apakah seorang siswa
# berhak mendapatkan beasiswa atau tidak berdasarkan nilai ujian dan kondisi keuangan
# mereka.

nilai_ujian = input("Nilai Ujian: ")
keuangan = input("Kondisi Keuangan: Rp")

if nilai_ujian.isdigit() and keuangan.isdigit():
    nilai_ujian = int(nilai_ujian)
    keuangan = int(keuangan)
    
    if nilai_ujian > 90 and keuangan < 2000000:
        print("Kamu berhak mendapatkan beasiswa penuh!")
        
    # kondisi seharusnya bisa diubah ke nilai_ujian > 80
    # karena jika inputan (misal) nilai_ujian > 90 dan keuangan < Rp4.000.000
    # tidak mendapat beasiswa sama sekali (seharusnya parsial)
    elif 80 < nilai_ujian <= 90 and keuangan < 4000000:
        print("Kamu berhak mendapatkan beasiswa parsial!")
    else:
        print("Mohon maaf, kamu tidak mendapatkan beasiswa.")
else:
    print("⚠️  ⚠️  Maaf, silahkan masukkan input berupa angka! 🔢🔢")
