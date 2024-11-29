from math import ceil
from functools import reduce
import sys

lava = []
minMaxCoord = [[1000000, 0] for _ in range(3)]

with open('/Users/evgeny/python/workbook/data/advent2022/advent_18.txt','r') as f:
    for line in f.readlines():
        lv = [int(x) for x in line.split(',')]
        lava.append(lv)
        for i in range(3):
            if lv[i] < minMaxCoord[i][0]:
                minMaxCoord[i][0] = lv[i]
            if lv[i] > minMaxCoord[i][1]:
                minMaxCoord[i][1] = lv[i]

#print(minMaxCoord)

area = []
for i in range(minMaxCoord[0][1] - minMaxCoord[0][0] + 3):
    area.append([])
    for j in range(minMaxCoord[1][1] - minMaxCoord[1][0] + 3):
        area[-1].append(['.'] * (minMaxCoord[2][1] - minMaxCoord[2][0] + 3))

sys.setrecursionlimit(reduce(lambda x,y: x*y,[coord[1] - coord[0] + 3 for coord in minMaxCoord]))

for lv in lava:
    for i in range(3):
        lv[i] = lv[i] + 1 - minMaxCoord[i][0]
    area[lv[0]][lv[1]][lv[2]] = 'O'

directions = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

def recursiveBlow(coord):
    for d in directions:
        nc = [coord[0] + d[0], coord[1] + d[1], coord[2] + d[2]]
        fl = False
        for i in range(3):
            if nc[i] < 0 or nc[i] > minMaxCoord[i][1] - minMaxCoord[i][0] + 2:
                fl = True
                break
        if fl:
            continue
        if area[nc[0]][nc[1]][nc[2]] == '.':
            area[nc[0]][nc[1]][nc[2]] = ' '
            recursiveBlow(nc)
        
    
area[0][0][0] = ' '
recursiveBlow([0,0,0])

#for x in area:
#    for y in x:
#        print(''.join(y))
#    print('')

def countAir(coord):
    a = 0
    o = 0
    for d in directions:
        if area[coord[0] + d[0]][coord[1] + d[1]][coord[2] + d[2]] == ' ':
            a = a + 1
            o = o + 1
        if area[coord[0] + d[0]][coord[1] + d[1]][coord[2] + d[2]] == '.':
            a = a + 1
    return (o, a)

firstAns = 0
secondAns = 0

for lv in lava:
    sa, fa = countAir(lv)
    firstAns = firstAns + fa
    secondAns = secondAns + sa

print(firstAns)
print(secondAns)

