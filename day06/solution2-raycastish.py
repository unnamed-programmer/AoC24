## NOTE TO SELF:
## RAYCAST THE LINES
## PATH = BOARD[gX:][gY] or otherwise appropriate
## MVCOUNT = PATH.INDEX('#')

## IT FUCKING WORKS AYE

import os
from enum import Enum
from multiprocessing import Pool
import time

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

retProcCount = 0

class Vector2():
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y + other.y, self.x + other.x)
        elif isinstance(other, int):
            return Vector2(self.y + other, self.x + other)
        else:
            return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y - other.y, self.x - other.x)
        elif isinstance(other, int):
            return Vector2(self.y - other, self.x - other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        return self.__add__(0 - other)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y * other.y, self.x * other.x)
        elif isinstance(other, int):
            return Vector2(self.y * other, self.x * other)
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.y / other.y, self.x / other.x)
        elif isinstance(other, int):
            return Vector2(self.y / other, self.x / other)
        else:
            return NotImplemented

    def __rdiv__(self, other):
        return self.__div__(other)

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return True if self.x == other.x and self.y == other.y else False
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Vector2):
            return False if self.x == other.x and self.y == other.y else True
        else:
            return True

    def __iter__(self):
        yield self.y
        yield self.x

    def __repr__(self):
        return f"Vector2({self.y}, {self.x})"

    def __print__(self):
        return f"{self.y}, {self.x}"

    def __hash__(self):
        return hash((self.y, self.x))

class dr(Enum): # direction
    up =    0
    right = 1
    down =  2
    left =  3

drVec = [
    Vector2(-1, 0),
    Vector2(0 , 1),
    Vector2(1 , 0),
    Vector2(0 ,-1),
]

def run(board: list[list[str]], gP: Vector2, gD: dr, j, i, count) -> tuple[int, tuple[int, int]]:
    vT = []

    while True:
        match gD:
            case dr.up:
                onwards = [board[tY][gP.x] for tY in range(gP.y - 1, -1, -1)]
            case dr.right:
                onwards = [board[gP.y][tX] for tX in range(gP.x + 1, len(board[gP.y]))]
            case dr.down:
                onwards = [board[tY][gP.x] for tY in range(gP.y + 1, len(board))]
            case dr.left:
                onwards = [board[gP.y][tX] for tX in range(gP.x - 1, -1, -1)]

        if '#' in onwards:
            if (gP, gD) in vT:
                # print(f"Process {count}: ({j}, {i}) INFINITE LOOP")
                # with open(os.path.join(currentPath, "new.txt"), 'w') as f2: f2.writelines([f'{v[0].y}, {v[0].x}' for v in vT])
                return (1, (j, i))

            else:

                vT.append((gP, gD))
                gP += drVec[gD.value] * onwards.index('#')
                gD = dr((gD.value + 1) % 4)

        else:
            # print(f"Process {count}: ({j}, {i}) returns")
            # with open(os.path.join(currentPath, "new.txt"), 'w') as f2: f2.writelines([f'{v[0].y}, {v[0].x}' for v in vT])
            return (0, (j, i))


def findVisited(board: list[list[str]], gP: Vector2, gD: dr) -> list[Vector2]:
    vT = []
    visited = []

    while True:
        match gD:
            case dr.up:
                onwards = [board[tY][gP.x] for tY in range(gP.y - 1, -1, -1)]
            case dr.right:
                onwards = [board[gP.y][tX] for tX in range(gP.x + 1, len(board[gP.y]))]
            case dr.down:
                onwards = [board[tY][gP.x] for tY in range(gP.y + 1, len(board))]
            case dr.left:
                onwards = [board[gP.y][tX] for tX in range(gP.x - 1, -1, -1)]

        if '#' in onwards:
            if (gP, gD) in vT:
                return False
            else:

                vT.append((gP, gD))

                for visit in range(onwards.index('#') + 1):
                    ap = gP + (drVec[gD.value] * visit)
                    if ap not in visited: visited.append(ap)

                gP += (drVec[gD.value] * onwards.index('#'))
                gD = dr((gD.value + 1) % 4)

        else:

            with open(os.path.join(currentPath, "wrongVisited.txt"), 'w') as f1:
                for v in sorted(visited, key = lambda v: (v.y * len(board)) + v.x):
                    f1.write(f"{v.y}, {v.x}\n")

            return visited


if __name__ == '__main__':
    startTime = time.time()

    print('Generating tasks...')

    with open(filename, "r") as f:
        lines = f.readlines()
        board = [[el for el in line.strip()] for line in lines]

    for line in board:
        if '^' in line:
            sY, sX = gY, gX = board.index(line), line.index('^')

    board[sY][sX] = '.'
    sD = gD = dr.up

    # checkCells = findVisited(board, Vector2(sY, sX), sD)
    checkCells = [(rowI, colI) for rowI in range(len(board)) for colI in range(len(board[rowI]))]

    p = Pool()
    args = []

    for x, (j, i) in enumerate(checkCells):
        board = [[el for el in line.strip()] for line in lines]
        board[sY][sX] = '.'
        board[i][j] = '#'

        args.append([board, Vector2(sY, sX), sD, j, i, x])

        # print(f'{x + 1} of {len(checkCells)} tasks started...')

        # run(board, Vector2(sY, sX), sD, j, i, x)

    print(f'Running {len(checkCells)} tasks...')

    returns = p.starmap(run, args)
    # god i hate this

    print(f'Writing log file...')

    retGrid = ['.' * len(board[0]) for _ in range(len(board))]
    total = 0
    for i in returns:
        # print(i)
        total += i[0]
        j = i[1]
        retGrid[j[0]] = f'{ retGrid[j[0]][:j[1]] }{ str(i[0]) }{ retGrid[j[0]][j[1] + 1:] }'

    with open(os.path.join(currentPath, "new-u.txt"), 'w') as f2:
        for line in retGrid:
            f2.write(line)
            f2.write('\n')


    # total = tQ.get()
    print(total)
    print(f'Time taken: {(time.time() - startTime)}s')
    pass