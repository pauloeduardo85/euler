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
def calculaPen(n):
	r = (3*n) - 1
	r = r * 0.5 * n
	return int(r)
#print(isHex(40755))
#print(isPen(40755))
n = 166
p = calculaPen(166)
while not isHex(p):
	n+=1
	p = calculaPen(n)
print(n,p)
