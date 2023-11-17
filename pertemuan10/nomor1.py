# Nama: Muhamad Shandy Winata
# NIM: 2305848

import numpy as np
import random as rand

def pembuatDataDummy(batasBawah, batasAtas, banyakData):
    return [rand.randrange(batasBawah, batasAtas) for i in range(banyakData)]

suhuSingapura = np.array(pembuatDataDummy(0, 100, 10))
print(f"Suhu di Singapura (Celcius): {suhuSingapura}")

for i in range(len(suhuSingapura)):
    suhuSingapura[i] = (suhuSingapura[i] * 9 / 5) + 32

print(f"Suhu di Singapura (Fahrenheit): {suhuSingapura}")