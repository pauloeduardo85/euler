import itertools
def gerarDivisoresMenoresQueNumero(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	return ret+v[::-1]
def isAbundant(numero):
	return sum(gerarDivisoresMenoresQueNumero(numero)) - numero > numero
def gerarListaAbundantes(inferior, superior):
	while not isAbundant(inferior):
		inferior+=1
	while not isAbundant(superior):
		superior-=1
	ret = [inferior]
	conjunto = range(inferior,superior+1)
	conjunto = filter(lambda x: isAbundant(x), conjunto)
	ret+=conjunto
	return ret[2::] #gambi porque duplicou o primeiro elemento
def TuplaSomada(tupla):
	s = 0
	for i in tupla:
		s += int(i)
	return s
limite = 28123
lista_abundantes = gerarListaAbundantes(1,limite)
# combinar a lista de abundantes 2 a 2 usando libs do próprio python
# pode duplicar elementos
combinacoes = itertools.combinations_with_replacement(lista_abundantes,2)
combinacoes_somadas = [TuplaSomada(x) for x in combinacoes]
combinacoes_somadas = list(filter(lambda x: x < limite, combinacoes_somadas))
todos = list(range(12,limite+1))
final = list(filter(lambda x: x not in combinacoes_somadas, todos)) #diff de listas
print(final)
