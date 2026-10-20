import sys
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,numero,2):
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
def gerarListaPrimosDivisores(numero):
	conjunto = gerarListaPrimos(numero)
	conjunto = list(filter(lambda x: numero % x == 0, conjunto))
	return conjunto
def s(n,m):
	conjunto = gerarListaPrimosDivisores(n**15+1)
	conjunto = list(filter(lambda x: x < m, conjunto))
	return sum(conjunto)  
cache = gerarListaPrimos(10**8)
print(cache)
