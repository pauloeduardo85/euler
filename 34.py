cache = dict()
def fatorial(n):
	if n in cache:
		return cache[n]
	if n == 0 or n == 1:
		cache[n] = 1
	else:
		cache[n] = fatorial(n-1) * n
	return cache[n]
v = [0,1,2,3,4,5,6,7,8,9]
fat = list([fatorial(x) for x in v])
for i in range(3,fat[-1]+1):
	digit_array = list(map(int, str(i)))
	soma = 0
	for j in digit_array:
		soma = soma + fat[j]
	if soma == i:
		print(i) 
