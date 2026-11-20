#print("hello world")
contador = 0
limite = 560000
i = 1
soma = 0
while contador < limite:
	#print(i)
	if i % 2 == 1:
		soma += i**2
	i+=1
	contador+=1
print(soma)
print(contador)

