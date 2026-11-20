import sys
import itertools
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
	conjunto = filter(lambda x: isPrime(x), conjunto)
	ret+=conjunto
	return ret
topo=10**6
v=gerarListaPrimos(topo)
dic = dict()
for numero in v:
	dic[numero] = numero
maior = -1
longest = -1
longest_sub = []
for pedaco in range(2,len(v)-1):
	if pedaco > longest:
		for i in range(0,len(v)):
			sub = v[i:pedaco]
			if len(sub)>longest and sum(sub) in dic:
				maior = sum(sub)
				longest = len(sub)
				print(maior,longest)
print(maior,longest,"fim")
