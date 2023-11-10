banyakBaris = int(input("Banyak barisan: "))
jumlahBilanganPrima = 0

for i in range(1, banyakBaris + 1):
    bilangan = int(input(f"Bilangan ke-{i}: "))
    
    for i in range(2, bilangan + 1):
        if bilangan % i == 0:
            jumlahBilanganPrima += 0
        else:
            jumlahBilanganPrima += bilangan
            break
        
if jumlahBilanganPrima <= 0:
    print("Tidak ada bilangan prima dalam list")
else:
    print(f"Jumlah bilangan prima adalah {jumlahBilanganPrima}")
