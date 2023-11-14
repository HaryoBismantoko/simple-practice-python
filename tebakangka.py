import random

random_number = random.randint(1, 100)
randnum = random_number
kesulitan = input("pilih kesulitan, hard atau easy? h untuk Hard dan e untuk Easy")
angka=int(input("Masukkan angka"))

max_attempts = 0
easy = max_attempts <= 5
hard = max_attempts <= 10

def dif():
    if kesulitan == "e":
        max_attempts = 10
    elif kesulitan == "h":
        max_attempts = 5
    else:
        print("Pilihan kesulitan tidak valid.")
    return max_attempts

def tebak_angka(angka,randnum):
    attempts = 0
    kesulitan = dif()
    while attempts < kesulitan:
        if angka > randnum:
            print("too high")
        elif angka < randnum:
            print("too low")
        else:
            print("benar")
            return
        attempts += 1
        angka=int(input("Masukkan angka lagi"))
        
    if attempts == kesulitan:
        print("batas tebak sudah tercapai, nomor yang tepat adalah ", randnum)
        return "Batas tebak tercapai"

hasil = tebak_angka(angka,randnum)
print(hasil)