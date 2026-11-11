import copy
import sys
#carregar a matrix
mtx = []
#with open('81_matrix_sample.txt', 'r') as file:
with open('81_matrix.txt', 'r') as file:
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
def Minimo(i,j):
	print(i,j)
	if cache[i][j] != -1:
		return cache[i][j]
	if i==len(mtx)-1 and j==len(mtx)-1:
		cache[i][j]=mtx[i][j]
		return cache[i][j]
	if i==len(mtx)-1 and j<len(mtx)-1:
		cache[i][j]=mtx[i][j]+Minimo(i,j+1)
		return cache[i][j]
	if i<len(mtx)-1 and j==len(mtx)-1:
		cache[i][j]=mtx[i][j]+Minimo(i+1,j)
		return cache[i][j]
	maior=MenorDeDois(Minimo(i+1,j),Minimo(i,j+1))
	cache[i][j]=mtx[i][j]+maior
	return cache[i][j]
print(Minimo(0,0))
