import sys
dic = dict()
def quantosNumerosCollatz(n):
	if n in dic:
		return dic[n]
	r = n
	v = []
	while r != 1:
		v.append(r)
		if r % 2 == 0:
			r = int(r/2)
		else:
			r = int(3*r + 1)
	dic[n] = len(v)+1
	return dic[n]
maior = -1
start = 0

print(quantosNumerosCollatz(13))
print(quantosNumerosCollatz(8))

for i in range(13,1000000):
	g = quantosNumerosCollatz(i)
	if g > maior:
		maior = g
		start = i
print(maior, start)
