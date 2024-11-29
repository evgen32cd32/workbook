class Sensor:
    def __init__(self, x, y, beaconX, beaconY):
        self.pos = (x, y)
        self.pBeacon = (beaconX, beaconY)
        self.radius = self.distanceTo(beaconX, beaconY)
    
    def distanceTo(self, x, y):
        return abs(self.pos[0] - x) + abs(self.pos[1] - y)
    
    def checkIfInside(self, p):
        r = self.distanceTo(p[0],p[1])
        return r <= self.radius
    
    def intersectHorizon(self, y):
        r = self.radius - abs(self.pos[1] - y)
        if r < 0:
            return set()
        return set(range(self.pos[0]-r, self.pos[0]+r+1))
    
    def checkFieldBorders(self, p, maxCoord):
        return p[0] >= 0 and p[0] <= maxCoord and p[1] >= 0 and p[1] <= maxCoord
    
    def getBorder(self, maxCoord):
        border = []
        for i in range(self.radius+1):
            tmp = []
            tmp.append((self.pos[0] + i, self.pos[1] + (self.radius + 1 - i)))
            tmp.append((self.pos[0] - i, self.pos[1] - (self.radius + 1 - i)))
            tmp.append((self.pos[0] + (self.radius + 1 - i), self.pos[1] - i))
            tmp.append((self.pos[0] - (self.radius + 1 - i), self.pos[1] + i))
            for p in tmp:
                if self.checkFieldBorders(p,maxCoord):
                    border.append(p)
        return border

with open('/Users/evgeny/python/workbook/data/advent2022/advent_15.txt','r') as f:
    sensors = []
    beacons = set()
    for line in f.readlines():
        splitted = line.split()
        x = int(splitted[2][2:-1])
        y = int(splitted[3][2:-1])
        bx = int(splitted[8][2:-1])
        by = int(splitted[9][2:])
        sensors.append(Sensor(x,y,bx,by))
        beacons.add((bx,by))

ib = set()
for s in sensors:
    ib = ib.union(s.intersectHorizon(2000000))

ib = ib.difference([b[0] for b in beacons if b[1] == 2000000])

# first answer
print(len(ib))

found  = False
for sen in sensors:
    brdr = sen.getBorder(4000000)
    for br in brdr:
        fl = False
        for s in sensors:
            if s is sen:
                continue
            if s.checkIfInside(br):
                fl = True
                break
        if fl:
            continue
        secondAns = br[0] * 4000000 + br[1]
        found = True
        break
    if found:
        break

# second answer
print(secondAns)