def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,numero,2):
		if numero % i == 0:
			return False
	return True
def gerarDivisores(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	return ret+v[::-1]
def gerarDivisoresMenosNumero(numero):
	ret = gerarDivisores(numero)
	return ret[0:len(ret)-1]
def d(numero):
	return sum(gerarDivisoresMenosNumero(numero))
def isAmicablePair(x,y):
	sx = d(x)
	sy = d(y)
	return sx == y and sy == x
v = range(2,10000)
lista = list()
for i in v:
	for j in v:
		if i!=j and isAmicablePair(i,j):
			w = sorted([i,j])
			if w not in lista:
				print(w)
				lista.append(w)
print(lista)

