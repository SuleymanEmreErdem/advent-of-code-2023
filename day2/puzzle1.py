def rgb(sets):
    for s in sets:
        s = s.split(',')
        color = {}
        for i in s:
            i = i.split(' ')
            color[i[2]] = i[1]
        if not (int(color.get('red', 0)) <= 12 and int(color.get('green', 0)) <= 13 and int(color.get('blue', 0)) <= 14):
            return False
    return True

inp = open('input.txt', 'r')

res = 0

for line in inp:
    line = line.strip().split(':')
    line[1] = line[1].split(';')
    line[0] = line[0].split(' ')
    print(line)
    print(rgb(line[1]))
    if rgb(line[1]):
        res += int(line[0][1])
    
print(res)
