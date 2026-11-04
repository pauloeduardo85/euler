#soma = 2
#for n in range(14):
#	soma = soma << 1
#print(soma)
soma = 2 << 999
digit_array = list(map(int, str(soma)))
print(digit_array)
print(sum(digit_array))
