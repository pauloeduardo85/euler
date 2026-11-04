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
i =  9
while True:
	if not isPrime(i):
		#print(i)
		primos_menores = gerarListaPrimos(i)
		booleano = False
		for p in primos_menores:
			r = (i - p) / 2
			r = math.sqrt(r)
			if r.is_integer():
				booleano = True
		if not booleano:
			print(i, "morreu")
			sys.exit()
	i+=2

