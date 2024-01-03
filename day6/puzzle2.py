file = open('input.txt', 'r').read().split('\n')
time, dist = int("".join(file[0].split()[1:])), int("".join(file[1].split()[1:]))
race = (time, dist)

res = 0
for i in range(1, race[0]//2 + 1):
    attempt = i * (race[0] - i)
    if attempt > race[1]:
        if i == race[0]/2 :
            res += 1
        else:
            res += 2

print(res)