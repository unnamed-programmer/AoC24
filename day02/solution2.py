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

def validate(line: list) -> bool:
    result = []
    for i in range(1, len(line)):
        diff = line[i] - line[i - 1]
        if diff < -3:
            result.append(State.lessinv)
        elif diff < 0:
            result.append(State.lessval)
        elif diff == 0:
            result.append(State.zrodiff)
        elif diff <= 3:
            result.append(State.grtrval)
        else:
            result.append(State.grtrinv)

    if State.grtrinv in result or State.lessinv in result:
        return False
    if State.lessval in result and State.grtrval in result:
        return False
    if State.zrodiff in result:
        return False

    return True

validLines = 0

for line in t:
    if validate(line):
        validLines += 1
    else:
        for i in range(len(line)):
            newLine = [line[j] if j != i else None for j in range(len(line))]
            del newLine[newLine.index(None)]
            if validate(newLine):
                validLines += 1
                break



print(validLines)