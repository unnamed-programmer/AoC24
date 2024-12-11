import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    stones = [(s, False) for s in [line.strip() for line in f.readlines()][0].split(' ')]

for blink in range(25):
    for ind in range(len(stones)):
        stones[ind] = (stones[ind][0], False)

    for ind, stone in enumerate(stones):
        if stone[1]: continue

        if stone[0] == '0':
            stones[ind] = ('1', True)

        elif len(stone[0]) % 2 == 0:
            sta = stone[0][:len(stone[0]) // 2]
            end = stone[0][len(stone[0]) // 2:]

            while end[0] == '0' and len(end) > 1:
                end = end[1:]

            stones.insert(ind + 1, (end, True))
            stones[ind] = (sta, True)

        else:
            stones[ind] = (str(int(stone[0]) * 2024), True)

    pass

print(len(stones))

pass
