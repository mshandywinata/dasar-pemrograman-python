# PERTEMUAN 2

# variable ialah tempat menyimpan data yang sifatya bisa dirubah
string = "string" # ini adalah variable dengan tipe data string
integer = 1 # ini adalah variabel dengan tipe data integer

print(string)
print(integer)

# casting variable digunakan untuk merubah tipe data dalam suatu variable
to_integer = int(integer)
to_float = float(integer)
to_string = str(string)

print(to_integer)
print(to_float)
print(to_string)

# multi-variable assign digunakan untuk memasukkan banyak nilai ke dalam beberapa variabel atau sebaliknya
a, b, c = "a", "b", "c"

print(a)
print(b)
print(c)

a = b = c = "same"

print(a)
print(b)
print(c)

# multi-variable output
print(a, b, c)

# memninta input
name = input("Enter your name: ")

print(f"Hello, {name}")

# mengecek tipe data
print(type(name))

# tipe data python
# numeric, dictionary, boolean, set, sequence type

# numeric: integer, float, complex
# jenis tipe data yang bisa digunakan untuk operasi matematika
# tipe int dapat memiliki panjang tak terhingga

# batas nilai float adalah 17 digit di belakang koma
# bisa juga berupa bilangan ilmiah "e" atau pangkat 10

# tipe data complex ialah data dengan nilai bilangan imajiner

# fungsi numeric
# abs(), max(), min(), pow(x, a), round(x, a)

# mengecek panjang string
# len()

# string slicing digunakan untuk mengambil sekumpulan string dengan rentanng tertentu
# a[index_start:index_finish] / a[:index_finish] / a[index_start:]

# modifikasi string
# upper(), lower(), strip()
# var.upper() / var.lower() / var.strip()
