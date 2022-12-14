from math import copysign

with open('/Users/evgeny/python/workbook/data/advent2022/advent_14_test.txt','r') as f:
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
        for i in range(ymax + 1):
            self.ar.append(['.']*(xmax - xmin + 1))
        self.sandG = 500 - xmin
        self.ar[0][self.sandG] = '+'
        self.abyss = False
    
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
    
    def trySandMove(self, x, y):
        if x < 0 or x >= len(self.ar[0]) or y >= len(self.ar):
            self.abyss = True
            return False
        if self.ar[y][x] == '.':
            return True
        return False
            

    def generateSand(self):
        cnt = 0
        while not self.abyss:
            sand = [self.sandG, 0]
            movable = True
            while movable:
                if self.trySandMove(sand[0], sand[1] + 1):
                    sand[1] = sand[1] + 1
                    continue
                if self.abyss:
                    break
                if self.trySandMove(sand[0] - 1, sand[1] + 1):
                    sand[0] = sand[0] - 1
                    sand[1] = sand[1] + 1
                    continue
                if self.abyss:
                    break
                if self.trySandMove(sand[0] + 1, sand[1] + 1):
                    sand[0] = sand[0] + 1
                    sand[1] = sand[1] + 1
                    continue
                if self.abyss:
                    break
                movable = False
                cnt = cnt + 1
                self.ar[sand[1]][sand[0]] = 'o'
        return cnt

cave = Cave(ymax,xmin,xmax)
cave.fillWithRocks(rocks)



# first answer
print(cave.generateSand())

print(cave)
