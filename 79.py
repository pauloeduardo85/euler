v=[319
,680
,180
,690
,129
,620
,762
,689
,762
,318
,368
,710
,720
,710
,629
,168
,160
,689
,716
,731
,736
,729
,316
,729
,729
,710
,769
,290
,719
,680
,318
,389
,162
,289
,162
,718
,729
,319
,790
,680
,890
,362
,319
,760
,316
,729
,380
,319
,728
,716
]
valores = [0] * 10
for i in v:
	u =  i % 10
	d =  int(((i % 100 - u))/10)
	c = int((i - (i % 100))/100)
	teste = 0
	#qual valor mais aparece primeiro 7	
	#qual valor mais aparece por último 9 e 0
	# 0 já apareceu depois do 9 sim
	# qual número mais aparece depois de 7 3
	# qual número mais aparece depois de 3 1
	# qual número mais aparece depois de 1 
	# algum número não aparece 4 5
	# qual número mais aparece antes do 9 2
	# 73162890 ou 73168290 testar
	if d == 9:
		valores[c]+=1
print(valores)



