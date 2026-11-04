import sys
sys.set_int_max_str_digits(100000)
a = 1
b = 1
n = 2
aux = -1
comparar = ['1','2','3','4','5','6','7','8','9'] 
while True:
	print(n)
	aux = a
	a = b
	b = aux+b
	s = str(b)
	n+=1
	s10u = sorted(s[-9:]) #10 ultimos
	s10p = sorted(s[:9]) #10 primeiros
	if s10u == comparar and s10p == comparar:
		print(n, "achou")
		break
'''
import math
# https://en.wikipedia.org/wiki/Fibonacci_sequence
'''
