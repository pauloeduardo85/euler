'''
import sys
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
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
r = len(p) / (i*2 - 1)
#print(len(p), i*2 - 1,r)
#sys.exit()
while r > 0.1:
	#print(r,i)
	i+=1
	v = gerar(i)
	p = list(filter(lambda x: isPrime(x), v))
	r = len(p)/len(v)
print(r,i)
'''
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
r = 10
v = [1]
n = 3
p = 0
r = 10
while r > 0.1:
	somador = (n - 1)
	ultimo = v[-1]
	a1=ultimo + (somador * 1)
	a2=ultimo + (somador * 2)
	a3=ultimo + (somador * 3)
	a4=ultimo + (somador * 4)
	v.append(a1)
	v.append(a2)
	v.append(a3)
	v.append(a4)
	if isPrime(a1):
		p+=1
	if isPrime(a2):
		p+=1
	if isPrime(a3):
		p+=1
	if isPrime(a4):
		p+=1
	r = p / (n*2 - 1)
	n+=2
print(v,p,r,n-2)
	
