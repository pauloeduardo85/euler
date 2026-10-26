import sys
def gerarRotacoes(numero):
	rotacoes = [int(numero)]
	v = str(numero)
	v = v[1::] + v[0]
	while v != str(numero):
		rotacoes.append(int(v))
		v = v[1::] + v[0]
	return rotacoes
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
#print(gerarRotacoes(73))
#print(gerarRotacoes(197))
todos = []
for numero in range (2,1000000):
	print(numero)
	if isPrime(numero):
		rotacoes = gerarRotacoes(numero)
		rotacoes = list(filter(lambda x: not isPrime(x), rotacoes))
		if len(rotacoes) == 0:
			todos.append(numero)
print(todos)
print(len(todos))
