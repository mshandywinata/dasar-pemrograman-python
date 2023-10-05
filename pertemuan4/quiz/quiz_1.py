# Bu Novia merupakan salah satu guru Matematika di SMA Bandung, beliau ingin memiliki
# program yang dapat menyimpan 10 nilai Matematika siswanya. Adapun susunan nilainya
# adalah sebagai berikut:
# 90, 86, 57, 59, 95, 77, 67, 94, 82, dan 86.
# Beliau ingin program yang apabila beliau mengetikan no urut siswa, maka program akan
# memunculkan nilai dari siswa yang memiliki no. urut tersebut. Sebagai contoh, ketika
# beliau mengetikan no. urut 1 maka nilai yang keluar adalah 90 dan ketika mengetikan no.
# urut 3 maka nilai yang keluar adalah 57, dst. Buatlah program yang dapat memenuhi
# kebutuhan Bu Novia.

nilai = [90, 86, 57, 59, 95, 77, 67, 94, 82, 86]
no_urut = int(input("Masukkan nomor urut siswa: "))

print(f"""
nilai siswa dengan nomor urut {no_urut}
adalah {nilai[no_urut - 1]}
""")
    