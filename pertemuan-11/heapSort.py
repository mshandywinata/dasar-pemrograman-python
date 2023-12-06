import time as tm

def heapify(arr, n, i):
    terbesar = i
    childKiri = 2 * i + 1
    childKanan = 2 * i + 2

    if childKiri < n and arr[childKiri] > arr[terbesar]:
        terbesar = childKiri

    if childKanan < n and arr[childKanan] > arr[terbesar]:
        terbesar = childKanan

    if terbesar != i:
        arr[i], arr[terbesar] = arr[terbesar], arr[i]
        heapify(arr, n, terbesar)

def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
    return arr

testArray = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76,
10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
print(f"Unsorted: {testArray}")

mulai = tm.perf_counter()
heapSort(testArray)
selesai = tm.perf_counter()

execTime = selesai - mulai

print(f"""
Sorted: {heapSort(testArray)}

Execution Time: {execTime:.3} detik
""")