import math
primosMenoresQueUmMilhao = []
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
	conjunto = list(filter(lambda x:x <= numero and numero % x == 0, primosMenoresQueUmMilhao))
	if isPrime(numero):
		conjunto.append(numero)
	return set(conjunto)
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
	if isPrime(numero):
		return numero-1
	v = [numero,1]
	for i in divisores:
		#print(i)
		v = multiplicaFracao(v[0],v[1],i-1,i)
	return v[0]
primosMenoresQueUmMilhao = gerarListaPrimos(10**6)
n = 10**6
soma = 0
for k in range(1,n+1):
	print(k)
	soma += calcular_Totient(k)
print(soma)

