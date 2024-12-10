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

def run(board: list[list[str]], gP: Vector2, gD: dr, j, i, count) -> int:
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
                return 1
            else:

                vT.append((gP, gD))
                gP += drVec[gD.value] * onwards.index('#')
                gD = dr((gD.value + 1) % 4)

        else:
            # print(f"Process {count}: ({j}, {i}) returns")
            return 0


def findVisited(board: list[list[str]], gP: Vector2, gD: dr) -> int:
    visited = []

    while True:

        nxP = gP + drVec[gD.value]

        if nxP.y in range(0, len(board)) and nxP.x in range(0, len(board[0])):

            if board[nxP.y][nxP.x] == '.':
                # if not gP in visited: visited.append(gP)
                if not gP in visited: visited.append(gP)
                gP = nxP

            else:
                gD = dr((gD.value + 1) % 4)

        else:
            # with open(os.path.join(currentPath, "wrongVisited.txt"), 'x') as f1:
            #     for v in visited:
            #         f1.write(f"{v.y}, {v.x}\n")
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

    checkCells = findVisited(board, Vector2(sY, sX), sD)
    # checkCells = [(rowI, colI) for rowI in range(len(board)) for colI in range(len(board[rowI]))]

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

    total = 0
    for i in returns:
        total += i

    # total = tQ.get()
    print(total)
    print(f'Time taken: {(time.time() - startTime)}s')
    pass