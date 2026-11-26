import itertools
def isNdigital(n):
	ordenado = [str(x) for x in range(1, len(str(n))+1)]
	ordenado_input = [str(x) for x in str(n)]
	ordenado = sorted(ordenado)
	ordenado_input = sorted(ordenado_input)
	return ordenado == ordenado_input
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
def gerarListaPrimos(inferior, superior):
	while not isPrime(inferior):
		inferior+=1
	while not isPrime(superior):
		superior-=1
	ret = [inferior]
	conjunto = range(inferior,superior+1, 2)
	conjunto = filter(lambda x: isNdigital(x) and isPrime(x), conjunto)
	ret+=conjunto
	return ret[1::] #gambi porque duplicou o 2
def gerarListaPrimosNDigital(n):
	primos = gerarListaPrimos(10**(n-1),10**n)
	return list(filter(lambda x: isNdigital(x), primos))
def TuplaParaInt(tupla):
	s = ""
	for i in tupla:
		s += str(i)
	return int(s)
def pegarNDigitPanPrime(v):
	w = itertools.permutations(v)
	w = [TuplaParaInt(x) for x in w]
	w = list(filter(lambda x: isPrime(x), w))
	return w
v = [9,8,7,6,5,4,3,2,1]
print(pegarNDigitPanPrime(v))
print(pegarNDigitPanPrime(v[1::]))
print(pegarNDigitPanPrime(v[2::]))
print(pegarNDigitPanPrime(v[3::]))
print(pegarNDigitPanPrime(v[4::]))
print(pegarNDigitPanPrime(v[5::]))
print(pegarNDigitPanPrime(v[6::]))
print(pegarNDigitPanPrime(v[7::]))
print(pegarNDigitPanPrime(v[8::]))
