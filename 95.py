import math
def get_proper_divisors(n):
  divisors = []
  # Loop only up to the integer square root of n
  for i in range(1, math.isqrt(n) + 1):
    if n % i == 0:
      divisors.append(i)
      # Add the paired divisor if it's not a duplicate (like 6*6 = 36)
      if i != n // i:
        divisors.append(n // i)
  return sorted(divisors)[:-1] # menos o próprio número
 
print(get_proper_divisors(220))
print(sum(get_proper_divisors(220)))
