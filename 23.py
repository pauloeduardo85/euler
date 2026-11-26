import itertools
import sys
def gerarDivisoresMenoresQueNumero(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	ret = ret+v[::-1]
	del ret[-1]	
	return set(ret)
def isAbudante(numero):
	return sum(gerarDivisoresMenoresQueNumero(numero)) > numero
limite = 28123
#print(gerarDivisoresMenoresQueNumero(4))
#sys.exit()
abundantes = list(filter(lambda x: isAbudante(x), range(1,limite+1)))
v = []
for i in abundantes:
	for j in abundantes:
		if i+j <= limite:
			v.append(i+j)
v = set(v)
soma = sum(range(1,limite+1))
print(soma - sum(v))
