import os
from enum import Enum

class State(Enum):
    grtrval = 0
    lessval = 1
    grtrinv = 2
    lessinv = 3
    zrodiff = 4

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    t = []
    for line in f.readlines():
        t.append(line.strip().split(" "))
    for i in range(len(t)):
        t[i] = [int(l) for l in t[i]]

results = []

for i in range(len(t)):
    results.append([])
    for j in range(1, len(t[i])):
        diff = t[i][j] - t[i][j - 1]
        if diff < -3:
            results[i].append(State.lessinv)
        elif diff < 0:
            results[i].append(State.lessval)
        elif diff == 0:
            results[i].append(State.zrodiff)
        elif diff <= 3:
            results[i].append(State.grtrval)
        else:
            results[i].append(State.grtrinv)

validLines = 0

for line in results:
    if State.grtrinv in line or State.lessinv in line:
        continue
    if State.lessval in line and State.grtrval in line:
        continue
    if State.zrodiff in line:
        continue

    validLines += 1

print(validLines)