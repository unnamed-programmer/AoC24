import os
import re
from enum import Enum

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    board = [[el for el in line.strip()] for line in lines]

def printBoard():
    for y in range(len(board)):
        for x in range(len(board[y])):
            print(board[y][x], end='')
        print()
    print('\n\n')

class dr(Enum): # direction
    up = 0
    right = 1
    down = 2
    left = 3

class Guard():
    def __init__(self, x, y, d, on = True):
        self.x = x
        self.y = y
        self.d = d
        self.on = on

    def move(self, direction = None) -> None:
        direction = self.d if direction is None else direction
        match direction:
            case dr.up:
                self.y -= 1
            case dr.right:
                self.x += 1
            case dr.down:
                self.y += 1
            case dr.left:
                self.x -= 1
        if self.y in range(len(board)) and self.x in range(len(board[self.y])):
            board[self.y][self.x] = 'X'
        else:
            self.on = False
        pass

    def turn(self) -> None:
        self.d = dr((self.d.value + 1) % 4)
        pass

    def check(self) -> bool:
        match self.d:
            case dr.up:
                nx = self.x
                ny = self.y - 1
            case dr.right:
                nx = self.x + 1
                ny = self.y
            case dr.down:
                nx = self.x
                ny = self.y + 1
            case dr.left:
                nx = self.x - 1
                ny = self.y
        try:
            match board[ny][nx]:
                case '.':
                    return True
                case '#':
                    return False
                case 'X':
                    return True
        except: return True

for line in board:
    if '^' in line:
        gY, gX = board.index(line), line.index('^')

board[gY][gX] = '.'

G = Guard(gX, gY, dr.up)

a = 1
while G.on:
    if G.check():
        G.move()
    else:
        G.turn()
    # printBoard()
    # print(f"{G.x} {G.y} {G.d}")
    a += 1
    if a % 10000 == 0:
        printBoard()
        pass

total = 0
for y in board:
    for x in y:
        if x == 'X':
            total += 1
print(total)