# input nama dan tahun lahir ouput nama dan umur user

nama_user = input("Masukkan nama Anda: ")
tahun_lahir_user = int(input("Masukkan tahun lahir Anda: "))

umur_user = 2023 - tahun_lahir_user

print(f"Selamat datang, {nama_user}! Karena Anda lahir di tahun {tahun_lahir_user}, maka umur Anda sekarang adalah {umur_user} tahun.")
