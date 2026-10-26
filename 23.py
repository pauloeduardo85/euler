import itertools
def gerarDivisoresMenoresQueNumero(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	ret = ret+v[::-1]
	del ret[-1]	
	return ret
def isAbudante(numero):
	return sum(gerarDivisoresMenoresQueNumero(numero)) > numero
#print(gerarDivisoresMenoresQueNumero(28), isAbudante(28))
#print(gerarDivisoresMenoresQueNumero(12), isAbudante(12))

limite = 28123
abundantes = []
for i in range(12,limite+1):
	if isAbudante(i):
		abundantes.append(i)
cannot = []
for i in range(0,len(abundantes)):
	for j in range(0,len(abundantes)):
		if abundantes[i] + abundantes[j] <= limite and (not isAbudante(abundantes[i] + abundantes[j])):
			cannot.append(abundantes[i] + abundantes[j])
print(cannot,sum(cannot))
