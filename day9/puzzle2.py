def full_zeros(li):
    count = 0
    for i in li:
        if i == 0:
            count += 1
    if count == len(li):
        return True
    else:
        return False

with open("input.txt", "r") as file:
    content = file.read()

rows = content.split("\n")
rows = [item.split(' ') for item in rows]

res = 0

for hist in rows:
    arr = [hist]
    ptr = 0
    tmp = 0
    while not full_zeros(arr[-1]):
        arr.append([(int(arr[ptr][j]) - int(arr[ptr][j-1])) for j in range(1, len(arr[ptr]))])
        ptr += 1
    for item in arr[::2]:
        tmp += int(item[0])
    for item in arr[1::2]:
        tmp -= int(item[0])
    res += tmp

print(res)