import os
import re

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

rows = lines

columns = []
for j in range(len(rows[0])):
    columns.append("")
    for i in range(len(rows)):
        columns[j] += lines[i][j]

diag1 = []
for x in range((len(lines) * 2) - 1):
    diag1.append("")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i + j == x: diag1[x] += lines[i][j]

diag2 = []
for x in range((len(lines) * 2) - 1):
    diag2.append("")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if i + j == x: diag2[x] += lines[len(lines)-1-i][j]

total = 0

for list in rows, columns, diag1, diag2:
    for r in list:
        a = re.findall("XMAS", r, re.IGNORECASE)
        total += len(a)
        b = re.findall("XMAS", r[::-1], re.IGNORECASE)
        total += len(b)

print(total)