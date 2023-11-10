banyakBilangan = int(input("Banyak bilangan: "))
jumlah = 0

for i in range(1, banyakBilangan + 1):
    bilangan = int(input(f"Masukkan bilangan ke-{i}: "))
    
    for i in range(2, int(bilangan ** (1/2)) + 1):
        if bilangan % i == 0:
            jumlah += bilangan
            break
        else:   
            jumlah += 0
            
print(f"Hasil penjumlahan bilangan yang bukan prima: {jumlah}")