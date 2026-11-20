def isPalindromo(numero):
	arr = str(numero)
	return arr[::-1] == arr

def isLych(numero):
	contador = 0
	rev = int(str(numero)[::-1])
	soma = numero + rev
	while contador < 50 and (not isPalindromo(soma)):
		contador += 1
		rev = int(str(soma)[::-1])
		soma = soma + rev
	return contador < 50 and isPalindromo(soma)
#print(isLych(47))
print(isLych(1292))
j = 0
for i in range(0,10000): #0,1,2,3... entra na conta
	if isLych(i):
		j+=1
print(10000-j)
