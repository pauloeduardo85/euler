import math
def isHex(n):
	delta = 1 + (8*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 4
	return teste.is_integer()
def isPen(n):
	delta = 1 + (24*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 6
	return teste.is_integer()
def isSquare(n):
	return (math.sqrt(i)).is_integer()
lista = range(1000,10000)
