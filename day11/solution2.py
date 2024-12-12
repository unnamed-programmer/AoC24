import os
import time

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    stones = [int(s) for s in [line.strip() for line in f.readlines()][0].split(' ')]

cache = {}

def calc(stone, count):
    global cache

    if (stone, count) in cache.keys():
        return cache[(stone, count)]

    else:
        if count == 0:
            r = 1

        elif stone == 0:
            r = calc(1, count - 1)

        elif len(str(stone)) % 2 == 0:
            r = calc(int(str(stone)[:len(str(stone)) // 2]), count - 1) + calc(int(str(stone)[len(str(stone)) // 2:]), count - 1)

        else:
            r = calc(stone * 2024, count - 1)

        cache[(stone, count)] = r
        return r


total = 0
for stone in stones:
    this = calc(stone, 75)
    total += this

print(total)
print(len(cache))