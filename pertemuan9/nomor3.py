daftarInputNilai = input("Nilai: ").split(", ")

for i in range(len(daftarInputNilai)):
    daftarInputNilai[i] = int(daftarInputNilai[i])

def hitungTotal(nilai):
    return sum(nilai)

def hitungRataRata(total):
    rataRata = total / len(daftarInputNilai)
    return rataRata

total = hitungTotal(daftarInputNilai)
rataRata = hitungRataRata(total)

print(f"""Total: {total}
Rata-rata: {rataRata}""")