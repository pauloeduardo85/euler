'''
import math
def how_many_digits(n):
	return len(str(n))
def sum_integer_fraction(integ,up,down):
	n = integ * down
	n = n + up
	gcd = math.gcd(n, down)
	n = int(n / gcd)
	down = int(down / gcd)
	return [n,down]
fracao_de_baixo = sum_integer_fraction(2,1,2)
final = sum_integer_fraction(1,fracao_de_baixo[1],fracao_de_baixo[0])
contagem = 2
res=0
while contagem < 1001:
	contagem+=1
	fracao_de_baixo=sum_integer_fraction(2,fracao_de_baixo[1],fracao_de_baixo[0])
	final = sum_integer_fraction(1,fracao_de_baixo[1],fracao_de_baixo[0])
	if how_many_digits(final[0]) > how_many_digits(final[1]):
		res+=1
print(res)
'''
p, q = 3, 2
count = 0

for _ in range(1000):
    if len(str(p)) > len(str(q)):
        count += 1
    p, q = p + 2 * q, p + q

print(count)  # 153
