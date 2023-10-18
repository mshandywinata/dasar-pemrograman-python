# Buatlah sebuah program untuk dapat menghitung total biaya yang Pak Abi harus
# keluarkan untuk membuat bangunan tersebut dimana biaya untuk pembuatan dindingnya
# yaitu Rp. 520.000/m2
# . Untuk menghitung luas permukaan dinding gunakan rumus 2 ×
# (Panjang × Tinggi) + 2 × (Lebar × Tinggi)

panjang_meter = 8
lebar_centi_ke_meter = 1000 / 100
tinggi_centi_ke_meter = 400 / 100

luas_permukaan = 2 * (panjang_meter * tinggi_centi_ke_meter) + 2 * (lebar_centi_ke_meter * tinggi_centi_ke_meter) 
biaya = luas_permukaan * 520000

print(f"""
total biaya yang diperlukan
untuk membangun dinding
dengan luas permukaan {luas_permukaan} m^2
adalah Rp.{biaya}
""")
