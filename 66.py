import math
from fractions import Fraction
#Pell's equation
def cf_to_fraction(cf: list[int]) -> Fraction:
  if not cf:
    raise ValueError("Continued fraction list cannot be empty.")
  result = Fraction(cf[-1])
  for term in reversed(cf[:-1]):
    result = term + 1 / result
  return result

def sqrt_continued_fraction_cycle(n):
    a0 = math.isqrt(n)
    if a0 * a0 == n:
        return a0, []
    m = 0
    d = 1
    a = a0
    cycle = []
    while a != 2 * a0:
        m = d * a - m
        d = (n - m * m) // d
        a = (a0 + m) // d
        cycle.append(a)
    return a0, cycle
def sum_fraction(up1,down1,up2,down2):
	n = (up1 * down2) + (up2 * down1)
	d = down1 * down2
	gcd = math.gcd(n,d)
	n = n / gcd
	d = d / gcd
	return [int(n),int(d)]
largest = 0
minimal_d = -1
lista = list(filter(lambda x: not math.sqrt(x).is_integer(), range(0,1001)))
for d in lista:
	a0, cycle = sqrt_continued_fraction_cycle(d)
	cycle = cycle[:-1] if len(cycle) % 2 == 0 else cycle + cycle[:-1]
	cycle.insert(0,a0)
	res=cf_to_fraction(cycle)
	if res.numerator > largest:
		largest = res.numerator
		minimal_d = d
print(minimal_d)
