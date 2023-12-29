from itertools import product

with open("input.txt", "r") as file:
    content = file.read()

rows = [item.split(' ') for item in content.split('\n')]
for i, item in enumerate(rows):
    rows[i][1] = item[1].split(',')
    rows[i][0] = item[0].split('.')
    while '' in item[0]:
        rows[i][0].remove('')
    rows[i][0] = ' '.join(rows[i][0])

values = [' ', '#']

res = 0

for row in rows:
    blank = row[0].count('?')
    for combination in product(values, repeat=blank):
        new_row = row[0]
        for value in combination:
            new_row = new_row.replace('?', value, 1)
        new_row = new_row.split(' ')
        arr = [item.count('#') for item in new_row if item.count('#') != 0]
        target = list(map(int, row[1]))
        if arr == target:
            res += 1
    
print(res)