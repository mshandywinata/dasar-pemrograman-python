def deretFibonacci(banyakDeret):
    a, b = 0, 1 
    jumlah = 0
    
    for i in range(banyakDeret):
        print(jumlah)
        a, b = b, jumlah
        jumlah = a + b

inputBanyakDeret = int(input("Masukkan banyak deret Fibonacci: "))

deretFibonacci(inputBanyakDeret)