def convert(seed, map):
    if int(map[1]) <= int(seed) and int(seed) <= (int(map[1])+int(map[2])-1):
        return (int(seed)-int(map[1])) + int(map[0]), True
    else:
        return int(seed), False
    
with open('input.txt', 'r') as f:
    file = f.read().split('\n\n')

seeds = file[0].split(':')
seeds = seeds[1].strip().split(' ')
print(seeds)

map = [(item.split(':'))[1].strip().split('\n') for item in file[1:]]

for i, j in enumerate(map):
    for k, l in enumerate(j):
        map[i][k] = map[i][k].split(' ')

print(map)


for ma in map:
    for i, seed in enumerate(seeds):
        for m in ma:
            newseed, stat = convert(seed, m)
            if stat == True:
                seeds[i] = newseed
                break

print(seeds)

print(min(seeds))