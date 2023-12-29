file = open("input.txt", "r")

res = 0

for line in file:
    line = line.strip().split(':')
    line[1] = line[1].split('|')
    line[1][0] = [i for i in line[1][0].split(' ') if i!='']
    line[1][1] = [i for i in line[1][1].split(' ') if i!='']
    print(line)
    tmp = 0
    for num in line[1][1]:
        if num in line[1][0]:
            tmp +=1
    print(tmp)
    if tmp > 0:
        res += 2**(tmp-1)

print(res)