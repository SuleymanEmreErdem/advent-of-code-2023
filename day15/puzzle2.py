def get_index_3d(array, element):
    for i, sublist in enumerate(array):
        for j, subsublist in enumerate(sublist):
            if element in subsublist:
                return (i, j, subsublist.index(element))
    return (-1, -1, -1)

with open('input.txt', 'r') as file:
    content = file.read()
steps = content.split(',')

res = 0
hashmap = [[] for _ in range(256)]

for step in steps:
    current = 0
    if '=' in step:
        for char in step.split('=')[0]:
            current += ord(char)
            current = (current * 17) % 256
        ind = get_index_3d(hashmap, step.split('=')[0])
        if ind != (-1, -1, -1):
            hashmap[ind[0]][ind[1]][1] = step.split('=')[1]
        else:
            hashmap[current].append(step.split('='))
    elif '-' in step:
        for char in step.split('-')[0]:
            current += ord(char)
            current = (current * 17) % 256
        ind = get_index_3d(hashmap, step.split('-')[0])
        if ind != (-1, -1, -1):
            hashmap[ind[0]].pop(ind[1])

for i, j in enumerate(hashmap):
    for k, l in enumerate(j):
        res += (i+1) * (k+1) * int(l[1])

print(res)