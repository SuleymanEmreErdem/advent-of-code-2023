def rgb(sets):
    sets = ','.join(sets)
    sets = sets.split(',')
    color = {'red': 0, 'green': 0, 'blue': 0}
    for s in sets:
        s = s.split(' ')
        print(s)
        if int(s[1]) > color.get(s[2], 0):
            color[s[2]] = int(s[1])
    return color.get('red', 0) * color.get('green', 0) * color.get('blue', 0)


inp = open('input.txt', 'r')

res = 0

for line in inp:
    line = line.strip().split(':')
    line[1] = line[1].split(';')
    line[0] = line[0].split(' ')
    print(line)
    res += rgb(line[1])
    
print(res)
