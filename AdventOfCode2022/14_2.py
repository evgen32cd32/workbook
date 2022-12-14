from math import copysign
from collections import deque

with open('/Users/evgeny/python/workbook/data/advent2022/advent_14.txt','r') as f:
    rocks = []
    xmax = 0
    xmin = 10**10
    ymax = 0
    ymin = 0
    for line in f.readlines():
        r = [list(map(lambda x: int(x),x.split(','))) for x in line.split('->')]
        xs = [x[0] for x in r]
        ys = [x[1] for x in r]
        if xmax < max(xs):
            xmax = max(xs)
        if xmin > min(xs):
            xmin = min(xs)
        if ymax < max(ys):
            ymax = max(ys)
        rocks.append(r)

class Cave:
    def __init__(self, ymax, xmin, xmax):
        self.ar = []
        self.xmin = xmin
        for i in range(ymax + 2):
            self.ar.append(['.']*(xmax - xmin + 1))
        self.ar.append(['#']*(xmax - xmin +1))
        self.sandG = 500 - xmin
        #self.ar[0][self.sandG] = '+'
    
    def fillWithRocks(self, rocks):
        for r in rocks:
            self.ar[r[0][1]][r[0][0] - self.xmin] = '#'
            for i in range(1,len(r)):
                if r[i][0] == r[i-1][0]:
                    for j in range(r[i][1],r[i-1][1],int(copysign(1,r[i-1][1] - r[i][1]))):
                        self.ar[j][r[i][0] - self.xmin] = '#'
                if r[i][1] == r[i-1][1]:
                    for j in range(r[i][0],r[i-1][0],int(copysign(1,r[i-1][0] - r[i][0]))):
                        self.ar[r[i][1]][j - self.xmin] = '#'
    
    def __str__(self):
        return '\n'.join([''.join(x) for x in self.ar])

    def addRight(self):
        for x in self.ar:
            x.append('.')
        self.ar[-1][-1] = '#'
    
    def addLeft(self):
        for x in self.ar:
            x.insert(0,'.')
        self.ar[-1][0] = '#'
        self.sandG = self.sandG + 1
    
    def trySandMove(self, x, y):
        left = False
        if x >= len(self.ar[0]):
            self.addRight()
        if x < 0:
            self.addLeft()
            x = x + 1
            left = True
        if self.ar[y][x] == '.':
            return (True, left)
        return (False, left)
            

    def generateSand(self):
        cnt = 0
        while self.ar[0][self.sandG] == '.':
            sand = [self.sandG, 0]
            movable = True
            while movable:
                res, left = self.trySandMove(sand[0], sand[1] + 1)
                sand[0] = sand[0] + 1 if left else sand[0]
                if res:
                    sand[1] = sand[1] + 1
                    continue
                res, left = self.trySandMove(sand[0] - 1, sand[1] + 1)
                sand[0] = sand[0] + 1 if left else sand[0]
                if res:
                    sand[0] = sand[0] - 1
                    sand[1] = sand[1] + 1
                    continue
                res, left =  self.trySandMove(sand[0] + 1, sand[1] + 1)
                sand[0] = sand[0] + 1 if left else sand[0]
                if res:
                    sand[0] = sand[0] + 1
                    sand[1] = sand[1] + 1
                    continue
                movable = False
                cnt = cnt + 1
                self.ar[sand[1]][sand[0]] = 'o'
        return cnt

cave = Cave(ymax,xmin,xmax)
cave.fillWithRocks(rocks)



# second answer
print(cave.generateSand())

print(cave)
