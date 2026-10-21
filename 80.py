import math
from decimal import Decimal, getcontext
getcontext().prec = 100
def isIrrational(numero):
	sq = math.sqrt(numero)
	return sq.is_integer()
lista = list(range(1,101))
lista_raizes = [math.sqrt(Decimal(x)) for x in lista]
print(lista_raizes)
