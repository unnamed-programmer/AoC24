import os
import re

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    pass

line = ''
for l in lines:
    line += l

regex = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', line)

do = True
results = []

for r in regex:
    if r[:3] == 'mul' and do:
        results.append(r)
    if r == 'do()':
        do = True
    if r == 'don\'t()':
        do = False


total = 0
for result in results:
    i = result.split(',')
    n1 = int(i[0].split('(')[1])
    n2 = int(i[1].split(')')[0])

    mul = n1 * n2
    total += mul
    pass

print(total)