with open("input.txt", "r") as file:
    content = file.read()

rows = content.split("\n")

inst = rows[0]
network = rows[2:]

net_dict = {}

for item in network:
    item = item.split('=')
    item[1] = item[1].strip().replace('(', '').replace(')', '').split(',')
    net_dict[item[0].strip()] = item[1][0].strip(), item[1][1].strip()
    print(item)

print(net_dict)

ptr = "AAA"
print(ptr)

res = 0

while ptr != "ZZZ":
    for i in inst:
        if i == 'L':
            ptr = net_dict.get(ptr)[0]
        elif i == 'R':
            ptr = net_dict.get(ptr)[1]
        res += 1
        print(ptr)

print(res)