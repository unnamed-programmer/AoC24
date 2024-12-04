import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    t = []
    for line in f.readlines():
        l = line.strip().split(" ")
        for i in l[::-1]:
            if i == '':
                del l[l.index(i)]
        t.append(l)

    # print(t)

    listA = [int(f[0]) for f in t]
    listB = [int(f[1]) for f in t]

    sLa = sorted(listA)
    sLb = sorted(listB)

    diffs = []

    for i in range(len(sLa)):
        diffs.append(sLb[i] - sLa[i] if sLb[i] - sLa[i] >= 0 else sLa[i] - sLb[i])

    print(sum(diffs))