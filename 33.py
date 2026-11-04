def getUnidade(numero):
	ret = numero % 10
	return ret
def getDezena(numero):
	ret = numero - getUnidade(numero)
	return int (ret / 10)
def isDigitCancelling(x,y):
	# x1x2/y1y2
	d1 = getDezena(x)
	u1 = getUnidade(x)
	d2 = getDezena(y)
	u2 = getUnidade(y)
	if x % 10 == 0 and y % 10 == 0:
		return False
	if d1 == u1 or d2 == u2:
		return False
	if u2 != 0 and d1/u2 == x/y and d2==u1:
		return True
	return False
for i in range(10,100):
	for j in range(i+1,100):
		if isDigitCancelling(i,j):
			print(f"{i}/{j}") #formatar string
#echo "operacao x operacao | bc"
