from itertools import combinations

def transpose(space):
    return [list(i) for i in zip(*space)]

def expand_rows(space):
    new_space = []
    for row in space:
        flag = 0
        for j in row:
            if j == '#':
                flag += 1
        if flag == 0:
            new_space.append(len(row) * ['.'])
        new_space.append(row)
    return new_space

with open("input.txt", "r") as file:
    content = file.read()

rows = content.split('\n')
rows = [list(i) for i in rows]

rows = transpose(expand_rows(transpose(expand_rows(rows))))

galaxy = 1
indexes = {}

for i, row in enumerate(rows):
    for j, ch in enumerate(row):
        if ch == '#':
            rows[i][j] = str(galaxy)
            indexes[str(galaxy)] = i, j
            galaxy += 1

galaxies = list(range(1, galaxy))

combs = list(combinations(galaxies, 2))

res = 0

for comb in combs:
    res += abs(indexes.get(str(comb[0]))[0] - indexes.get(str(comb[1]))[0]) + abs(indexes.get(str(comb[0]))[1] - indexes.get(str(comb[1]))[1])

print(res)