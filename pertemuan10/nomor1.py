# Nama: Muhamad Shandy Winata
# NIM: 2305848

import numpy as np

def pembuatDataDummy(batasBawah, batasAtas, banyakData):
    return np.random.randint(batasBawah, batasAtas, banyakData)

suhuCelcius = np.array(pembuatDataDummy(0, 100, 10))
print(f"Suhu di Singapura (Celcius): {suhuCelcius}")

suhuFarenheit = (suhuCelcius * 9 / 2) + 32
print(f"Suhu di Singapura (Fahrenheit): {suhuFarenheit}")