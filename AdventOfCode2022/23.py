elfs = {}

class Elf:
    def __init__(self, coord):
        self.coord = coord
        self.nc = None
    
    def considerMove(self, step):
        self.nc = None
        ar = [0]*9
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j == 0:
                    continue
                if (self.coord[0]+j,self.coord[1]+i) in elfs:
                    ar[(i+1)*3+(j+1)] = 1
        if sum(ar) == 0:
            return self.nc
        for i in range(4):
            test = (i + step) % 4
            if test == 0: #north
                if sum(ar[:3]) == 0:
                    self.nc = (self.coord[0],self.coord[1]-1)
                    return self.nc
            if test == 1: #south
                if sum(ar[6:]) == 0:
                    self.nc = (self.coord[0],self.coord[1]+1)
                    return self.nc
            if test == 2: #west
                if sum(ar[::3]) == 0:
                    self.nc = (self.coord[0]-1,self.coord[1])
                    return self.nc
            if test == 3: #east
                if sum(ar[2::3]) == 0:
                    self.nc = (self.coord[0]+1,self.coord[1])
                    return self.nc
        return self.nc


with open('/Users/evgeny/python/workbook/data/advent2022/advent_23.txt','r') as f:
    for i, line in enumerate(f.readlines()):
        for j, ch in enumerate(line):
            if ch == '#':
                elfs[(j,i)] = Elf((j,i))

def calcEmptys(pr = False):
    ks = elfs.keys()
    minx = min(ks, key=lambda x: x[0])[0]
    maxx = max(ks, key=lambda x: x[0])[0]
    miny = min(ks, key=lambda x: x[1])[1]
    maxy = max(ks, key=lambda x: x[1])[1]
    if pr:
        for j in range(miny,maxy+1):
            s = ''
            for i in range(minx,maxx+1):
                if (i,j) in elfs:
                    s = s + '#'
                else:
                    s = s + '.'
            print(s)
        print('')
    return (maxx-minx+1)*(maxy-miny+1) - len(elfs)

#print(calcEmptys(True))
#print('')
i = 0
while True:
    newCoords = {}
    for _, elf in elfs.items():
        nc = elf.considerMove(i%4)
        if nc is not None:
            if nc in newCoords:
                elf.nc = None
                newCoords[nc].nc = None
                del newCoords[nc]
            else:
                newCoords[nc] = elf
    if len(newCoords) == 0:
        print('Last iter: {}'.format(i+1))
        #print(calcEmptys(True))
        break
    for _, elf in newCoords.items():
        del elfs[elf.coord]
        elf.coord = elf.nc
        elfs[elf.nc] = elf
    i += 1
    if i == 10:
        print(calcEmptys())
    #print('{} {}\n'.format(i, calcEmptys(True)))



