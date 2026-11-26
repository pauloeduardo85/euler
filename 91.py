import math
import sys
def distancia_entre_pontos(x1,y1,x2,y2):
	el1 = x2 - x1
	el2 = y2 - y1
	el1 = el1**2
	el2 = el2**2
	return math.sqrt(el1+el2)
#print(distancia_entre_pontos(1,1,4,1))
#print(distancia_entre_pontos(4,6,1,2))
#sys.exit()
soma=0
limite=51
w=[]
for x1 in range(0,limite):
	for x2 in range(0,limite):
		for y1 in range(0,limite):
			for y2 in range(0,limite):
				d12 = distancia_entre_pontos(x1,y1,x2,y2)
				d13 = distancia_entre_pontos(x1,y1,0,0)
				d23 = distancia_entre_pontos(x2,y2,0,0)
				if d12 != 0 and d13 != 0 and d23 != 0:
					v = [d12,d13,d23]
					v = sorted(v)
					if round(v[2]**2,2) == round(v[1]**2 + v[0]**2,2): #arredondar é essencial
						soma+=1
print(int(soma / 2))
