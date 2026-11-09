import sys
def gerar_farey(n):
	cont=0

	a,b = 0,1
	c,d = 1,n
	e,f = 0,0
	while c<=n:
		cont+=1
		k=(n+b)//d
		a,b,c,d = c,d,(k*c-a),(k*d-b)
	print(cont-1)
gerar_farey(1000000)



