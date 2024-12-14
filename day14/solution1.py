import os
import re
from AoCutils import Vector2

currentPath = os.path.normpath(os.path.realpath(os.path.split(__file__)[0]))

filename = os.path.join(currentPath, "input.txt")

with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

width = 103
height = 101

robots = []

for line in lines:
    p = re.findall(r'p=[0-9]*,[0-9]*', line)[0]
    v = re.findall(r'v=-?[0-9]*,-?[0-9]*', line)[0]

    p = [int(_) for _ in p[2:].split(',')]
    v = [int(_) for _ in v[2:].split(',')]

    p = Vector2(p[0], p[1])
    v = Vector2(v[0], v[1])

    robots.append([p, v])

    pass

for i in range(100):
    for robot in robots:
        robot[0] += robot[1]

        while robot[0].x < 0:
            robot[0].x += width
            # robot[1].x = -robot[1].x
        while robot[0].x >= width:
            robot[0].x -= width
            # robot[1].x = -robot[1].x

        while robot[0].y < 0:
            robot[0].y += height
            # robot[1].y = -robot[1].y
        while robot[0].y >= height:
            robot[0].y -= height
            # robot[1].y = -robot[1].y

q1 = q2 = q3 = q4 = 0

for robot in robots:
    if robot[0].y < height // 2:
        if robot[0].x < width // 2:
            q1 += 1
        elif robot[0].x > width // 2:
            q2 += 1
    elif robot[0].y > height // 2:
        if robot[0].x < width // 2:
            q3 += 1
        elif robot[0].x > width // 2:
            q4 += 1

total = q1 * q2 * q3 * q4

print(total)