def login():
    kesempatan = 3
    
    while kesempatan > 0:
        username = input("Username: ")
        password = input("Password: ")
        
        if password == "Latihan":
            print(f"Selamat datang {username}! Anda berhasil login!")
            break
            
        else:
            kesempatan -= 1
            
            if kesempatan <= 0:
                print(f"Maaf, kesempatan Anda telah habis! Anda telah keluar dari menu login.")
            else:
                print(f"Password Anda salah! Kesempatan Anda tinggal {kesempatan}x lagi!")
    
login()