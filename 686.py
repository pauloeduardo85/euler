import sys
sys.set_int_max_str_digits(1000000)
def p(L,n):
	contador = 0
	ret = 0
	i = 2
	s = str(L)
	length=len(s)
	while contador < n:
		ret+=1
		if str(i)[:length] == s:
			contador+=1
		i = i << 1
	return ret
v=[]
d=[]
for i in range(45,61):
	v.append(p(123,i))
print(v)
for i in range(1,len(v)):
	d.append(v[i]-v[i-1])
#print(d)


sys.exit()
padrao=[196, 289, 196, 289, 196, 485, 485]

i = 45
m = 12710
contador=0
while i <= 678910:
	#print(p(123,i))
	i+=1
	m+=padrao[contador]
	contador+=1
	contador = contador % len(padrao)
	print(m,contador,padrao[contador],i)
