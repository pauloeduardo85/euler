def isPrime(numero):
	try:
		if numero % 2 == 0:
			return numero == 2
		for i in range(3,int(numero**0.5)+1,2):
			if numero % i == 0:
				return False
		return True
	except:
		return False
def Formula(a,b,n):
	soma = n**2
	soma += n * a
	soma += b
	return soma
def AteOndeVaiN(a,b):
	n = 0
	while isPrime(Formula(a,b,n)):
		n+=1
	return n-1
#print(AteOndeVaiN(1,41))
#print(AteOndeVaiN(-79,1601))
maior = -1
for a in range(-1000,1001):
	for b in range(-1000,1001):
		#quantos primos 0<=n<=limite
		x = AteOndeVaiN(a,b)
		if x > maior:
			maior = x
			print(a,b)
