from decimal import Decimal, getcontext
getcontext().prec = 105
soma = 0
for inteiro in range(1,101):
	number = Decimal(inteiro)
	sqrt_result = number.sqrt()
	if sqrt_result % 1 != 0:
		#print(inteiro,sqrt_result)
		s = str(sqrt_result).split(".")
		soma += sum([int(x) for x in s[1][:100]])
print(soma)
