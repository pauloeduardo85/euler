import math

def is_relatively_prime(a,b):
	return math.gcd(a,b) == 1
'''
def euler_totient_function(i):
	lista = range(1,i+1)
	lista = filter(lambda x: is_relatively_prime(i,x), lista)
	return len(list(lista))
'''
maior = -1
n = 0
for i in range(2,1000001):
	print(i)
	r = i / euler_totient_function(i)
	if r > maior:
		maior = r
		n = i
print(n)
