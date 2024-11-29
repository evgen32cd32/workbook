from collections import deque

class Area():
    def __init__(self):
        self.heightMap = []
        self.wayMap = []
        self.start = None
    
    def init2(self):
        self.nx = len(self.heightMap[0]) - 1
        self.ny = len(self.heightMap) - 1
        self.ways = deque()
        self.ways.append(self.start)
    
    def checkIfPossibleWay(self, x, y, curH):
        if x < 0 or x > self.nx or y < 0 or y > self.ny:
            return False
        if self.wayMap[y][x] > 0:
            return False
        if self.heightMap[y][x] - curH > 1:
            return False
        return True
         

with open('/Users/evgeny/python/workbook/data/advent2022/advent_12.txt','r') as f:
    area = Area()
    for line in f.readlines():
        area.heightMap.append([])
        area.wayMap.append([])
        for x in line:
            if x == 'S':
                area.heightMap[-1].append(0)
                area.wayMap[-1].append(1)
                area.start = (len(area.wayMap[-1])-1, len(area.wayMap)-1)
            elif x == 'E':
                area.heightMap[-1].append(26)
                area.wayMap[-1].append(-1)
            elif x.isalpha():
                area.heightMap[-1].append(ord(x) - ord('a'))
                area.wayMap[-1].append(0)


#for i in range(len(area.heightMap)):
#    print('{} {}'.format(area.heightMap[i], area.wayMap[i]))

area.init2()
firstAns = 0

f = open('/Users/evgeny/python/workbook/data/advent2022/advent_12_out.txt','w')

while len(area.ways) > 0:
    x,y = area.ways.popleft()
    ch = area.heightMap[y][x]
    cs = area.wayMap[y][x]
    pws = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
    for pw in pws:
        if area.checkIfPossibleWay(pw[0], pw[1], ch):
            if area.wayMap[pw[1]][pw[0]] == -1:
                firstAns = cs
                area.ways.clear()
                break
            area.wayMap[pw[1]][pw[0]] = cs + 1
            area.ways.append(pw)
    f.write('{} {}\n'.format(x,y))
    for i in area.wayMap:
        f.write('{}\n'.format(''.join([str(j % 10) if j != 0 else '.' for j in i])))

f.close()
# first answer
print(firstAns)