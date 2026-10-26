def isPrime(numero):
	if numero % 2 == 0:
		return numero == 2
	for i in range(3,int(numero**0.5)+1,2):
		if numero % i == 0:
			return False
	return True
	
conjunto = list(range(1001,9999,2))
conjunto = list(filter(lambda x: isPrime(x), conjunto))
for i in range(0,len(conjunto)):
	for j in range(i+1,len(conjunto)):
		for k in range(j+1,len(conjunto)):
			if conjunto[j] - conjunto[i] == conjunto[k] - conjunto[j]:
				if sorted(list(map(int, str(conjunto[i])))) == sorted(list(map(int, str(conjunto[j])))) == sorted(list(map(int, str(conjunto[k])))):
					print(conjunto[i], conjunto[j], conjunto[k])
		
