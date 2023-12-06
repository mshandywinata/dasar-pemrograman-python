# NAMA: MUHAMAD SHANDY WINATA 
# NIM: 2305848

import time as tm

def linearSearch(arr, target):
    for item in range(len(arr)):
        if arr[item] == target:
            return item
    return -1

sortedArray = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33, 34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57, 58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82, 85, 90, 93, 100]
nilaiTarget = 60

mulai = tm.perf_counter()
hasil = linearSearch(sortedArray, nilaiTarget)
selesai = tm.perf_counter()
runtime = selesai - mulai

if hasil != -1:
    print(f"Nilai {nilaiTarget} ditemukan pada indeks ke-{hasil}")
else:
    print(f"Nilai {nilaiTarget} tidak ditemukan dalam array")
    
print(f"Runtime: {runtime:.3} detik")