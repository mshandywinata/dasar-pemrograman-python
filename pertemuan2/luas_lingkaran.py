# luas lingkaran
import math

print("""
      
            PROGRAM KALKULATOR LUAS LINGKARAN

""")

pi = math.pi # inisiasi nilai pi
jari_jari = float(input("Masukkan nilai jari-jari: ")) # meminta input nilai jari-jari

luas_lingkaran = round(pi * jari_jari ** 2, 2) # menghitung luas lingkaran

print(f"Luas lingkaran dengan jari-jari {jari_jari} adalah {luas_lingkaran}")
