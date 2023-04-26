# Main Program
huruf = [chr(i) for i in range(97,123)]

def enkripsi_mono(kalimat,kunci):
    sandi = ""

    for i in kalimat:
        try:
            if i.isupper():
                sandi += huruf[(huruf.index(i.lower()) + kunci) % 26].upper()
            else:
                sandi += huruf[(huruf.index(i) + kunci) % 26]
        except ValueError:
                sandi += i

    return sandi

def dekripsi_mono(sandi,kunci):
    kalimat = ""

    for i in sandi:
        try:
            if i.isupper():
                kalimat += huruf[huruf.index(i.lower()) + kunci].upper()
            else:
                kalimat += huruf[huruf.index(i) + kunci]
        except ValueError:
            kalimat += i

    return kalimat


# CLI Program
import os

while True:
    os.system('clear') # for macos
    # os.system('cls') # for winos

    print('Pilih: \n1. Enkripsi Monoalphabetic\n2. Dekripsi Monoalphabetic')
    try:
        pilihan = int(input('\nMasukkan nomor pilihan: '))
    except:
        pilihan = 0

    if pilihan == 1:
        kalimat = input('\nMasukkan kalimat: ')
        kunci = int(input('Masukkan kunci: '))
        print("Hasil enkripsi:", enkripsi_mono(kalimat, kunci))
    elif pilihan == 2:
        kalimat = input('\nMasukkan kalimat: ')
        kunci = int(input('Masukkan kunci: '))
        print("Hasil dekripsi:", dekripsi_mono(kalimat, kunci))
    else:
        print('\nmasukkin pilihannya yang bener saattt!!!')

    isEnough = input('\nudah belooonnn (y/t)?')
    if isEnough == 'y' or isEnough == 'Y':
        break