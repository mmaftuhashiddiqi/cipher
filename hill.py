# Main Program

n = 4

keyMatrix = [[0] * n for i in range(n)]

# Generate vector for the message
messageVector = [[0] for i in range(n)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(n)]

# generate key matrix
def getKeyMatrix(key):

	k = 0
	for i in range(n):
		for j in range(n):
			keyMatrix[i][j] = ord(key[k].upper()) % 65
			k += 1

# hill encryption
def encrypt(message, key):

	# matrix key
	getKeyMatrix(key)

	# Generate vector for the message
	for i in range(n):
		messageVector[i][0] = ord(message[i]) % 65

	# cipher matrix
	for i in range(n):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(n):
				cipherMatrix[i][j] += (keyMatrix[i][x] * messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26
	# print(cipherMatrix)

	# cipher string
	CipherText = []
	for i in range(n):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	# cipher array to cipher text
	return "".join(CipherText)


# CLI Program
import os

while True:
	os.system('clear') # for macos
	# os.system('cls') # for winos

	if True:
		message = input('\nMasukkan kalimat: ')
		key = input('Masukkan kunci: ')
		print('the encryption is:', encrypt(message, key))

	isEnough = input('\nudah belooonnn (y/t)?')
	if isEnough == 'y' or isEnough == 'Y':
		break

# message = "ACTA"
# key = "GYBNQKURPABCDEFG"