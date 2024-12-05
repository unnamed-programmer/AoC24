import os

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

rules = lines[:lines.index('')]
updates = lines[lines.index('') + 1:]
badUpdates = []

for update in updates:
    ulist = [int(u) for u in update.split(',')]
    ok = True
    a = False
    while not a:
        a = True
        for rule in rules:
            rule = [int(n) for n in rule.split('|')]
            if rule[0] in ulist and rule[1] in ulist:
                i1 = ulist.index(rule[0])
                i2 = ulist.index(rule[1])
                if i1 >= i2:
                    ok = False
                    a = False
                    print(f"{update} is NOT ok: rule {rule}")
                    t = ulist.pop(i2)
                    ulist.insert(i1, t)

                    # ulist[i1], ulist[i2] = ulist[i2], ulist[i1]
                    pass
    if not ok:
        print(f"{update} is NOT ok")
        badUpdates.append(ulist)

total = 0

for update in badUpdates:
    total += update[len(update) // 2]

print(total)
pass

# that was painful, took a good 20 minutes to realise all i had to do was rerun the rules until it was all sorted (see l19)