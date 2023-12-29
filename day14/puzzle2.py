with open('input.txt', 'r') as file:
    content = file.read()
rows = content.split('\n')
rows = [list(item) for item in rows]

res = 0

seen = []
iter = 0
flag = True

while flag:
    for _ in range(4):
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
        if rows in seen:
            ind = seen.index(rows)
            print(iter, ind)
            flag = False
            break
        else:
            iter += 1
            seen.append(rows)
            rows = [list(x) for x in zip(*rows[::-1])]

for _ in range(((4000000000-ind)%(iter-ind))):
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
    rows = [list(x) for x in zip(*rows[::-1])]

for _ in range((iter-ind)%4):
    rows = [list(x) for x in zip(*rows[::-1])]

res += sum(row.count('O') * (len(rows) - i) for i, row in enumerate(rows))

print(res)