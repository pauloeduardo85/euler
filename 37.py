def isPrime(numero):
	if numero == 1:
		return False
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,numero,2):
		if numero % i == 0:
			return False
	return True
def proximoPrimo(numero):
	ret = numero+1
	if ret % 2 == 0:
		ret+=1
	while not isPrime(ret):
		ret+=2
	return ret
def isTruncable(numero):
	v = str(numero)
	while len(v) > 0:
		#print(v)
		if not isPrime(int(v)):
			return False
		v = v[1::]
	v = str(numero)
	while len(v) > 0:
		#print(v)
		if not isPrime(int(v)):
			return False
		v = v[0:len(v)-1]
	return True
isTruncable(3797)
r = 10
contador = 0
while contador < 11:
	r = proximoPrimo(r)
	#print(r)
	if isTruncable(r):
		contador+=1
		print(r)
