def hitungVolumeTabung(jariJari, tinggi):
    phi = 3.14
    volume = phi * jariJari ** 2 * tinggi
    return volume

inputJariJari = int(input("Jari-jari tabung: "))
inputTinggi = int(input("Tinggi tabung: "))

volume = hitungVolumeTabung(inputJariJari, inputTinggi)

print(f"Volume tabung dengan jari-jari {inputJariJari} dan tinggi {inputTinggi} adalah {volume}")