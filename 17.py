um = ["one","two","three","four","five","six","seven","eight","nine"]
dois = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
dezenas = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
centenas = ["hundred"]
'''
soma1a9=0
soma10a19=0
somadezenas=0
somacentenas=0

for i in um:
	soma1a9+=len(i)
for i in dois:
	soma10a19+=len(i)
for i in dezenas:
	somadezenas+=len(i)
for i in centenas:
	somacentenas+=len(i)
'''
def EscreverNumeroPorExtenso(numero):
	ret = ""
	u = numero % 10
	d = int(((numero % 100) - u)/10)
	c = int((numero - (d*10) - u)/100)
	print(c,d,u)
	if c != 0:
		ret += um[c-1] + "hundred"
	if c != 0 and (d!=0 or u!=0):
		ret += "and" 
	if d == 1:
		ret += dois[d+u	-1]
	if d == 0 and u != 0:
		ret += um[u-1]
	if d > 1:
		ret += dezenas[d-2]
	if u != 0 and d > 1:
		ret += um[u-1]
	return ret
s="onethousand"
for i in range(1,1000):
	s+=EscreverNumeroPorExtenso(i)
print(s, len(s))
#EscreverNumeroPorExtenso(115)
#EscreverNumeroPorExtenso(899)
#EscreverNumeroPorExtenso(400)
#EscreverNumeroPorExtenso(21)
#EscreverNumeroPorExtenso(1)
#EscreverNumeroPorExtenso(106)
