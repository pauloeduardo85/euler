L = 1000
for l in range(1,L):
	for a in range(1,l):
		for b in range(a+1,l):
			for c in range(b+1,l):
				if a+b+c == l and (c**2 == b**2 + a**2):
					print(a,b,c,l)				
