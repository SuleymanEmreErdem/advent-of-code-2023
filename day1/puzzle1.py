sum = 0

with open('input1.txt', 'r') as inp:
    for line in inp:
        line = line.strip()
        for i in line:
            if i.isdigit():
                a = int(i) * 10
                break
        for i in line[::-1]:
            if i.isdigit():
                b = int(i)
                break
        sum += a + b

print(sum)