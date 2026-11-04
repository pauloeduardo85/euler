import math

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
	#conjunto = list(filter(lambda x: x % 2 != 0, conjunto))
	conjunto = list(filter(lambda x: isPrime(x), conjunto))
	ret+=conjunto
	return ret
def gerarListaPrimosDivisores(numero):
	conjunto = gerarListaPrimos(numero)
	conjunto = list(filter(lambda x: numero % x == 0, conjunto))
	if isPrime(numero):
		conjunto.append(numero)
	return conjunto
def multiplicaFracao(up1,down1,up2,down2):
	upf =  up1 * up2
	downf = down1 * down2
	#print(upf,downf)
	gcd=math.gcd(upf,downf)
	upf = upf / gcd
	downf = downf/gcd
	return [int(upf),int(downf)]
def calcular_Totient(numero):
	divisores=gerarListaPrimosDivisores(numero)
	v = [numero,1]
	for i in divisores:
		#print(i)
		v = multiplicaFracao(v[0],v[1],i-1,i)
	return v
maior = -1
for i in range(2,1000001):
	t = calcular_Totient(i)
	r = i / t[0]
	#print(t,i,r)
	if r > maior:
		maior = r
		print(i)
