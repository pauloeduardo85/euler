import sys
power = 5
limite = 9**(power + 1)
def canWriteAsNPower(i,power):
	digit_array = list(map(int, str(i)))
	soma=0
	#print(digit_array)
	for q in digit_array:
		soma += q**power
	print(soma,i)
	return soma == i
#canWriteAsNPower(1634,4)
#canWriteAsNPower(92727,5)
#sys.exit()
for i in range(2,limite+1):
	if canWriteAsNPower(i,power):
		print(i)


