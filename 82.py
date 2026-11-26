import copy
import sys
#carregar a matrix
mtx = []
with open('81_matrix_sample.txt', 'r') as file:
#with open('81_matrix.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip().split(",")
        numeros = [int(x) for x in cleaned_line]      
        mtx.append(numeros)
#print(mtx)
#sys.exit()
#carregar cache
cache = copy.deepcopy(mtx)
for i in range(0,len(cache)):
	for j in range(0,len(cache[i])):
		cache[i][j] = -1
#print(cache)
#sys.exit()
def MenorDeDois(x,y):
	if x < y:
		return x
	return y
def Minimo(i,j,up = False):
	if cache[i][j] != -1:
		return cache[i][j]
	if j==len(mtx)-1:
		cache[i][j]=mtx[i][j]
		return cache[i][j]
	if i==0 and up:
		 cache[i][j]=mtx[i][j] + Minimo(i,j+1)
		 return cache[i][j]
	if i==0 and j==0:
		 menor = MenorDeDois(Minimo(i,j+1),Minimo(i+1,j))
		 cache[i][j]=mtx[i][j] + menor
		 return cache[i][j]
	if i==0 and not up:
		 menor = MenorDeDois(Minimo(i,j+1),Minimo(i+1,j))
		 cache[i][j]=mtx[i][j] + menor
		 return cache[i][j]
	if i!=0 and up:
		 menor = MenorDeDois(Minimo(i,j+1),Minimo(i-1,j))
		 cache[i][j]=mtx[i][j] + menor
		 return cache[i][j]
	if i==len(mtx):
		 cache[i][j]=mtx[i][j] + Minimo(i,j+1)
		 return cache[i][j]
	return cache[i][j]
for i in range(0,len(mtx[0])):
	print(Minimo(i,0))
