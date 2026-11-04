import sys
#lembrete = [None] * (10**6 + 1)
limite = (10**7) + 1
lembrete = [0] * (limite+1)
lembrete[1] = 1
#sys.exit()
def somarQuadrados(numero):
	s = str(numero)
	numeros = [int(x) for x in s]
	numeros = list(numeros)
	numeros = numeros[::-1]
	soma = 0
	for i in range(0,len(numeros)):
		soma += numeros[i]**2
	return soma	
def calcularFim(numero):
	if(numero <= limite and lembrete[numero] != 0):
		return lembrete[numero]
	i = somarQuadrados(numero)
	while i != 89 and i != 1:
		i = somarQuadrados(i)
	lembrete[numero] = i
	return i
lista = list(range(1,limite))
lista = [calcularFim(x) for x in lista]
lista = list(filter(lambda x: x == 89, lista))
print(len(lista))
