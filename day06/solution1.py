import os
import re
from enum import Enum

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    board = [[el for el in line.strip()] for line in lines]

class dr(Enum): # direction
    up = 0
    right = 1
    down = 2
    left = 3

def printBoard():
    if len(visited) % 100 == 0:
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
        print(f"{len(visited)}\n\n")
    pass

for line in board:
    if '^' in line:
        gY, gX = board.index(line), line.index('^')

board[gY][gX] = '.'

gD = dr.up
visited = []

guardOnBoard = True
while guardOnBoard:
    #print(f"Guard at ({gX}, {gY}), facing {gD}. Total {visited}.")
    match gD:
        case dr.up:
            if gY - 1 < 0:
                guardOnBoard = False
                break
            match board[gY - 1][gX]:
                case '.':
                    if not (gX, gY) in visited: visited.append((gX, gY))
                    gY -= 1
                case '#':
                    gD = dr((gD.value + 1) % 4)
        case dr.right:
            if gX + 1 >= len(board[gY]):
                guardOnBoard = False
                break
            match board[gY][gX + 1]:
                case '.':
                    if not (gX, gY) in visited: visited.append((gX, gY))
                    gX += 1
                case '#':
                    gD = dr((gD.value + 1) % 4)
        case dr.down:
            if gY + 1 >= len(board):
                guardOnBoard = False
                break
            match board[gY + 1][gX]:
                case '.':
                    if not (gX, gY) in visited: visited.append((gX, gY))
                    gY += 1
                case '#':
                    gD = dr((gD.value + 1) % 4)
        case dr.left:
            if gX - 1 < 0:
                guardOnBoard = False
                break
            match board[gY][gX - 1]:
                case '.':
                    if not (gX, gY) in visited: visited.append((gX, gY))
                    gX -= 1
                case '#':
                    gD = dr((gD.value + 1) % 4)

visited += 1
# god i hate this

printBoard()
print(len(visited))
pass
