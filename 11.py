def gerarDivisores(numero):
	ret = []
	for i in range(1,int(numero**0.5)+1):
		if numero % i == 0:
			ret.append(i)
	v = [int(numero / x) for x in ret]
	return ret+v[::-1]
limite = 500
i = 1
divisores = []
while len(divisores) <= limite:
	soma = sum(range(1,i+1))
	divisores = gerarDivisores(soma)
	print(soma)
	print(divisores)
	i+=1

