import math
def fibonacci(numero):
	if numero < 2:
		return 1
	return fibonacci(numero-1) + fibonacci(numero-2)
limite = 4 * (10**6)
v = [1,2]
#for i in range(1,limite+1):
#	v.append(fibonacci(i))
while v[-1] < limite:
	v.append(v[-1]+v[-2])
del v[-1]
v = list(filter(lambda x: x % 2 == 0, v))
print(sum(v))
print(v)
