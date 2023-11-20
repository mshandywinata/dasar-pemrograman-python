# Nabila merupakan seorang pemilik online shop. Ia membutuhkan program yang dapat
# menyimpan seluruh barang jualan di online shop-nya. Pada bulan Juli lalu, barangbarang yang dijual oleh online shop Nabila antara lain:
# T-Shirt, Blouse, Kemeja, Celana Panjang, Rok, Baju Renang, Tas, Topi, Sepatu,
# dan Sendal
# Mulai bulan ini, online shop tersebut berhenti berjualan Baju Renang dan diganti menjadi
# Gamis. Selain itu, karena banyaknya permintaan pelanggan, kini online shop-nya pun
# memproduksi Ikat Rambut dan Kerudung. Program yang Nabila butuhkan harus dapat
# menampilkan daftar barang jualan pada bulan Juli berserta jumlah jenis barangnya dan
# daftar barang jualan bulan ini berserta jumlah jenis barangnya. Buatlah program yang
# dapat memenuhi kebutuhan Nabila.

barang_jualan_bulan_juli = ["T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok", "Baju Renang", "Tas", "Topi", "Sepatu", "Sandal"]

print(f"Barang jualan bulan Juli: {barang_jualan_bulan_juli}")
print(f"Jumlah barang jualan bulan Juli: {len(barang_jualan_bulan_juli)}")

barang_jualan_bulan_ini = barang_jualan_bulan_juli
barang_jualan_bulan_ini[5] = "Gamis"
barang_jualan_bulan_ini.append("Ikat Rambut")
barang_jualan_bulan_ini.append("Kerudung")

print(f"Barang jualan bulan ini: {barang_jualan_bulan_ini}")
print(f"Jumlah barang jualan bulan ini: {len(barang_jualan_bulan_ini)}")
