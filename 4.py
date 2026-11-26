def ehPalindromo(numero):
	arr = str(numero)
	return arr[::-1] == arr
maior = -1
for i in range(999,100,-1):
	for j in range(999,100,-1):
		if ehPalindromo(i*j) and i*j > maior:
			 maior = i*j
print(maior)
