import sys
def gerar_farey(n):
	a,b = 0,1
	c,d = 1,n
	e,f = 0,0
	while c<=n:
		if c==3 and d==7:
			print(a,b)
			sys.exit()
		k=(n+b)//d
		a,b,c,d = c,d,(k*c-a),(k*d-b)
gerar_farey(1000000)



