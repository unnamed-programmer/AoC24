import os
import re

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

rules = lines[:lines.index('')]
updates = lines[lines.index('') + 1:]
goodUpdates = []

for update in updates:
    ulist = [int(u) for u in update.split(',')]
    ok = True
    for rule in rules:
        rule = [int(n) for n in rule.split('|')]
        if rule[0] in ulist and rule[1] in ulist:
            i1 = ulist.index(rule[0])
            i2 = ulist.index(rule[1])
            if i1 >= i2:
                ok = False
                print(f"{update} is NOT ok: rule {rule}")
                break
    if ok:
        print(f"{update} is OK")
        goodUpdates.append(ulist)

total = 0

for update in goodUpdates:
    total += update[len(update) // 2]

print(total)
pass