# NAMA: MUHAMAD SHANDY WINATA 
# NIM: 2305848

def linearSearch(arr, target):
    for item in range(len(arr)):
        if arr[item] == target:
            return item
        
    return -1

daftarNama = ["arul", "andika", "fatra", "mahesa", "fadhel", "achmad", "rafi", "bagas", "shandy", "ghaisan", "zam", "gregorius", "shaehyan", "zie", "mutia", "haryo", "fadli", "zikri", "wilga", "asep"]
namaTarget = input("Masukkan nama yang ingin dicari: ")

hasil = linearSearch(daftarNama, namaTarget)

if hasil != -1:
    print(f"Nama {namaTarget} ditemukan pada indeks ke-{hasil}")
else:
    print(f"Nama {namaTarget} tidak ditemukan dalam array")