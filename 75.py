import sys
def how_many_triangles(L):
	contagem = 0
	for a in range(1,L+1):
		for b in range(a+1, L+1-a):
			for c in range(b+1, L+1-a-b):
				if a+b+c==L:
					if c**2==b**2+a**2:
						contagem+=1
					if contagem > 1:
						return contagem
	return contagem
print(how_many_triangles(12))
print(how_many_triangles(20))
print(how_many_triangles(280))
#sys.exit()
contador = 0
for L in range(1,1500001):
	print(L)
	if how_many_triangles(L) == 1:
		contador+=1
print(contador)
