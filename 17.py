um = ["one","two","three","four","five","six","seven","eight","nine"]
dois = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
dezenas = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
centenas = ["hundred"]

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
EscreverNumeroPorExtenso(115)
EscreverNumeroPorExtenso(899)
