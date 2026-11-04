import sys
sys.set_int_max_str_digits(3000000)
a = 28433
a = a << 7830457
a += 1
s = str(a)
print(s[-10:])
