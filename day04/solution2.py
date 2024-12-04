import os
import re

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

rows = lines
rowsrev = [row[::-1] for row in rows]
columns = []
for j in range(len(rows[0])):
    columns.append("")
    for i in range(len(rows)):
        columns[j] += lines[i][j]
columnsrev = [column[::-1] for column in columns]

regexList = [
    "M.S",
    ".A.",
    "M.S"
]

total = 0

for list in rows, rowsrev, columns, columnsrev:
    testSec = []
    for i in range(len(list) - 2):
        for j in range(len(list[i]) - 2):
            testSec = [
                f"{list[i    ][j    ]}{list[i    ][j + 1]}{list[i    ][j + 2]}",
                f"{list[i + 1][j    ]}{list[i + 1][j + 1]}{list[i + 1][j + 2]}",
                f"{list[i + 2][j    ]}{list[i + 2][j + 1]}{list[i + 2][j + 2]}"
            ]
            if  isinstance(re.search(regexList[0], testSec[0]), re.Match) \
            and isinstance(re.search(regexList[1], testSec[1]), re.Match) \
            and isinstance(re.search(regexList[2], testSec[2]), re.Match):
                print(testSec)
                print(f"at {i}, {j}\n")
                total += 1

print(total)


#########
# X-MAS #
#       #
# M . S #
# . A . #
# M . S #
#########

# what the fuck is this
