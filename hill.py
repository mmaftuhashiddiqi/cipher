# Main Program

# hill encryption
def encrypt(message, key):

	n = len(message)

	# key matrix template
	keyMatrix = [[0] * n for i in range(n)]
	# message vector template
	messageVector = [[0] for i in range(n)]
	# cipher matrikx template
	cipherMatrix = [[0] for i in range(n)]

	# key matrix
	k = 0
	for i in range(n):
		for j in range(n):
			keyMatrix[i][j] = ord(key[k].upper()) % 65
			k += 1

	# generate message vector
	for i in range(n):
		messageVector[i][0] = ord(message[i].upper()) % 65

	# cipher matrix
	for i in range(n):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(n):
				cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

	# cipher text
	CipherText = []
	for i in range(n):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	# cipher array to cipher string
	return "".join(CipherText)

# hill decryption
def decrypt(cipherMessage, key):
	print("bentar, belum nemu")


# CLI Program
import os

while True:
    os.system('clear') # for macos
    # os.system('cls') # for winos

    print('Pilih: \n1. Enkripsi Hill\n2. Dekripsi Hill')
    try:
        choices = int(input('\nMasukkan nomor pilihan: '))
    except:
        choices = 0

    if choices == 1:
        message = input('\nMasukkan kalimat: ')
        key = input('Masukkan kunci: ')
        print("Hasil enkripsi:", encrypt(message, key))
    elif choices == 2:
        cipherMessage = input('\nMasukkan kalimat sandi: ')
        key = input('Masukkan key: ')
        print("Hasil dekripsi:", decrypt(cipherMessage, key))
    else:
        print('\nmasukkin pilihannya yang bener saattt!!!')

    isEnough = input('\nudah belooonnn (y/t)?')
    if isEnough == 'y' or isEnough == 'Y':
        break

# message = "ACTA"
# key = "GYBNQKURPABCDEFG"