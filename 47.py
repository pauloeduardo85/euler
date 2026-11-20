import sys
listadeprimos=[]
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
	conjunto = list(filter(lambda x: isPrime(x), conjunto))
	ret+=conjunto
	return ret
def gerarListaPrimosDivisores(numero):
	conjunto = list(filter(lambda x: x <= numero and numero % x == 0, listadeprimos))
	return conjunto
aux = gerarListaPrimosDivisores(2)
aux2 = gerarListaPrimosDivisores(3)
aux3 = gerarListaPrimosDivisores(4)
cota = 4
topo = 10**6
listadeprimos = gerarListaPrimos(topo)
for i in range(2,10**6):
	d1 = aux
	d2 = aux2
	d3 = aux3
	d4 = gerarListaPrimosDivisores(i+3)
	aux = d2
	aux2 = d3
	aux3 = d4
	if len(d1) == cota and len(d2) == cota and len(d3) == cota and len(d4) == cota:
		print(i,i+1,i+2, i+3)
		print("achou")
		sys.exit()
