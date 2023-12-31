# Nama: Muhamad Shandy Winata
# NIM: 2305848

import numpy as np

def pembuatDataDummy(batasBawah, batasAtas, banyakData):
    return np.random.randint(batasBawah, batasAtas, banyakData)

nilaiMatematika = np.array(pembuatDataDummy(40, 101, 30))
nilaiMatematikaUrut = np.sort(nilaiMatematika)[::-1]
nilaiMatematikaLimaTerbesar = np.array(nilaiMatematikaUrut[:5:])

print(f"""
Nilai Ujian Matematika (sebelum diurutkan):
{nilaiMatematika}

Nilai Ujian Matematika (setelah diurutkan):
{nilaiMatematikaUrut}

Nilai Ujian Matematika (5 terbesar): {nilaiMatematikaLimaTerbesar}""")