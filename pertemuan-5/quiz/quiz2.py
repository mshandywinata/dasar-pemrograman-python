# Bu Rinda merasa perlu olahraga dan berencana untuk berlari sore ini. Beliau akan berlari
# di lapngan sekitar rumahnya. Lapngan yang akan digunakan beliau memiliki ukuran
# panjang 80 meter dengan lebar 3200 centimeter. Beliau berencana akan berlari
# sebanyak 5x putaran dan jalan santai sebanyak masing-masing 2x putaran saat
# pemanasan dan saat pendinginan. Buatlah sebuah program untuk menghitung total jarak
# yang akan ditempuh oleh Bu Rinda dalam satuan kilometer. Gunakan rumus menghitung
# keliling persegi panjang.

panjang_meter_ke_kilo = 80 / 1000
lebar_centi_ke_kilo = 3200 / 100000

putaran = 5 + 2 + 2
total = (2 * panjang_meter_ke_kilo + 2 * lebar_centi_ke_kilo) * putaran

print(f"""
total jarak yang telah
ditempuh Ibu Rinda
setelah {putaran}x putaran adalah
{total} km
""")
