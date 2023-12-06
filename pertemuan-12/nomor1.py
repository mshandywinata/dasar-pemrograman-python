# NAMA: MUHAMAD SHANDY WINATA 
# NIM: 2305848

def linearSearch(arr, target):
    for item in range(len(arr)):
        if arr[item] == target:
            return item
    return -1

stokBarang = ["garam", "gula", "beras", "kacang", "ayam", "ikan", "telur", "susu", "keju", "mentega", "minyak", "bumbu", "cabai", "terasi", "tepung"]
barangTarget = "smartphone"

hasil = linearSearch(stokBarang, barangTarget)

if hasil != -1:
    print(f"Barang {barangTarget} ditemukan pada indeks ke-{hasil}")
else:
    print(f"Barang {barangTarget} tidak ditemukan dalam array")
