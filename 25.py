contador = 3
a = 1
b = 1

c = a+b
while len(str(c)) < 1000:
	a = b
	b = c
	c = a+b
	contador += 1
print(a,b,c,contador)
