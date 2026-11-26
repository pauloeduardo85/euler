import math
import sys
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
def gerarListaPrimos(limite):
	if limite % 2 == 0:
		limite+=1
	ret = [2]
	conjunto = range(3,limite,2)
	conjunto = list(filter(lambda x: isPrime(x), conjunto))
	ret+=conjunto
	return ret
primos = gerarListaPrimos(7071)
#primos = gerarListaPrimos(7)
#print(primos, len(primos))
#sys.exit()
soma = 0
for a in primos:
	for b in primos:
		for c in primos:
			if a**2+b**3+c**4 <= 50000000:
				soma+=1
print(soma)
