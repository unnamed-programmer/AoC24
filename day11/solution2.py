import os
import time
from functools import cache


currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    stones = [int(s) for s in [line.strip() for line in f.readlines()][0].split(' ')]

@cache
def run(stone, steps):
    if steps == 0:
        return 1

    if stone == 0:
        return run(1, steps - 1)

    st = str(stone)
    ln = len(st)

    if ln % 2 == 0:
        return run(int(st[:ln // 2]), steps - 1) + run(int(st[ln // 2:]), steps  -1)

    return run(stone * 2024, steps - 1)

print(sum(run(stone, 75) for stone in stones))
