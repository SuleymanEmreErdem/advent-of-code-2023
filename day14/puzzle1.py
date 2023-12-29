with open('input.txt', 'r') as file:
    content = file.read()
rows = content.split('\n')
rows = [list(item) for item in rows]

res = 0

for i, row in enumerate(rows):
    for j, rock in enumerate(row):
        if rock == 'O':
            ptr = i
            while (ptr-1) != -1:
                if rows[ptr-1][j] == '.':
                    rows[ptr-1][j] = 'O'
                    rows[ptr][j] = '.'
                    ptr -= 1
                else:
                    break

res += sum(row.count('O') * (len(rows) - i) for i, row in enumerate(rows))

print(res)