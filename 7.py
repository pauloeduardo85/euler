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
	#conjunto = list(filter(lambda x: x % 2 != 0, conjunto))
	conjunto = list(filter(lambda x: isPrime(x), conjunto))
	ret+=conjunto
	return ret
v = [2]
i = 3
while len(v) < 10001:
	if isPrime(i):
		v.append(i)
	i+=2
print(v)

