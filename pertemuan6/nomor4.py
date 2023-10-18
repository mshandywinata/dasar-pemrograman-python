# NOMOR 4

# Sebuah perusahaan memberikan bonus tahunan kepada karyawan berdasarkan performa
# mereka. Karyawan dengan performa "sangat baik" akan mendapatkan bonus sebesar 20%
# dari gaji mereka, karyawan dengan performa "cukup" akan mendapatkan bonus 10%, dan
# karyawan lainnya akan mendapatkan bonus 5%. Tuliskan program Python yang meminta
# input performa seorang karyawan dan gaji mereka, lalu menghitung jumlah bonus yang
# akan mereka terima.

performa = input("Performa (Sangat Baik/Cukup): ").lower()
gaji = input("Gaji: ")

if gaji.isdigit():
    gaji = int(gaji)
    
    if performa == "sangat baik":
        persentase_bonus = 20
        
    elif performa == "cukup":
        persentase_bonus = 10
        
    else:
        persentase_bonus = 5
        
    bonus = gaji * (persentase_bonus / 100)
    
    print(f"""
✨      ✨      ✨
Selamat! Performa kerja kamu {performa}!
Kamu mendapatkan bonus sebesar {persentase_bonus}%
Gaji kamu: Rp{gaji}
Bonus gaji: Rp{bonus}
Total gaji kamu: Rp{gaji + bonus}
            """)
else:
    print("⚠️  ⚠️  Maaf, silahkan masukkan input yang valid!")
