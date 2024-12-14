import os
import re
import colorama
from math import lcm
from AoCutils import Vector2

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "testin.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

total = 0

for i in range(0, len(lines), 4):
    aS = lines[i]
    bS = lines[i + 1]
    pS = lines[i + 2]

    a = Vector2(int(re.search(r'Y\+[0-9]*', aS).group()[2:]), int(re.search(r'X\+[0-9]*', aS).group()[2:]))
    b = Vector2(int(re.search(r'Y\+[0-9]*', bS).group()[2:]), int(re.search(r'X\+[0-9]*', bS).group()[2:]))

    p = Vector2(int(re.search(r'Y=[0-9]*', pS).group()[2:]) + 10000000000000, int(re.search(r'X=[0-9]*', pS).group()[2:]) + 10000000000000)

    maxM = p.y // b.y


    print(f'{colorama.Back.RED}Button {i // 4}{colorama.Back.RESET}')

    m = maxM // 2
    dM = maxM // 2
    found = False
    lowestDiff = float('inf')
    interval = 1000000

    while True:

        m += interval
        remaining = p.y - (m * b.y)
        n = remaining // a.y
        diff = p.x - (a.x * n) + (b.x * m)

        print(f'{i // 4} {interval} search {m} {n} {diff}')


        if abs(diff) < abs(lowestDiff):
            if diff == 0:
                total += m + (n * 3)
                found = True
                break

            lowestDiff = abs(diff)

        else:

            if abs(diff) >= abs(lowestDiff) and interval == 1:
                break

            remaining = p.y - (m * b.y)
            n = remaining // a.y
            diff = p.x - (a.x * n) + (b.x * m)
            interval //= -10
            lowestDiff = abs(diff)

            if abs(diff) < abs(lowestDiff):
                if diff == 0:
                    total += m + (n * 3)
                    found = True
                    break

                lowestDiff = abs(diff)






print(total)