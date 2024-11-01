import random

def tebak_angka():
    print("Selamat datang di permainan Tebak Angka!")
    print("Saya telah memilih angka antara 1 hingga 100.")
    print("Coba tebak angka tersebut dalam sesedikit mungkin tebakan.\n")

    # Komputer memilih angka acak antara 1 dan 100
    angka_rahasia = random.randint(1, 100)
    tebakan = None
    jumlah_tebakan = 0

    # Loop hingga pemain menebak angka yang benar
    while tebakan != angka_rahasia:
        try:
            # Meminta input dari pemain
            tebakan = int(input("Masukkan tebakan Anda: "))
            jumlah_tebakan += 1

            # Menentukan apakah tebakan terlalu tinggi, rendah, atau tepat
            if tebakan < angka_rahasia:
                print("Terlalu rendah! Coba lagi.")
            elif tebakan > angka_rahasia:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Anda berhasil menebak angka {angka_rahasia} dalam {jumlah_tebakan} kali tebakan.")
        except ValueError:
            print("Harap masukkan angka yang valid.")
            
# Menjalankan game
tebak_angka()
