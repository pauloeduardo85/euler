maior=0
for a in range(1,100):
	for b in range(1,100):
		pot = a**b
		numeros = [int(x) for x in str(pot)]
		if sum(numeros)>maior:
			maior = sum(numeros)
print(maior)

