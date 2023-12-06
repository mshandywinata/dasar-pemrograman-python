def splashScreen():
    print('''
=======================================
|           SELAMAT DATANG            |
|          DI APLIKASI EKOS           |
=======================================      
''')



def login(InputUsername, InputPassword, InputNamaKos):
    username = open(f"/data/dataPenghuni/data{InputUsername}.txt", "r")
    password = open(f"/data/dataPenghuni/data{InputUsername}.txt", "r")
    namaKos = open(f"/data/dataPenghuni/data{InputUsername}.txt", "r")
    
    if InputUsername == username and InputPassword == password and InputNamaKos == namaKos:
        return True
    else:
        return False
    
def registrasiPemilik():
    pass

def registrasiPenghuni():
    pass

def displayMenu():
    print('''
[1.] Masuk
[2.] Daftar
[3.] Keluar
''')