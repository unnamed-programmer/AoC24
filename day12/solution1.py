import os
from multiprocessing import Pool
from AoCutils import Vector2, drVec

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    garden = [line.strip() for line in lines]

types = set()
for i in garden:
    for j in i:
        types.add(j)
types = sorted(list(types))

totalPrice = 0

def findContiguousArea(table: list[list[str]], element: str, start: Vector2) -> list[Vector2]:
    matches = [start]

    anyMatch = True
    while anyMatch:
        anyMatch = False
        for match in matches.copy():
            for dr in drVec:
                nx = match + dr
                if nx.y < 0 or nx.y >= len(table) or nx.x < 0 or nx.x >= len(table[nx.y]):
                    continue
                if table[nx.y][nx.x] == element:
                    if nx not in matches:
                        anyMatch = True
                        matches.append(nx)

    return sorted(matches, key = lambda k: (k.y * len(table)) + k.x)

plantsByType = {}
for plant in types:
    plantsByType[plant] = []
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            if garden[y][x] == plant:
                plantsByType[plant].append(Vector2(y, x))

contiguousRegions = {plant: set() for plant in types}
for plant in types:
    print(f'Plant {plant}')

    p = Pool()
    args = []

    args = [[garden, plant, instance] for instance in plantsByType[plant]]
    print('Args appended.')
        # if instance not in contiguousRegions[plant]:
        #     contiguousRegions[plant].add(tuple(findContiguousArea(garden, plant, instance)))

    returns = p.starmap(findContiguousArea, args)

    for ind, ret in enumerate(returns):
        contiguousRegions[plant].add(tuple(ret))
        print(f'Return {ind} of {len(returns)}...')

print('Found regions.')
pass

for plant in types:
    print(f'Plant {plant}')
    filteredGarden = [[plant if i == plant else '.' for i in j] for j in garden]

    for index, region in enumerate(contiguousRegions[plant]):
        print(f'Region {region} of {len(contiguousRegions[plant])}.')
        plantInstances = list(region)

        area = len(plantInstances)

        perimeter = 0
        for instance in plantInstances:
            for dr in drVec:
                nx = instance + dr
                if 0 <= nx.y < len(filteredGarden) and 0 <= nx.x < len(filteredGarden[nx.y]):
                    if filteredGarden[nx.y][nx.x] == '.':
                        perimeter += 1
                else:
                    perimeter += 1

        totalPrice += area * perimeter

    pass

print(totalPrice)