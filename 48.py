def greet():
    print("Hello! Welcome to Python.")
def selfpower(n):
	return n**n
numbers = list(range(1001))
#digit_array = list(map(int, str(numbers)))
soma=0
for i in numbers:
	soma+=selfpower(i)
print(soma-1)

#9110846700
