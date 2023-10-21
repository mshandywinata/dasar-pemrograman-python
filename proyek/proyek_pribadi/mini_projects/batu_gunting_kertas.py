import random as rand
import os

border = "###############################################"

print(f"""
{border}

                🪨  ✂️  📰
 
🔥SELAMAT DATANG DI GIM BATU GUNTING KERTAS!🔥

                🪨  ✂️  📰

{border}
""")

username = input("Masukkan username Anda: ").upper()
os.system("cls")

user_wins = 0
comp_wins = 0
choices = ["batu", "gunting", "kertas"]

while True:
    print(f"""🪨  ✂️  📰
KAMU: {user_wins} VS KOMPUTER: {comp_wins}
""")
    
    user_choice = input(
"""Pilih Batu/Gunting/Kertas
atau ketik \"K\" untuk KELUAR dari permainan.
Pilihanmu: """).lower()
    if user_choice == "k":
        break
    
    if user_choice not in choices:
        print("\nMasukkan pilihan yang tersedia!")
        input("Tekan ENTER untuk mengulang! ")
        os.system("cls")
        continue
    
    random_number = rand.randint(0, 2)
    # batu = 0, gunting = 1, kertas = 2
    comp_choice = choices[random_number]
    print(f"""
Komputer memillih {comp_choice}.""")
    
    if user_choice == "batu" and comp_choice == "gunting":
        print("Kamu menang!\n")
        user_wins += 1
        input("Tekan ENTER untuk melanjutkan! ")
        os.system("cls")

    elif user_choice == "kertas" and comp_choice == "batu":
        print("Kamu menang!\n")
        user_wins += 1
        # os.system("pause")
        input("Tekan ENTER untuk melanjutkan! ")
        os.system("cls")
    
    elif user_choice == "gunting" and comp_choice == "kertas":
        print("Kamu menang!\n")
        user_wins += 1
        input("Tekan ENTER untuk melanjutkan! ")
        os.system("cls")
        
    elif user_choice == comp_choice:
        print("Seri!\n")
        input("Tekan ENTER untuk melanjutkan! ")
        os.system("cls")

    else:
        print("Kamu kalah!\n")
        comp_wins +=1
        input("Tekan ENTER untuk melanjutkan! ")
        os.system("cls")

os.system("cls")
print(f"""
Kamu menang sebanyak {user_wins} kali,
komputer menang sebanyak {comp_wins} kali!""")

if user_wins > comp_wins:
    print(f"""
{border}

Kamu lebih unggul dari komputer!
KAMU MENANG!

{border}
""")
elif user_wins < comp_wins:
    print(f"""
{border}

Kamu kurang beruntung :(
KOMPUTER MENANG!
        
{border}
""")
else:
    print(f"""
{border}

PERMAINAN SERI!

{border}
""")

print(f"""
{border}

TERIMA KASIH {username} KARENA
TELAH MENCOBA PROJECT INI 🤟🤟    

{border}
""")
