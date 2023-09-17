import os

border = "=========================================="

username = input("Siapa namamu? ").upper()
print(f"""
{border}

SELAMAT DATANG {username} DI PETUALANGAN INI!

{border}
""")

os.system("pause")
os.system("cls")

answer = input("""
Kamu berada di sebuah gang sempit dan hanya bisa pergi ke kanan atau kiri.
Arah mana yang akan kamu pilih? (KANAN/KIRI)
Pilihan: """).lower()

if answer == "kanan":
    print()
elif answer == "kiri":

else:
