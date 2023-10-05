# Pak Oki memiliki sebuah mobil dengan spesifikasi seperti berikut:
# • Merk: Honda
# • Tipe: HRV
# • Tahun: 2018
# • Warna: Hitam
# • No. Polisi: D 1234 ABC
# • Bensin: Pertalite
# • Tranmisi: Manual
# Karena usahanya semakin sukses, Pak Oki mengganti mobilnya dengan mobil keluaran
# terbaru, yaitu Honda Civic Turbo tahun 2023 bewarna Merah. Mobil baru Pak Oki
# menggunakan bensin Pertamax dan transmisinya Automatic. Plat nomor mobil baru Pak
# Oki adalah D 0 KI. Buatlah program yang dapat menyimpan detail informasi dari mobil
# lama Pak Oki sekaligus dapat mengupdate informasi mobil baru yang dibeli oleh Pak Oki
# (berdasarkan inputan).

border = "--------------***---------------"

mobil_pak_oki = {
    "merk": "Honda",
    "tipe": "HRV",
    "tahun": 2018,
    "warna": "Hitam",
    "no_polisi": "D 1234 ABC",
    "bensin": "Pertalite",
    "transmisi": "Manual"
}

print(f"""
Mobil lama Pak Oki adalah:
Merk: {mobil_pak_oki.get("merk")}
Tipe: {mobil_pak_oki.get("tipe")}
Warna: {mobil_pak_oki.get("warna")}
Tahun: {mobil_pak_oki.get("tahun")}
""")

print("Masukkan informasi detail mobil baru")
merk = input("Merk: ")
tipe = input("Tipe mobil: ")
tahun = input("Tahun keluaran: ")
warna = input("Warna: ")
no_polisi = input("No. Polisi: ")
bensin = input("Bensin: ")
transimisi = input("Transmisi: ")

mobil_pak_oki = {
    "merk": merk,
    "tipe": tipe,
    "tahun": tahun,
    "warna": warna,
    "no_polisi": no_polisi,
    "bensin": bensin,
    "transmisi": transimisi
}

print(f"""
{border}
Mobil baru Pak Oki adalah:
Merk: {mobil_pak_oki.get("merk")}
Tipe: {mobil_pak_oki.get("tipe")}
Warna: {mobil_pak_oki.get("warna")}
Tahun: {mobil_pak_oki.get("tahun")}
{border}
""")
