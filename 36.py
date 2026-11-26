def isPalindromo(numero):
	arr = str(numero)
	return arr[::-1] == arr
def isBinaryPalindromo(numero):
	s = f"{numero:b}"
	return isPalindromo(s)
lista = list(range(1,1000001))
lista = list(filter(lambda x: isPalindromo(x) and isBinaryPalindromo(x), lista))

print(lista)
print(sum(lista))
