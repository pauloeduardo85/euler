import sys
def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,numero,2):
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
	return conjunto
aux = gerarListaPrimosDivisores(2)
aux2 = gerarListaPrimosDivisores(3)
aux3 = gerarListaPrimosDivisores(4)
cota = 4
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
		sys.exit()
'''
import itertools
import sys
def TuplaMultiplicadas(tupla):
	s = 1
	for i in tupla:
		s *= int(i)
	return s
#gerar lista de primos menor que 10.000
lista_primos = gerarListaPrimos(10000)
lista_tuplas = list(itertools.combinations(lista_primos,2))
lista_tuplas = [TuplaMultiplicadas(x) for x in lista_tuplas]
lista_tuplas = sorted(lista_tuplas)	
for i in range(0,len(lista_tuplas)):
	if lista_tuplas[i+1] - lista_tuplas[i] == 1:
		print(lista_tuplas[i+1],lista_tuplas[i]) 
		sys.exit()
'''
