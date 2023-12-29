sum = 0

with open('input1.txt', 'r') as inp:
    for line in inp:
        line = line.strip()
        line = line.replace('one', 'o1e').replace('two', 't2o').replace('three', 'th3ee').replace('four', 'f4ur').replace('five', 'f5ve').replace('six', 's6x').replace('seven', 'se7en').replace('eight', 'ei8ht').replace('nine', 'n9ne')
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