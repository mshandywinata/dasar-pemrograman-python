def hitungSelisih(mulaiJam, mulaiMenit, mulaiDetik, selesaiJam, selesaiMenit, selesaiDetik):
    
    mulai = mulaiJam % 24 * 3600 + mulaiMenit * 60 + mulaiDetik
    selesai = selesaiJam % 24 * 3600 + selesaiMenit * 60 + selesaiDetik
    selisih = selesai - mulai

    selisihDetik = selisih % 60
    selisihMenit = round((selisih - selisihDetik) / 60) % 60
    selisihJam = round((selisih - selisihMenit * 60 - selisihDetik) / 3600) % 60 % 36
    
    return selisihJam, selisihMenit, selisihDetik

print("Input mulai: ")
inputMulaiJam = int(input("Jam: "))
inputMulaiMenit = int(input("Menit: "))
inputMulaiDetik = int(input("Detik: "))

print()
print("Input selesai: ")
inputSelesaiJam = int(input("Jam: "))
inputSelesaiMenit = int(input("Menit: "))
inputSelesaiDetik = int(input("Detik: "))

selisih = hitungSelisih(inputMulaiJam, inputMulaiMenit, inputMulaiDetik, inputSelesaiJam, inputSelesaiMenit, inputSelesaiDetik)

print(f"""
Hitung selisih:
{selisih[0]} jam - {selisih[1]} menit - {selisih[2]} detik
""")