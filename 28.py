v = [1]
n = 3
while n <= 1001:
	somador = (n - 1)
	ultimo = v[-1]
	v.append(ultimo + (somador * 1))
	v.append(ultimo + (somador * 2))
	v.append(ultimo + (somador * 3))
	v.append(ultimo + (somador * 4))
	n+=2
print(v)
print(sum(v))
