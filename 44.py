import math
import sys
def isPen(n):
	delta = 1 + (24*n)
	delta = math.sqrt(delta)
	teste = 1 + delta
	teste = teste / 6
	return teste.is_integer()
def CalculaPen(n):
	ret = 3*n - 1
	ret = ret * n
	ret = ret / 2
	return int(ret)
v=[1,5,12]
n=3
#print(CalculaPen(3))
#sys.exit()
while True:
	n+=1
	v.append(CalculaPen(n))
	ultimo = v[-1]
	for el in v[0:len(v)-1][::-1]:
		if isPen(ultimo-el) and isPen(ultimo+el):
			print(ultimo - el)
			sys.exit()
