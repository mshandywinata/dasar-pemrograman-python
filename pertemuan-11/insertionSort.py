import time as tm

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr

testArray = [7, 1, 36, 26, 63, 93, 55, 16, 19, 38, 74, 65, 18, 59, 8, 43, 24, 79, 49, 35, 23, 78, 51, 2, 46, 28, 60, 76,
10, 85, 66, 29, 82, 58, 69, 75, 48, 100, 5, 32, 40, 33, 34, 90, 81, 42, 57, 44, 41, 77]
print(f"Unsorted: {testArray}")

mulai = tm.perf_counter()
sortedArray = insertionSort(testArray)
selesai = tm.perf_counter()

execTime = selesai - mulai

print(f"""
Sorted: {sortedArray}

Execution Time: {execTime:.3} detik
""")