import itertools
def gerarDivisoresMenoresQueNumero(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	ret = ret+v[::-1]
	del ret[-1]	
	return ret
def gerarLista():
	ret=[]
	for i in range(12,28124):
		divisores = gerarDivisoresMenoresQueNumero(i)
		if sum(divisores) > i:
			ret.append(i)
	return ret
#print(gerarDivisoresMenoresQueNumero(28))
#print(gerarLista())
lista = gerarLista()
#combinatios = itertools.combinations_with_replacement(lista, 2)
#combinatios = list(combinatios)
#print(combinatios)
combinatios = []
for i in lista:
	for j in lista:
		combinatios.append(i+j)
final = list(filter(lambda x: x not in combinatios, range(12,28124)))
print(final)

