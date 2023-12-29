with open('dummy.txt', 'r') as file:
    content = file.read()
steps = content.split(',')

res = 0

for step in steps:
    current = 0
    for char in step:
        current += ord(char)
        current = (current * 17) % 256
    res += current

print(res)