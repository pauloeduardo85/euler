with open('81_matrix.txt', 'r') as file:
    for line in file:
        cleaned_line = line.strip()  # Removes trailing \n and whitespace
        print(cleaned_line)
