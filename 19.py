#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import datetime
#d = 1
#m = 1
#x = datetime.datetime(1901, d, m)
#print(x) 
#print(x.strftime("%w")) # 0 sunday

meses = range(1, 13)
anos = range(1901, 2001)
contador = 0
for a in anos:
	for m in meses:
		x = datetime.datetime(a, m, 1)
		if x.strftime("%w") == '0':
			contador+=1
print(contador)
