## NOTE TO SELF:
## RAYCAST THE LINES
## PATH = BOARD[gX:][gY] or otherwise appropriate
## MVCOUNT = PATH.INDEX('#')

import os
from enum import Enum
from multiprocessing import Pool
import time

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

retProcCount = 0

class dr(Enum): # direction
    up =    0
    right = 1
    down =  2
    left =  3

drVec = [
    (-1, 0),
    (0 , 1),
    (1 , 0),
    (0 ,-1),
]

def run(board: list[list[str]], sY: int, sX: int, sD: dr, j: int, i: int, count: int, retVisited: bool = False) -> int:

    # global retProcCount

    gY, gX, gD = sY, sX, sD
    gP = (gY, gX)

    vT = []
    visited = []

    while True:

        nxP = gP[0] + drVec[gD.value][0], gP[1] + drVec[gD.value][1]

        if (gP, gD) in vT:
            print(f"Process {count}: ({j}, {i}) INFINITE LOOP")
            return visited if retVisited else 1

        if nxP[0] in range(0, len(board)) and nxP[1] in range(0, len(board[0])):

            if board[nxP[0]][nxP[1]] == '.':
                # if not gP in visited: visited.append(gP)
                if not (gP, gD) in vT: vT.append((gP, gD))
                gP = nxP

            else:
                gD = dr((gD.value + 1) % 4)

                nxP = gP[0] + drVec[gD.value][0], gP[1] + drVec[gD.value][1]

                if board[nxP[0]][nxP[1]] == '.':
                    if not (gP, gD) in vT: vT.append((gP, gD))
                    gP = nxP

                else:
                    gD = dr((gD.value + 1) % 4)

                    if not (gP, gD) in vT: vT.append((gP, gD))
                    gP = nxP = gP[0] + drVec[gD.value][0], gP[1] + drVec[gD.value][1]

        else:
            print(f"Process {count}: ({j}, {i}) returns")
            visited = list(set([x[0] for x in vT]))
            return visited if retVisited else 0


if __name__ == '__main__':
    startTime = time.time()

    with open(filename, "r") as f:
        lines = f.readlines()
        board = [[el for el in line.strip()] for line in lines]

    for line in board:
        if '^' in line:
            sY, sX = gY, gX = board.index(line), line.index('^')

    board[sY][sX] = '.'
    sD = gD = dr.up

    checkCells = run(board, sY, sX, sD, 0, 0, 0, True)

    p = Pool()
    args = []

    for x, (j, i) in enumerate(checkCells):
        board = [[el for el in line.strip()] for line in lines]
        board[sY][sX] = '.'
        board[i][j] = '#'

        args.append([board, sY, sX, sD, j, i, x])

        print(f'{x} of {len(checkCells)} tasks started...')

    returns = p.starmap(run, args)
    # god i hate this

    total = 0
    for i in returns:
        total += i

    # total = tQ.get()
    print(total)
    print(f'Time taken: {(time.time() - startTime)}s')
    pass