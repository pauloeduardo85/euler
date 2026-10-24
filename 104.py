v = [1,1]
while True:
	v.append(v[-1]+v[-2])
	s = str(v[-1])
	s10u = s[-9:] #10 ultimos
	s10p = s[:9] #10 primeiros
	print(s10u,"foi")
