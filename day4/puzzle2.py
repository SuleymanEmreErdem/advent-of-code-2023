with open("input.txt", "r") as filess:
    liness = filess.readlines()

num_lines = len(liness)

file = open("input.txt", "r")

cards = [1] * num_lines * 3

for line in file:
    line = line.strip().split(':')
    line[0] = line[0].split(' ')
    line[1] = line[1].split('|')
    line[1][0] = [i for i in line[1][0].split(' ') if i!='']
    line[1][1] = [i for i in line[1][1].split(' ') if i!='']
    line[0] = [i for i in line[0] if i!='']
    card_num = int(line[0][1])
    tmp = 0
    for num in line[1][1]:
        if num in line[1][0]:
            tmp +=1
    for _ in range(int(cards[card_num])):
        for i in range(tmp):
            cards[card_num + i + 1] += 1

print(sum(cards[1:(num_lines+1)]))