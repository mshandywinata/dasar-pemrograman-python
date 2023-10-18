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

# PR
# 1. Format file .pdf
# 2. sisipkan flowchart
# 3. Copy code programnya
# 4. Screenshot output dari terminal
# 5. Pengumpulan di SPOT atau ke email yulia.retnowati@upi.edu dengan subject Nama Lengkap_NIM_Tugas-2_1A

# PERTEMUAN 3
# tipe data list dan tuple
# list dan tuple biasa juga disebut tipe data sequence

# list bisa menyimpan berbagai tipe data dalam satu variabel dengan posisi disebut sebagai index,
# tipe data ini bersifat mutable (dapat dimodifikasi), ordered, dan memungkinkan adanya duplikasi

# manipulasi dan akses data list
# len(), var[index], var[indexStart:indexEnd - 1], append(), insert(), pop(), extend(), 

# tuple memiliki sifat seperti list namum immutable
# manipulasi dan akses data tuple
# len(), var[index], var[indexStart:indexEnd - 1]
# list() => konversi tuple ke list
# packing memungkinkan variabel pada tiap nilai yang ada di tuple
# tuple = ("data1", "data2", ..., "dataN")
# (var1, var2, ..., varN) = tuple

# PERTEMUAN 4
# tipe data set dan dictionary

# PERTEMUAN 6
# kondisional
