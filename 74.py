lista = [0] * 1000001
def fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fatorial(n-1) * n
fat = list([fatorial(x) for x in range(0,10)])
def calculaSomaFatorial(numero):
	v = list(map(int, str(numero)))
	vf = [fat[x] for x in v]
	return sum(vf)
def calculaChain(numero):
	v = []
	v.append(numero)
	i = calculaSomaFatorial(v[-1])
	while True:
		v.append(i)
		i = calculaSomaFatorial(v[-1])
		if i in v:
			break
	lista[numero] = len(v)
	return lista[numero]
contagem=0
for n in range(0,1000000):
	if calculaChain(n) == 60:
		contagem+=1
		print(n)
print(f"{contagem} - contagem")
