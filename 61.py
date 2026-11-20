import math
def isTriangle(n):
	delta = 1 + (8*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 2
	return teste.is_integer()
def isSquare(n):
	return (math.sqrt(i)).is_integer()
def isPen(n):
	delta = 1 + (24*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 6
	return teste.is_integer()
def isHex(n):
	delta = 1 + (8*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 4
	return teste.is_integer()
def isHepta(n):
	delta = 9 + (40*n)
	delta = math.sqrt(delta)
	teste = 3 + delta
	teste = teste / 10
	return teste.is_integer()
def isOcto(n):
	delta = 4 + (12*n)
	delta = math.sqrt(delta)
	teste = 2 + delta
	teste = teste / 6
	return teste.is_integer()
def isCyclicAtoB(a,b):
	doisUltimosDigitosDeA = str(a)[-2:]
	doisPrimeirosDigitosDeB = str(b)[:2]
	return doisUltimosDigitosDeA == doisPrimeirosDigitosDeB
lista = list(range(1000,10000))
print(lista)
