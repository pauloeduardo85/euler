import math
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,numero,2):
		if numero % i == 0:
			return False
	return True
#print(isPrime(13165))
n = 600851475143
limite = math.sqrt(n)
limite = math.ceil(limite)
for i in range(limite,1,-1):
	print(i)
	if n % i == 0 and isPrime(i):
		print(i)
		break
print("fim")
