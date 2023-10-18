import os
import random

MAK_BARISAN = 3
MAK_TARUHAN = 1000000
MIN_TARUHAN = 50000

BARIS = 3
KOLOM = 3

banyak_simbol = {
    "💠": 2,
    "🔔": 4,
    "🍋": 6,
    "🍒": 8
}

def putaran_mesin_slot(barisan, kols, simbol_simbol):
    semua_simbol = []
    for simbol, banyak_simbol in simbol_simbol.items():
        for _ in range(banyak_simbol):
            semua_simbol.append(simbol)
            
    kolom_kolom = []
    for kol in range(kols):
        kolom = []
        simbol_sekarang = semua_simbol[:]
        for baris in range(barisan):
            nilai = random.choice(semua_simbol)
            

def deposit():
    while True:
        os.system('cls')
        jumlah = input("Berapa banyak deposit yang kamu inginkan? Rp.")
        if jumlah.isdigit():
            jumlah = int(jumlah)
            if jumlah > 0:
                break
            else:
                os.system('cls')
                print("JUMLAH DEPOSIT HARUS LEBIH DARI 0.")
                os.system('pause')
        else:
            os.system('cls')
            print("MASUKKAN INPUTAN YANG VALID!")
            os.system('pause')
    
    return jumlah

def banyak_barisan():
    while True:
        os.system('cls')
        baris = input(f"Masukkan barisan yang ingin ditaruhkan(1-{MAK_BARISAN}): ")
        if baris.isdigit():
            baris = int(baris)
            if 1 <= baris <= MAK_BARISAN:
                break
            else:
                os.system('cls')
                print("MASUKKAN JUMLAH BARIS YANG VALIID!")
                os.system('pause')
        else:
            os.system('cls')
            print("MASUKKAN INPUTAN YANG VALID!")
            os.system('pause')
    
    return baris

def banyak_taruhan():
    while True:
        os.system('cls')
        jumlah = input("Berapa banyak saldo yang akan ditaruhkan pada tiap barisnya? Rp.")
        if jumlah.isdigit():
            jumlah = int(jumlah)
            if MIN_TARUHAN <= jumlah <= MAK_TARUHAN:
                break
            else:
                os.system('cls')
                print(f"JUMLAH TARUHAN HARUS KISARAN Rp.{MIN_TARUHAN} - Rp.{MAK_TARUHAN}.")
                os.system('pause')
        else:
            os.system('cls')
            print("MASUKKAN INPUTAN YANG VALID!")
            os.system('pause')
    
    return jumlah

def main():
    saldo = deposit()
    baris = banyak_barisan()
    while True:
        taruhan = banyak_taruhan()
        jumlah_taruhan = taruhan * baris
        
        if jumlah_taruhan > saldo:
            os.system('cls')
            print(f"KAMU TIDAK MEMILIKI SALDO YANG CUKUP. SALDO KAMU SAAT INI: Rp.{saldo}")
            os.system('pause')
            
        else: 
            break
    
    os.system('cls')
    print(f"Kamu bertaruh Rp.{taruhan} pada {baris} baris. Jumlah taruhan: Rp.{jumlah_taruhan}")
    
main()
