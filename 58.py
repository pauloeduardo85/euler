def isPrime(numero):
	if numero == 1:
		return False
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,numero,2):
		if numero % i == 0:
			return False
	return True
def gerar(limite):
	v = [1]
	n = 3
	while n <= limite:
		somador = (n - 1)
		ultimo = v[-1]
		v.append(ultimo + (somador * 1))
		v.append(ultimo + (somador * 2))
		v.append(ultimo + (somador * 3))
		v.append(ultimo + (somador * 4))
		n+=2
	return v
i = 7
v = gerar(i)
p = list(filter(lambda x: isPrime(x), v))
r = len(p)/len(v)
while r > 0.1:
	i+=1
	v = gerar(i)
	p = list(filter(lambda x: isPrime(x), v))
	r = len(p)/len(v)
print(r,n)

