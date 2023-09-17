print("Selamat Datang di Kuis Seputar RPL")

# meminta inputan untuk memulai program
playing = input("Ingin memulai game? ")

# program berhenti jika inputan tidak sesuai
if playing.lower() != "ya":
    quit()

print("Baiklah! Ayo bermain :)")
# inisiasi skor dan banyaknya pertanyaan yang telah dilalui
score = 0
question_number = 0

# meminta inputan jawaban
answer = input("Apa kepanjangan dari JS? ")
# memeriksa apakah jawabannya tepat
if answer.lower() == "javascript":
    # kode ini akan dieksekusi jika jawaban benar dan menambah skor
    print("Benar!")
    score += 1
# kode ini akan dieksekusi jika jawaban salah
else: 
    print("Salah!")
# menambah banyaknya pertanyaan yang telah dilalui
question_number += 1
    
answer = input("Apa kepajangan dari HTML? ")
if answer.lower() == "hypertext markup language":
    print("Benar!")
    score += 1
else: 
    print("Salah!")
question_number += 1

answer = input("Apa kepajangan dari CSS? ")
if answer.lower() == "cascading style sheet":
    print("Benar!")
    score += 1
else: 
    print("Salah!")
question_number += 1

answer = input("Apa kepanjangan dari OOP? ")
if answer.lower() == "object oriented programming":
    print("Benar!")
    score += 1
else: 
    print("Salah!")
question_number += 1

answer = input("Apa kepajangan dari SDLC? ")
if answer.lower() == "software development life cycle":
    print("Benar!")
    score += 1
else: 
    print("Salah!")
question_number += 1

# menampilkan banyaknya pertanyaan yang telah dijawab dengan benar
print(f"Kamu telah menajawab {score} pertanyaan.")
# menampilkan skor berupa persentase
print(f"Skor kamu adalah {(score / question_number) * 100}%")
