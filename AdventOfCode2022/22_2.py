area = []
with open('/Users/evgeny/python/workbook/data/advent2022/advent_22.txt','r') as f:
    area = f.readlines()
    cmds = area[-1][:-1]
    area = [x[:-1] for x in area[:-2]]

mx = max([len(x) for x in area])
for i in range(len(area)):
    area[i] = area[i] + ' '*(mx - len(area[i]))

cubeSize = max(len(area),len(area[0]))//4

y = 'y'
x = 'x'
f = 'f'

class CubeFace:
    def __init__(self, coord, dir, ar):
        self.ar = ar
        self.coord = coord
        self.dir = dir
        self.n = {'t':None,'b':None,'l':None,'r':None}
        self.cd = {'t':0,'b':0,'l':0,'r':0}

faces = [[] for _ in range(6)]

# +-+-+-+
# |4|0|5|
# +-+-+-+
#   |1|
#   +-+
#   |2|
#   +-+
#   |3|
#   +-+

# test: 0
# real: 0
start = {y:0, x:area[0].find('.')//cubeSize}
faces[0] = CubeFace(start,0,[row[start[x]*cubeSize:(start[x]+1)*cubeSize] for row in area[0:cubeSize]])

# test: 0 1 2
# real: 0 1 2
for i in range(1,3):
    coord = {y:i, x:start[x]}
    faces[i] = CubeFace(coord,0,[row[coord[x]*cubeSize:(coord[x]+1)*cubeSize] for row in area[coord[y]*cubeSize:(coord[y]+1)*cubeSize]])

# test: 0 1 2
# real: 0 1 2 5
if area[0][(start[x]+1)*cubeSize] != ' ':
    coord = {y:0, x:start[x]+1}
    faces[5] = CubeFace(coord,0,[row[coord[x]*cubeSize:(coord[x]+1)*cubeSize] for row in area[coord[y]*cubeSize:(coord[y]+1)*cubeSize]])

# test: 0 1 2 5
# real: 0 1 2 5
if area[2*cubeSize][(start[x]+1)*cubeSize] != ' ':
    coord = {y:2, x:start[x]+1}
    faces[5] = CubeFace(coord,2,[row[(coord[x]+1)*cubeSize-1:coord[x]*cubeSize-1:-1] for row in area[(coord[y]+1)*cubeSize-1:coord[y]*cubeSize-1:-1]])

# test: 0 1 2 5
# real: 0 1 2 5 4
if area[2*cubeSize][(start[x]-1)*cubeSize] != ' ':
    coord = {y:2, x:start[x]-1}
    faces[4] = CubeFace(coord,2,[row[(coord[x]+1)*cubeSize-1::-1] for row in area[(coord[y]+1)*cubeSize-1:coord[y]*cubeSize-1:-1]])

# test: 0 1 2 5 3
# real: 0 1 2 5 4
if start[x] == 2:
    coord = {y:1, x:start[x]-2}
    faces[3] = CubeFace(coord,2,[row[(coord[x]+1)*cubeSize-1::-1] for row in area[(coord[y]+1)*cubeSize-1:coord[y]*cubeSize-1:-1]])

# test: 0 1 2 5 3 4
# real: 0 1 2 5 4
if area[cubeSize][(start[x]-1)*cubeSize] != ' ':
    coord = {y:1, x:start[x]-1}
    ar = []
    for i in range(cubeSize):
        ar.append('')
        for j in range(cubeSize):
            ar[-1] = ar[-1] + area[(coord[y]+1)*cubeSize-1-j][coord[x]*cubeSize+i]
    faces[4] = CubeFace(coord,3,ar)

# test: 0 1 2 5 3 4
# real: 0 1 2 5 4 3
if len(area) > 3*cubeSize:
    coord = {y:start[y]+3, x:start[x]-1}
    ar = []
    for i in range(cubeSize):
        ar.append('')
        for j in range(cubeSize):
            ar[-1] = ar[-1] + area[coord[y]*cubeSize+j][(coord[x]+1)*cubeSize-1-i]
    faces[3] = CubeFace(coord,1,ar)

for i in range(4):
    faces[i].n['t'] = (i-1)%4
    faces[i].n['b'] = (i+1)%4
    faces[i].n['l'] = 4
    faces[i].n['r'] = 5
    faces[i].cd['l'] = i
    faces[i].cd['r'] = -i

faces[4].n = {'t':3,'b':1,'l':2,'r':0}
faces[4].cd = {'t':1,'b':-1,'l':2,'r':0}
faces[5].n = {'t':3,'b':1,'l':0,'r':2}
faces[5].cd = {'t':-1,'b':1,'l':0,'r':2}

# r d l u
# 0 1 2 3
facing = 0
cf = {'L': -1, 'R': 1}
coord = {f:0, y:0, x:0}

def move(steps, facing, coord):
    delta = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    fc = facing
    for _ in range(steps):
        nc = {f:coord[f], y: coord[y] + delta[facing][0], x: coord[x] + delta[facing][1]}
        if nc[y] < 0:
            nc[f] = faces[coord[f]].n['t']
            cd = faces[coord[f]].cd['t']
            facing = (facing + cd) % 4
            if cd == 0:
                nc[y] = cubeSize - 1
            elif cd == 1: # 4 -> 3
                nc[y] = nc[x]
                nc[x] = 0
            else: # 5 -> 3
                nc[y] = cubeSize - 1 - nc[x]
                nc[x] = cubeSize - 1
        if nc[y] >= cubeSize:
            nc[f] = faces[coord[f]].n['b']
            cd = faces[coord[f]].cd['b']
            facing = (facing + cd) % 4
            if cd == 0:
                nc[y] = 0
            elif cd == 1: # 5 -> 1
                nc[y] = nc[x]
                nc[x] = cubeSize - 1
            else: # 4 -> 1
                nc[y] = cubeSize - 1 - nc[x]
                nc[x] = 0
        if nc[x] < 0:
            nc[f] = faces[coord[f]].n['l']
            cd = faces[coord[f]].cd['l']
            facing = (facing + cd) % 4
            if cd == 0:
                nc[x] = cubeSize - 1
            elif cd == 2:
                nc[x] = 0
                nc[y] = cubeSize - 1 - nc[y]
            elif cd == 1: # 1 -> 4
                nc[x] = cubeSize - 1 - nc[y]
                nc[y] = cubeSize - 1
            else: # 3 -> 4
                nc[x] = nc[y]
                nc[y] = 0
        if nc[x] >= cubeSize:
            nc[f] = faces[coord[f]].n['r']
            cd = faces[coord[f]].cd['r']
            facing = (facing + cd) % 4
            if cd == 0:
                nc[x] = 0
            elif cd == 2 or cd == -2:
                nc[x] = cubeSize - 1
                nc[y] = cubeSize - 1 - nc[y]
            elif cd == -1: # 1 -> 5
                nc[x] = nc[y]
                nc[y] = cubeSize - 1
            else: # 3 -> 5
                nc[x] = cubeSize - 1 - nc[y]
                nc[y] = 0
        if faces[nc[f]].ar[nc[y]][nc[x]] == '#':
            break
        coord = nc
        fc = facing
    return coord, fc

#f1 = open('/Users/evgeny/python/workbook/data/advent2022/advent_22_1_score.txt','w')

def calcTrue(coord, facing, step, dir):
    face = faces[coord[f]]
    facing = (facing + face.dir) % 4
    ansCoord = {y:face.coord[y]*cubeSize, x: face.coord[x]*cubeSize}
    
    if face.dir == 0:
        ansCoord[x] += coord[x]
        ansCoord[y] += coord[y]
    elif face.dir == 2:
        ansCoord[x] += cubeSize - 1 - coord[x]
        ansCoord[y] += cubeSize - 1 - coord[y]
    elif face.dir == 1:
        ansCoord[x] += cubeSize - 1 - coord[y]
        ansCoord[y] += coord[x]
    else:
        ansCoord[x] += coord[y]
        ansCoord[y] += cubeSize - 1 - coord[x]
    
    #f1.write('{} {} {}{}\n'.format(facing,[ansCoord[y],ansCoord[x]],step, dir))
    print(1000 * (ansCoord[y]+1) + 4*(ansCoord[x]+1) + facing)

nr = cmds.find('R')
nl = cmds.find('L')
while True:
    if nr < 0 or nl < nr:
        if nl < 0:
            coord, facing = move(int(cmds), facing, coord)
            calcTrue(coord,facing, int(cmds), None)
            break
        dir = 'L'
        nr -= nl + 1
        nl = cmds.find('L',nl+1) - nl - 1
    else:
        dir = 'R'
        nl -= nr + 1
        nr = cmds.find('R',nr+1) - nr - 1
    st, cmds = cmds.split(dir,1)
    coord, facing = move(int(st), facing, coord)
    facing = (facing + cf[dir]) % 4
    #calcTrue(coord,facing, int(st), dir)

#f1.close()