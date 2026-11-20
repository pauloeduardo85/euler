import sys
cache = dict()
def fatorial(n):
	if n in cache:
		return cache[n]
	if n == 0 or n == 1:
		cache[n] = 1
	else:
		cache[n] = fatorial(n-1) * n
	return cache[n]
contador=0
for n in range(1,101):
	for r in range(1, n+1):
		c = fatorial(n) / (fatorial(r) * fatorial(n-r))
		if c > 1000000:
			print(n,r,c)
			#sys.exit()
			contador += 1
print(contador)
