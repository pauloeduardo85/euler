def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
def gerarDivisores(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	return set(ret+v[::-1])
aux = gerarDivisores(1)
contagem = 0
for n in range(2,10**7):
	div_n = len(gerarDivisores(n))
	div_n_plus = len(gerarDivisores(n+1))
	if div_n == div_n_plus:
		contagem+=1
print("contagem:",contagem)
	
