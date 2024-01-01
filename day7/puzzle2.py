from collections import defaultdict

def swap_pos(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def set_types(card_count):
    if card_count[0][1] == 5:
        return 6
    elif card_count[0][1] == 4 and card_count[1][1] == 1:
        return 5
    elif card_count[0][1] == 3 and card_count[1][1] == 2:
        return 4
    elif card_count[0][1] == 3 and card_count[1][1] == 1 and card_count[2][1] == 1:
        return 3
    elif card_count[0][1] == 2 and card_count[1][1] == 2 and card_count[2][1] == 1:
        return 2
    elif card_count[0][1] == 2 and card_count[1][1] == 1 and card_count[2][1] == 1 and card_count[3][1] == 1:
        return 1
    elif card_count[0][1] == 1 and card_count[1][1] == 1 and card_count[2][1] == 1 and card_count[3][1] == 1 and card_count[4][1] == 1:
        return 0
    
def compare_hands(hand1, hand2):
    card_str = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}
    for i in range(len(hand1)):
        if card_str.get(hand1[i]) > card_str.get(hand2[i]):
            return True
        elif card_str.get(hand1[i]) < card_str.get(hand2[i]):
            return False


file = [hand.split(' ') for hand in open('input.txt', 'r').read().split('\n')]

types = [[], [], [], [], [], [], []]

for hand in file:
    card_count = defaultdict(int)
    count_j = 0
    for card in hand[0]:
        if card != 'J':
            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1
        else:
            count_j += 1
    card_count = sorted(card_count.items(), key=lambda item: item[1], reverse=True)
    print(card_count)
    if card_count:
        if card_count[0][1] + count_j > 5:
            card_count = [(card_count[0][0], 5)] + card_count[1:]
        else:
            card_count = [(card_count[0][0], card_count[0][1] + count_j)] + card_count[1:]
    else:
        card_count.append(('J', count_j))
    types[set_types(card_count)].append(tuple(hand))


for j, t in enumerate(types):
    for k in range(len(t)):
        for i in range(len(t)-k-1):
            if compare_hands(t[i][0], t[i+1][0]):
                swap_pos(types[j], i, i+1)

res, rank = 0, 1

for typ in types:
    if typ:
        for i in typ:
            res += int(i[1]) * rank
            rank += 1

print(res)