import sys
longest = []
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
def somaDivisoresProprios(numero):
	return sum(gerarDivisoresMenosNumero(numero))
def gerarAmicableChain(numero):
	if(isPrime(numero)):
		return []
	v = [numero]
	i = somaDivisoresProprios(numero)
	while i != numero:
		v.append(i)
		i = somaDivisoresProprios(i)
	return v
print(gerarAmicableChain(220))
print(gerarAmicableChain(12496))
print(gerarAmicableChain(5))
print(gerarAmicableChain(15472))
