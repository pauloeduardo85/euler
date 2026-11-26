def number_increasing(num):
	s = str(num)
	for i in range(0,len(s)):
		for j in range(i+1,len(s)):
			if int(s[j]) < int(s[i]):
				return False
	return True
def number_decreasing(num):
	s = str(num)
	s = s[::-1]
	return number_increasing(int(s))
def number_bouncy(num):
	return (not number_increasing(num)) and (not number_decreasing(num)) 
ratio = 0
bouncy=[]
i = 1
while ratio != 0.99:
	if number_bouncy(i):
		bouncy.append(i)
	ratio = len(bouncy) / i
	i+=1
print(i-1)
