from collections import deque
from datetime import datetime
from itertools import cycle

with open('/Users/evgeny/python/workbook/data/advent2022/advent_17_test.txt','r') as f:
    cmds = f.readline()[:-1]

figures = []
figures.append([[1]*4])
figures.append([[0,1,0],[1]*3,[0,1,0]])
figures.append([[0,0,1],[0,0,1],[1]*3])
figures.append([[1],[1],[1],[1]])
figures.append([[1,1],[1,1]])

area = deque()
area.append([1]*7)
area.extendleft([[0]*7 for _ in range(4)])

def moveLeft(coord, figure):
    if coord[0] == 0:
        return coord
    for y in range(len(figure)):
        for x in range(len(figure[0])):
            if figure[y][x] == 1:
                if area[coord[1] + y][coord[0] + x - 1] == 1:
                    return coord
                break
    return (coord[0] - 1, coord[1])

def moveRight(coord, figure):
    if coord[0] == len(area[0])-len(figure[0]):
        return coord
    for y in range(len(figure)):
        for x in range(len(figure[0])-1, -1, -1):
            if figure[y][x] == 1:
                if area[coord[1] + y][coord[0] + x + 1] == 1:
                    return coord
                break
    return (coord[0] + 1, coord[1])

def moveDown(coord, figure):
    for x in range(len(figure[0])):
        for y in range(len(figure)-1, -1, -1):
            if figure[y][x] == 1:
                if area[coord[1] + y + 1][coord[0] + x] == 1:
                    return coord
                break
    return (coord[0], coord[1] + 1)

figureCycle = cycle(figures)
cmdCycle = cycle(cmds)
hidden = 0
for i in range(1000000000000):
    if i % 1000000 == 0:
        current_time = datetime.now().strftime("%H:%M:%S")
        print('{} {}'.format(current_time, i // 1000000))
    f = next(figureCycle)
    x = 2
    for _ in range(4):
        if next(cmdCycle) == '<':
            x = 0 if x <= 1 else x - 1
        else:
            x = 7 - len(f[0]) if x >= 6 - len(f[0]) else x + 1
    coord = (x, 4 - len(f))
    while True:
        nc = moveDown(coord, f)
        if nc == coord:
            for y in range(len(f)):
                for x in range(len(f[0])):
                    area[coord[1] + y][coord[0] + x] = area[coord[1] + y][coord[0] + x] + f[y][x]
            if min([area[coord[1]][x] + area[coord[1] + 1][x] for x in range(len(area[0]))]) > 0:
                k = len(area) - coord[1] - 2
                hidden = hidden + k
                for _ in range(k):
                    area.pop()
                area[-1] = [1]*7
            area.extendleft([[0]*7 for _ in range(4 - coord[1])])
            #for r in area:
            #    print(''.join(['.' if x == 0 else '#' for x in r]))
            #print('')
            break
        coord = nc
        if next(cmdCycle) == '>':
            coord = moveRight(coord, f)
        else:
            coord = moveLeft(coord, f)

firstAns = len(area) - 5 + hidden

# first answer
print(firstAns)

