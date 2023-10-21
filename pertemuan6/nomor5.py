# Toko "Hemat Berkah" memberikan diskon kepada pelanggan berdasarkan total belanjaan
# mereka. Jika total belanjaan pelanggan melebihi Rp 500.000, mereka akan mendapatkan
# diskon sebesar 10%. Jika total belanjaan kurang dari atau sama dengan Rp 500.000, mereka
# tidak akan mendapatkan diskon. Tuliskan program Python yang meminta input total
# belanjaan pelanggan dan menentukan apakah mereka berhak mendapatkan diskon atau
# tidak, serta menghitung total yang harus dibayar setelah diskon (jika ada).

total_belanjaan = input("Total Belanjaan: Rp")

if total_belanjaan.isdigit():
    total_belanjaan = int(total_belanjaan)
    
    if total_belanjaan > 500000:
        persentase_diskon = 10
        total_harga = total_belanjaan - (total_belanjaan * (persentase_diskon / 100))
        
        print(f"""
Selamat! Kamu mendapatkan diskon sebesar {persentase_diskon}%
Total Belanjaan: Rp{total_belanjaan}
Total Belanjaan (setelah diskon): Rp{total_harga}
        """)
        
    else:
        print(f"""
Mohon maaf, kamu tidak mendapatkan diskon
Total Belanjaan: Rp{total_belanjaan} 
              """)
else:
    print("⚠️  ⚠️  Maaf, silahkan masukkan input berupa angka! 🔢🔢")
