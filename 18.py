import copy
import sys
t = [[75]
,[95,64]
,[17,47,82]
,[18,35,87,10]
,[20,4,82,47,65]
,[19,1,23,75,3,34]
,[88,2,77,73,7,63,67]
,[99,65,4,28,6,16,70,92]
,[41,41,26,56,83,40,80,70,33]
,[41,48,72,33,47,32,37,16,94,29]
,[53,71,44,65,25,43,91,52,97,51,14]
,[70,11,33,28,77,73,17,78,39,68,17,57]
,[91,71,52,38,17,14,91,43,58,50,27,29,48]
,[63,66,4,68,89,53,67,30,73,16,69,87,40,31]
,[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]
cache = copy.deepcopy(t)
for i in range(0,len(cache)):
	for j in range(0,len(cache[i])):
		cache[i][j] = -1
#print(cache)
#print(t)
#sys.exit()
def MaiorDeDois(x,y):
	if x > y:
		return x
	return y
def MaxTriangle(i,j):
	if cache[i][j] != -1:
		return cache[i][j]
	if i == len(t) - 1:
		cache[i][j] = t[i][j]
		return cache[i][j] 
	#el1 = MaxTriangle(i+1,j)
	#el2 = MaxTriangle(i+1,j+1)
	maior = MaiorDeDois(MaxTriangle(i+1,j), MaxTriangle(i+1,j+1))
	return maior + t[i][j]
print(MaxTriangle(0,0))

