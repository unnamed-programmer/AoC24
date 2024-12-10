import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    topoMap = [line.strip() for line in lines]

headVal = 0
tailVal = 9

checkVecs = [
    (-1,  0),
    ( 0, -1),
    ( 0,  1),
    ( 1,  0),
]

def find(plane: list[str], startPos: tuple, target: int) -> list[tuple]:
    ret = []
    for cv in checkVecs:
        pos = vecAdd(startPos, cv)
        if pos[0] in range(0, len(plane)) and pos[1] in range(0, len(plane[0])):
            if plane[pos[0]][pos[1]] == str(target):
                ret.append(pos)
        else:
            continue
    return ret

def vecAdd(v1: tuple ,v2: tuple) -> tuple:
    return (v1[0] + v2[0], v1[1] + v2[1])

heads = [(v, h) for v in range(len(lines)) for h in range(len(lines[v])) if lines[v][h] == '0']
# list of dicts
links = [{} for _ in range(10)]
links[0] = {head: None for head in heads}

# generate links
for i in range(10):
    for link in links[i]:
        links[i][link] = find(topoMap, link, i + 1)
        for nxL in links[i][link]:
            links[i + 1][nxL] = None
    pass

total = 0

for l0 in heads:
    for l1 in links[0][l0]:
        for l2 in links[1][l1]:
            for l3 in links[2][l2]:
                for l4 in links[3][l3]:
                    for l5 in links[4][l4]:
                        for l6 in links[5][l5]:
                            for l7 in links[6][l6]:
                                for l8 in links[7][l7]:
                                    for l9 in links[8][l8]:
                                        total += 1
                                        print(total)

print(total)
pass