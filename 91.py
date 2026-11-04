import math
# P x1,y1 Q x2,y2
# a2 + b2 = c2
# dP2P1 = sqrt(x2 - x1)^2 + (y2 - y1)^2
def distancia_entre_pontos(x1,y1,x2,y2):
	el1 = x2-x1
	el2 = y2-y1
	el1 = el1*el1
	el2 = el2*el2
	d = math.sqrt(el1+el2)
	return d
limite = 6
soma = 0
for x1 in range(0,limite):
	for x2 in range(0,limite):
		for y1 in range(0,limite):
			for y2 in range(0,limite):
				lados = [distancia_entre_pontos(x1,y1,x2,y2), distancia_entre_pontos(x1,y1,0,0), distancia_entre_pontos(x2,y2,0,0)]
				lados = sorted(lados)
				if lados[0] != 0 and lados[1] != 0 and lados[2] != 0:
					if lados[2]**2 == (lados[0]**2) + (lados[1]**2):
						print(lados)
