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