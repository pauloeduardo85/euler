def greet():
    print("Hello! Welcome to Python.")
def fatorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return fatorial(n-1) * n
digit_array = list(map(int, str(fatorial(100))))
print(sum(digit_array))
