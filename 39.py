def solucoesPorPerimetro(perimetro):
	contador = 0
	for v1 in range(1,perimetro+1):
		for v2 in range(v1+1,perimetro - v1+1):
			for v3 in range(v2+1, perimetro - v1 - v2+1):
				if v1 < v2 and v2 < v3 and v1+v2+v3 == perimetro and v1**2 + v2**2 == v3**2:
					contador+=1
	return contador
maior = -1
#print(solucoesPorPerimetro(120))
for i in range(1,1001):
	s = solucoesPorPerimetro(i)
	if s > maior:
		maior = s
		print(maior,i)
print(f"maior = {maior}")
