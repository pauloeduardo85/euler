for a in range(-1000,1001):
	for b in range(-1000,1001):
		a+b
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
booleano = True
contagem=0
