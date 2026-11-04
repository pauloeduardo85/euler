v = [0,1,2,3,4,5,6,7,8,9]
lista = list()
soma=0
for d1 in v:
	for d2 in filter(lambda x: x != d1, v):
		for d3 in filter(lambda x: x != d1 and x!= d2, v):
			for d4 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x in (0,2,4,6,8), v):
				for d5 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x!=d4, v):
					for d6 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x!=d4 and x!=d5 and x in (0,5), v):				
						for d7 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x != d4 and x!=d5 and x!=d6, v):
							for d8 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x != d4 and x!=d5 and x!=d6 and x!=d7, v):
								for d9 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x != d4 and x!=d5 and x!=d6 and x!=d7 and x!=d8, v):
									for d10 in filter(lambda x: x != d1 and x != d2 and x!=d3 and x != d4 and x!=d5 and x!=d6 and x!=d7 and x!=d8 and x!=d9, v):
										w=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
										d234 = str(d2) + str(d3) + str(d4)
										d345 = str(d3) + str(d4) + str(d5)
										d456 = str(d4) + str(d5) + str(d6)
										d567 = str(d5) + str(d6) + str(d7)
										d678 = str(d6) + str(d7) + str(d8)
										d789 = str(d7) + str(d8) + str(d9)
										d8910 = str(d8) + str(d9) + str(d10)
										
										if int(d345) % 3 == 0 and int(d567) % 7 == 0 and int(d678) % 11== 0 and int(d789) % 13 == 0 and int(d8910) % 17 == 0:
											s=""
											for el in w:
												s+=str(el)
											soma+=int(s)
print(soma)
