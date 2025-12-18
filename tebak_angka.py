import random

while True:
    print("===============================")
    print("======= SELAMAT DATANG ========")
    print("===== DI GAME TEBAK ANGKA =====")
    print("== ANDA DAPAT MENEBAK 3 KALI ==")
    print("===============================")
    print("\n")

    print("PILIH LEVEL KESULITAN (1, 2, 3):")
    print('1. Mudah (1-10)')
    print('2. Sedang (1-50)')
    print('3. Sulit (1-100)')

    level = int(input("Masukkan pilihan: "))

    print("\n")
    print(f"ANDA MEMILIH LEVEL KESULITAN {level}")

    if level == 1:
        angka = random.randint(1, 10)
        maks = 10
    elif level == 2:
        angka = random.randint(1, 50)
        maks = 50
    elif level == 3:
        angka = random.randint(1, 100)
        maks = 100

    kesempatan = 3

    for i in range(kesempatan):
        tebakan = int(input("Masukkan angka tebakan: "))

        if tebakan < 1 or tebakan > maks:
            print("Hanya dapat menebak angka 1 sampai", maks, "!")
            continue

        elif tebakan < angka:
            print("Tebakan anda terlalu kecil!")

        elif tebakan > angka:
            print("Tebakan anda terlalu besar!")

        elif tebakan == angka:
            print("Tebakan anda benar!")
            break

    else:
        print("Kesempatan habis! Angka yang benar adalah", angka)

    main_lagi = input("Ingin bermain lagi? (y/n): ").lower()
    print("\n")

    if main_lagi != "y":
        print("Terima kasih telah bermain!")
        break

    