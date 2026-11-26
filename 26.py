def get_cycle_length(d: int) -> int:
    # Remove factors of 2 and 5 which cause terminating decimals
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    
    if d == 1:
        return 0 # Terminating decimal
        
    # Find the smallest k such that 10^k ≡ 1 (mod d)
    remainder = 10 % d
    length = 1
    while remainder != 1:
        remainder = (remainder * 10) % d
        length += 1
        
    return length
maior = 0
for i in range(2,1000):
	c=get_cycle_length(i)
	if c > maior:
		maior = c
		print(c,i)
	
