# memeriksa kelulusan mahasiswa

print("""
      
            PROGRAM MEMERIKSA KELULUSAN NILAI

""")

nilai_UAS = float(input("Masukkan nilai UAS: ")) # meminta input nilai

if nilai_UAS >= 60: # menentukan apakah nilai lebih dari 60
    print(f"Selamat Anda lulus dengan nilai {nilai_UAS}") # kode ini akan berjalan jika kondisi terpenuhi

else:
    print(f"Maaf Anda tidak lulus dengan nilai {nilai_UAS}") # kode ini akan berjalan jika kondisi terpenuhi
