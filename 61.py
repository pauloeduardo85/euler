import math
def isTriangle(n):
	delta = 1 + (8*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 2
	return teste.is_integer()
def isSquare(n):
	return (math.sqrt(n)).is_integer()
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

lista_triangle = list(filter(lambda x: isTriangle(x), range(1000,10000)))
lista_square = list(filter(lambda x: isSquare(x), range(1000,10000)))
lista_penta = list(filter(lambda x: isPen(x), range(1000,10000)))
lista_hex = list(filter(lambda x: isHex(x), range(1000,10000)))
lista_hepta = list(filter(lambda x: isHepta(x), range(1000,10000)))
lista_octa = list(filter(lambda x: isOcto(x), range(1000,10000)))
soma=0
for t in lista_triangle:
	for s in filter(lambda x: int(str(t)[-2:]) == int(str(x)[:2]), lista_square):
		for p in filter(lambda x: int(str(s)[-2:]) == int(str(x)[:2]), lista_penta):
			for h in filter(lambda x: int(str(p)[-2:]) == int(str(x)[:2]), lista_hex):
				for h7 in filter(lambda x: int(str(h)[-2:]) == int(str(x)[:2]), lista_hepta):
					for o in filter(lambda x: int(str(h7)[-2:]) == int(str(x)[:2]), lista_octa):
						print(t,s,p,h,h7,o)
