import os
import time
from multiprocessing import Pool

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "testin.txt")

with open(filename, "r") as f:
    stones = [(s, False) for s in [line.strip() for line in f.readlines()][0].split(' ')]

def process(stone: tuple[str, bool], index: int) -> tuple[int, str | tuple[str, str]]:
    if stone[1]: return(index, stone[0])

    if stone[0] == '0':
        r = '1'

    elif len(stone[0]) % 2 == 0:
        sta = stone[0][:len(stone[0]) // 2]
        end = stone[0][len(stone[0]) // 2:]

        while end[0] == '0' and len(end) > 1:
            end = end[1:]

        r = (sta, end)

    else:
        r = str(int(stone[0]) * 2024)

    return (index, r)

for blink in range(25):
    startTime = time.time()

    stones = [(s[0], False) for s in stones]

    pool = Pool()
    args = []

    returns = []

    for ind, stone in enumerate(stones):
        # returns.append(process(stone, ind))
        args.append([stone, ind])

    returns = pool.starmap(process, args)

    for r in returns:
        ind = r[0]
        out = r[1]

        if isinstance(out, str):
            stones[ind] = (out, True)

        else:
            stones.insert(ind + 1, (out[1], True))
            stones[ind] = (out[0], True)

    print(f'Blink {blink + 1} of 75 complete. {len(stones)} stones in {round(time.time() - startTime, 3)} seconds.')

print(len(stones))

pass
