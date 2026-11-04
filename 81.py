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
#carregar cache
cache = copy.deepcopy(mtx)
for i in range(0,len(cache)):
	for j in range(0,len(cache[i])):
		cache[i][j] = -1
#print(cache)
def MaiorDeDois(x,y):
	if x > y:
		return x
	return y
def Maximo(i,j):
	if cache[i][j] != -1:
		return cache[i][j]
	if i == len(mtx) - 1 and j == len(mtx) - 1:
		cache[i][j] = mtx[i][j]
		return cache[i][j]
	if i == len(mtx) - 1:
		cache[i][j] = mtx[i][j] + Maximo(i,j+1)
		return cache[i][j]
	if j == len(mtx) - 1:
		cache[i][j]=mtx[i][j] + Maximo(i+1,j)
		return cache[i][j]
	maior = MaiorDeDois(Maximo(i+1,j), Maximo(i,j+1))
	cache[i][j] = maior + mtx[i][j]
	return cache[i][j]
print(Maximo(0,0))
#print(cache)
