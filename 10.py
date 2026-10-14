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
topo=2*10**6
v=gerarListaPrimos(topo)
print(v)
print(sum(v))
