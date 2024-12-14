import os
from multiprocessing import Pool
from collections import deque
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
    print(f'\nPlant {plant}')

    p = Pool()
    args = []

    args = [[garden, plant, instance] for instance in plantsByType[plant]]
    print('Args appended.')

    returns = p.starmap(findContiguousArea, args)

    for ind, ret in enumerate(returns):
        contiguousRegions[plant].add(tuple(ret))
        # print(f'Return {ind} of {len(returns)}...')

print('\n\nFound regions.')
pass

for plant in types:
    print(f'\nPlant {plant}')
    filteredGarden = [[plant if i == plant else '.' for i in j] for j in garden]

    for index, region in enumerate(contiguousRegions[plant]):
        print(f'Region {index + 1} of {len(contiguousRegions[plant])}.')
        plantInstances = list(region)

        area = len(plantInstances)

        outerCells = []
        for y in range(len(filteredGarden)):
            for x in range(len(filteredGarden[y])):
                try:
                    if filteredGarden[y][x] == plant and any(filteredGarden[y + dr.y][x + dr.x] == '.' for dr in drVec):
                        outerCells.append(Vector2(y, x))
                except: pass

        outerFilter = [[plant if Vector2(y, x) in outerCells else '.' for x in range(len(garden[0]))] for y in range(len(garden))]

        perimeter = 0
        #for instance in plantInstances:
        #    for dr in drVec:
        #        nx = instance + dr
        #        if 0 <= nx.y < len(filteredGarden) and 0 <= nx.x < len(filteredGarden[nx.y]):
        #            if filteredGarden[nx.y][nx.x] == '.':
        #                perimeter += 1
        #        else:
        #            perimeter += 1

        rL = len(filteredGarden)
        cL = len(filteredGarden[0])
        edges = set()

        # Find the starting point (first occupied cell)
        start_row, start_col = -1, -1
        for row in range(rL):
            for col in range(cL):
                if filteredGarden[row][col] == plant:
                    start_row, start_col = row, col
                    break
            if start_row != -1:
                break

        # Perform BFS to find the edges
        queue = deque([(start_row, start_col)])
        visited = set([(start_row, start_col)])

        while queue:
            row, col = queue.popleft()

            # Check if the current cell is an edge
            found = False
            for dr in drVec:
                try:
                    if filteredGarden[row + dr.y][col + dr.x] == '.':
                        found = True
                        break
                except: pass
            if found:
                edges.add(Vector2(row, col))

            # Explore the neighbors
            for dr in drVec:
                new_row, new_col = row + dr.y, col + dr.x
                if 0 <= new_row < rL and 0 <= new_col < cL and filteredGarden[new_row][new_col] == plant and (new_row, new_col) not in visited:
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))

        for edge in edges:
            for drI in range(len(drVec)):
                if edge + drVec[drI] in edges:
                    if edge + drVec[(drI + 1) % 4] in edges or edge + drVec[(drI + 3) % 4] in edges:
                        perimeter += 1

        totalPrice += area * perimeter

    pass

print(totalPrice)