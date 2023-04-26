# Main Program
huruf = [chr(i) for i in range(97,123)]

def enkripsi_poly(kalimat,kunci):
    kunci_2 = ""
    i_kunci = -1

    for i in range(len(kalimat)):

        if kalimat[i].lower() in huruf:
            i_kunci += 1
            kunci_2 += kunci[i_kunci % len(kunci)].lower()
        else:
            kunci_2 += kalimat[i].lower()

    sandi = ""

    for i in range(len(kalimat)):

        try:
            i_sandi = (huruf.index(kalimat[i].lower()) + huruf.index(kunci_2[i])) % 26
            if kalimat[i].isupper():
                sandi += huruf[i_sandi].upper()
            else:
                sandi += huruf[i_sandi]
        except ValueError:
            if kalimat[i].isupper():
                sandi += kalimat[i].upper()
            else:
                sandi += kalimat[i]

    return sandi

def dekripsi_poly(sandi,kunci):
    kunci_2 = ""
    i_kunci = -1

    for i in range(len(sandi)):

        if sandi[i].lower() in huruf:
            i_kunci += 1
            kunci_2 += kunci[i_kunci % len(kunci)].lower()
        else:
            kunci_2 += sandi[i].lower()
    
    kalimat = ""

    for i in range(len(sandi)):

        try:
            i_kata = (huruf.index(sandi[i].lower()) - huruf.index(kunci_2[i]))
            if sandi[i].isupper():
                kalimat += huruf[i_kata].upper()
            else:
                kalimat += huruf[i_kata]
        except ValueError:
            if sandi[i].isupper():
                kalimat += sandi[i].upper()
            else:
                kalimat += sandi[i]

    return kalimat


# CLI Program
import os

while True:
    os.system('clear') # for macos
    # os.system('cls') # for winos

    print('Pilih: \n1. Enkprisi Polyalphabetic\n2. Dekripsi Polyalphabetic')
    try:
        pilihan = int(input('\nMasukkan nomor pilihan: '))
    except:
        pilihan = 0

    if pilihan == 1:
        kalimat = input('\nMasukkan kalimat: ')
        kunci = input('Masukkan kunci: ')
        print("Hasil enkripsi:", enkripsi_poly(kalimat, kunci))
    elif pilihan == 2:
        kalimat = input('\nMasukkan kalimat: ')
        kunci = input('Masukkan kunci: ')
        print("Hasil dekripsi:", dekripsi_poly(kalimat, kunci))
    else:
        print('\nmasukkin pilihannya yang bener saattt!!!')

    isEnough = input('\nudah belooonnn (y/t)?')
    if isEnough == 'y' or isEnough == 'Y':
        break