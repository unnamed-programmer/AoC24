import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    topoMap = [line.strip() for line in lines]

headVal = 0
tailVal = 9

checkVecs = [
    # (-1, -1),
    (-1,  0),
    # (-1,  1),
    ( 0, -1),
    ( 0,  1),
    # ( 1, -1),
    ( 1,  0),
    #  1,  1)
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

# parse through links and find how many tails each head reaches
headCount = [0 for _ in range(len(links[0]))]
headLinks = [[[list(links[0].keys())[x]]] + [None for _ in range(9)] for x in range(len(links[0]))]

for trail in headLinks:
    if trail == headLinks[4]:
        pass
    for i in range(0, 9):
        prev = trail[i]
        trail[i + 1] = set()
        for p in prev:
            nx = links[i][p]
            if isinstance(nx, list):
                for nxItem in nx: trail[i + 1].add(nxItem)
            pass
    pass

total = 0
for hl in headLinks:
    total += len(hl[9])

print(total)
pass