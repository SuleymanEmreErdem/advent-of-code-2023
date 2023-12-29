import string

with open('input.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

symbols = []
numbers = []
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
res = 0

for i, line in enumerate(lines):
    num_indices = []
    for j, ch in enumerate(line):
        if ch in string.punctuation and ch != '.':
            symbols.append((i, j))
        elif ch.isdigit():
            num_indices.append(j)
    
    if num_indices:
        current_group = [num_indices[0]]

        for k in range(1, len(num_indices)):
            if num_indices[k] - num_indices[k-1] == 1:
                current_group.append(num_indices[k])
            else:
                numbers.append((i, current_group))
                current_group = [num_indices[k]]

        if current_group:
            numbers.append((i, current_group))
        
for i, number in enumerate(numbers):
    index, group = number
    numbers[i] = list(zip([index]*len(group), group))  

for sym in symbols:
    for dir in dirs:
        a, b = dir[0]+sym[0], dir[1]+sym[1]
        for j, num in enumerate(numbers):
            if (a, b) in num:
                n = [lines[k[0]][k[1]] for k in num]
                n = int("".join(n))
                res += n
                numbers.pop(j)
                    
print(res)