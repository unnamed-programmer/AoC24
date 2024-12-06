import os
import re
from enum import Enum
import asyncio

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

class dr(Enum): # direction
    up = 0
    right = 1
    down = 2
    left = 3

def printBoard():
    for y in range(len(board)):
        for x in range(len(board[y])):
            if x == gX and y == gY:
                match gD:
                    case dr.up:
                        print('^', end='')
                    case dr.right:
                        print('>', end='')
                    case dr.down:
                        print('v', end='')
                    case dr.left:
                        print('<', end='')
            elif (x, y) in visited:
                print('X', end='')
            else:
                print(board[y][x], end='')
        print()
    # print(f"{len(visited)}\n\n")
    pass



total = 0

async def run(board: list[list[str]], sY: int, sX: int, sD: dr, j: int, i: int) -> int:

    gY, gX, gD = sY, sX, sD
    vT = []
    visited = []
    pass

    guardOnBoard = True
    while guardOnBoard:

        if (gX, gY, gD) in vT:
            print(f"({j}, {i}) INFINITE LOOP")
            # printBoard()
            return 1
            break # fucking woohoo

        #print(f"Guard at ({gX}, {gY}), facing {gD}. Total {visited}.")
        match gD:
            case dr.up:
                if gY - 1 < 0:
                    guardOnBoard = False
                else:
                    match board[gY - 1][gX]:
                        case '.':
                            if not (gX, gY) in visited: visited.append((gX, gY))
                            if not (gX, gY, gD) in vT: vT.append((gX, gY, gD))
                            gY -= 1
                        case '#':
                            gD = dr((gD.value + 1) % 4)
            case dr.right:
                if gX + 1 >= len(board[gY]):
                    guardOnBoard = False
                else:
                    match board[gY][gX + 1]:
                        case '.':
                            if not (gX, gY) in visited: visited.append((gX, gY))
                            if not (gX, gY, gD) in vT: vT.append((gX, gY, gD))
                            gX += 1
                        case '#':
                            gD = dr((gD.value + 1) % 4)
            case dr.down:
                if gY + 1 >= len(board):
                    guardOnBoard = False
                else:
                    match board[gY + 1][gX]:
                        case '.':
                            if not (gX, gY) in visited: visited.append((gX, gY))
                            if not (gX, gY, gD) in vT: vT.append((gX, gY, gD))
                            gY += 1
                        case '#':
                            gD = dr((gD.value + 1) % 4)
            case dr.left:
                if gX - 1 < 0:
                    guardOnBoard = False
                else:
                    match board[gY][gX - 1]:
                        case '.':
                            if not (gX, gY) in visited: visited.append((gX, gY))
                            if not (gX, gY, gD) in vT: vT.append((gX, gY, gD))
                            gX -= 1
                        case '#':
                            gD = dr((gD.value + 1) % 4)


    else:
        pass
        print(f"({j}, {i}) returns")
        return 0
        # printBoard()



async def main():

    with open(filename, "r") as f:
        lines = f.readlines()
        board = [[el for el in line.strip()] for line in lines]

    for line in board:
        if '^' in line:
            gY, gX = board.index(line), line.index('^')
            sY, sX = gY, gX

    board[gY][gX] = '.'

    gD = dr.up
    sD = gD

    tasks = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 5 and j == 7:
                pass
            board = [[el for el in line.strip()] for line in lines]
            board[sY][sX] = '.'
            board[i][j] = '#'

            vT = []
            visited = []
            # printBoard()
            pass

            tasks.append(asyncio.create_task(run(board, sY, sX, sD, j, i)))
            print(f"{len(tasks)} tasks running right now.")
            pass


    # god i hate this

    for i in tasks:
        await i

    print(total)
    pass


asyncio.run(main())