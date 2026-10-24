def contemMesmosDigitos(a,b):
	sx = [str(x) for x in str(a)]
	sy = [str(x) for x in str(b)]
	return sorted(sx) == sorted(sy)
x = 1
while True:
	if contemMesmosDigitos(x,2*x) and contemMesmosDigitos(x,3*x) and contemMesmosDigitos(x,4*x) and contemMesmosDigitos(x,5*x) and contemMesmosDigitos(x,6*x):
		print(x)
		break
	x+=1
	
