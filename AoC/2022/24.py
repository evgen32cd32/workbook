from collections import deque
from datetime import datetime

blizzsD = {}
blizzs = []
mx = 0
my = 0

class Blizzard:
    def __init__(self, coord, ch):
        self.coord = coord
        self.dir = None
        if ch == 'v':
            self.dir = (0,1)
        if ch == '^':
            self.dir = (0,-1)
        if ch == '<':
            self.dir = (-1,0)
        if ch == '>':
            self.dir = (1,0)
    
    def move(self):
        nc = (self.coord[0] + self.dir[0], self.coord[1] + self.dir[1])
        if nc[0] <= 0:
            nc = (mx-1, nc[1])
        if nc[0] >= mx:
            nc = (1, nc[1])
        if nc[1] <= 0:
            nc = (nc[0], my-1)
        if nc[1] >= my:
            nc = (nc[0], 1)
        if blizzsD[self.coord] is self:
            del blizzsD[self.coord]
        else:
            blizzsD[self.coord].remove(self)
            if len(blizzsD[self.coord]) == 1:
                blizzsD[self.coord] = blizzsD[self.coord].pop()
        self.coord = nc
        if self.coord in blizzsD:
            if isinstance(blizzsD[self.coord],set):
                blizzsD[self.coord].add(self)
            else:
                s = set()
                s.add(self)
                s.add(blizzsD[self.coord])
                blizzsD[self.coord] = s
        else:
            blizzsD[self.coord] = self

with open('/Users/evgeny/python/workbook/data/advent2022/advent_24.txt','r') as f:
    for i, line in enumerate(f.readlines()):
        if line[2] == '#':
            continue
        for j in range(1,len(line)-2):
            if line[j] != '.':
                blizzsD[(j,i)] = Blizzard((j,i), line[j])
                blizzs.append(blizzsD[(j,i)])
    my = i
    mx = len(line) - 2

d = deque()
d.append((1,0,0))
step = 0
visited = set()

while True:
    party = d.popleft()
    if step == party[2]:
        step += 1
        #current_time = datetime.now().strftime("%H:%M:%S")
        #print('{} {}'.format(current_time,step))
        for b in blizzs:
            b.move()
    if party in visited:
        continue
    visited.add(party)
    if party[1] + 1 < my and (party[0],party[1]+1) not in blizzsD:
        if party[0] + 1 == mx and party[1] + 2 == my:
            print(step+1)
            break
        d.append((party[0],party[1] + 1,step))
    if party[0] + 1 < mx and party[1] > 0 and (party[0]+1,party[1]) not in blizzsD:
        if party[0] + 2 == mx and party[1] + 1 == my:
            print(step+1)
            break
        d.append((party[0]+1,party[1],step))
    if (party[0],party[1]) not in blizzsD:
        d.append((party[0],party[1],step))
    if party[1] > 1 and (party[0],party[1]-1) not in blizzsD:
        d.append((party[0],party[1] - 1,step))
    if party[0] > 1 and (party[0]-1,party[1]) not in blizzsD:
        d.append((party[0] - 1,party[1],step))

for b in blizzs:
    b.move()

d = deque()
step += 1
d.append((mx-1,my,step))
visited = set()

while True:
    party = d.popleft()
    if step == party[2]:
        step += 1
        #current_time = datetime.now().strftime("%H:%M:%S")
        #print('{} {}'.format(current_time,step))
        for b in blizzs:
            b.move()
    if party in visited:
        continue
    visited.add(party)
    if party[1] > 1 and (party[0],party[1]-1) not in blizzsD:
        if party[0]  == 1 and party[1] == 2:
            break
        d.append((party[0],party[1] - 1,step))
    if party[0] > 1 and party[1] < my and (party[0]-1,party[1]) not in blizzsD:
        if party[0]  == 2 and party[1] == 1:
            break
        d.append((party[0] - 1,party[1],step))
    if (party[0],party[1]) not in blizzsD:
        d.append((party[0],party[1],step))
    if party[1] + 1 < my and (party[0],party[1]+1) not in blizzsD:
        d.append((party[0],party[1] + 1,step))
    if party[0] + 1 < mx and (party[0]+1,party[1]) not in blizzsD:
        d.append((party[0]+1,party[1],step))

for b in blizzs:
    b.move()

d = deque()
step += 1
d.append((1,0,step))
visited = set()

while True:
    party = d.popleft()
    if step == party[2]:
        step += 1
        #current_time = datetime.now().strftime("%H:%M:%S")
        #print('{} {}'.format(current_time,step))
        for b in blizzs:
            b.move()
    if party in visited:
        continue
    visited.add(party)
    if party[1] + 1 < my and (party[0],party[1]+1) not in blizzsD:
        if party[0] + 1 == mx and party[1] + 2 == my:
            print(step+1)
            break
        d.append((party[0],party[1] + 1,step))
    if party[0] + 1 < mx and party[1] > 0 and (party[0]+1,party[1]) not in blizzsD:
        if party[0] + 2 == mx and party[1] + 1 == my:
            print(step+1)
            break
        d.append((party[0]+1,party[1],step))
    if (party[0],party[1]) not in blizzsD:
        d.append((party[0],party[1],step))
    if party[1] > 1 and (party[0],party[1]-1) not in blizzsD:
        d.append((party[0],party[1] - 1,step))
    if party[0] > 1 and (party[0]-1,party[1]) not in blizzsD:
        d.append((party[0] - 1,party[1],step))