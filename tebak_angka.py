import random

angka = random.randint(1, 10)

kesempatan = 3
i = 0

print("========================================================")
print("==================== SELAMAT DATANG ====================")
print("================= DI GAME TEBAK ANGKA ==================")
print("======== SILAHKAN TEBAK ANGKA DARI 1 SAMPAI 10 =========")
print("== ANDA AKAN DIKASIH 3 KESEMPATAN UNTUK MENEBAK ANGKA ==")
print("========================================================")
print("\n")

while True:
    user_tebak = int(input("Masukkan angka tebakan: "))

    if user_tebak == angka:
        print("Selamat tebakan anda benar!")

        ulang = input("Mau bermain lagi? (y/n): ")

        if ulang == "y":
            i = 0
        else:
            print("Terima kasih telah bermain")
            break

    elif user_tebak < angka:
        print("Angka tebakan anda terlalu kecil")
        i += 1

    elif user_tebak > angka:
        print("Angka tebakan anda terlalu besar")
        i += 1

    if i == kesempatan:
        print(f"Maaf, kesempatan tebakan anda habis. Angka yang benar adalah {angka}")
        break

print("\n")
    