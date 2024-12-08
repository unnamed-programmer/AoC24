import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

freqs = set(char for line in lines for char in line if char != '.')

antennas = {freq: [(v, h) for v in range(len(lines)) for h in range(len(lines[v])) if lines[v][h] == freq] for freq in freqs}

distanceVecs = dict()
for freq in freqs:
    ant = antennas[freq]
    distanceVecs[freq] = []
    for i in range(len(ant)):
        for j in range(i + 1, len(ant)):
            dV = ant[j][0] - ant[i][0]
            dH = ant[j][1] - ant[i][1]
            distanceVecs[freq].append({'origin': ant[i], 'destination': ant[j], 'vector': (dV, dH)})
            pass
    pass

antinodes = set()
for freq in distanceVecs:
    for vec in distanceVecs[freq]:
        origin = vec['origin']
        destination = vec['destination']
        vector = vec['vector']

        antinode1 = (origin[0] - vector[0], origin[1] - vector[1])
        antinode2 = (destination[0] + vector[0], destination[1] + vector[1])

        if antinode1[0] >= 0 and antinode1[1] >= 0 and antinode1[0] < len(lines) and antinode1[1] < len(lines[0]):
            antinodes.add(antinode1)

        if antinode2[0] >= 0 and antinode2[1] >= 0 and antinode2[0] < len(lines) and antinode2[1] < len(lines[0]):
            antinodes.add(antinode2)
print(len(antinodes))
pass