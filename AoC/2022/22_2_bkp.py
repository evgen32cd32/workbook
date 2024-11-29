area = []
with open('/Users/evgeny/python/workbook/data/advent2022/advent_22.txt','r') as f:
    area = f.readlines()
    cmds = area[-1][:-1]
    area = [x[:-1] for x in area[:-2]]

mx = max([len(x) for x in area])
for i in range(len(area)):
    area[i] = area[i] + ' '*(mx - len(area[i]))


cubeSize = len(area)//4

# r d l u
# 0 1 2 3
facing = 0
cf = {'L': -1, 'R': 1}
coord = [0, area[0].find('.')]

def move(steps, facing, coord):
    fc = facing
    delta = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    for _ in range(steps):
        nc = [coord[i] + delta[facing][i] for i in range(2)]
        if nc[1] >= len(area[0]): #1
            facing = 2
            nc[1] = cubeSize*2 - 1
            nc[0] = cubeSize*3 - 1 - nc[0]
        elif nc[0] < 0:
            if nc[1] // cubeSize == 1: #2
                facing = 0
                nc[0] = cubeSize*2 + nc[1]
                nc[1] = 0
            else: #3
                facing = 3
                nc[0] = cubeSize*4 - 1
                nc[1] = nc[1] - cubeSize*2
        elif nc[0] >= len(area): #4
            nc[0] = 0
            nc[1] = cubeSize*2 + nc[1]
        elif nc[1] < 0:
            if nc[0] // cubeSize == 2: #5
                facing = 0
                nc[1] = cubeSize
                nc[0] = cubeSize*3 - 1 - nc[0]
            else: #6
                facing = 1
                nc[1] = nc[0] - cubeSize*2
                nc[0] = 0
        elif area[nc[0]][nc[1]] == ' ':
            if facing == 2:
                if nc[0] // cubeSize == 0: #7
                    facing = 0
                    nc[1] = 0
                    nc[0] = cubeSize*3 - 1 - nc[0]
                else: #8
                    facing = 1
                    nc[1] = cubeSize*2 - 1 - nc[0]
                    nc[0] = cubeSize*2
            elif facing == 3: #9
                facing = 0
                nc[0] = cubeSize + nc[1]
                nc[1] = cubeSize
            elif facing == 1:
                facing = 2
                if nc[1] // cubeSize == 2: #10
                    nc[0] = nc[1] - cubeSize
                    nc[1] = cubeSize*2 - 1
                else: #11
                    nc[0] = nc[1] + cubeSize*2
                    nc[1] = cubeSize - 1
            else:
                if nc[0] // cubeSize == 1: #12
                    facing = 3
                    nc[1] = nc[0] + cubeSize
                    nc[0] = cubeSize - 1
                elif nc[0] // cubeSize == 2: #13
                    facing = 2
                    nc[0] = cubeSize*3 - 1 - nc[0]
                    nc[1] = cubeSize*3 - 1
                else: #14
                    facing = 3
                    nc[1] = nc[0] - cubeSize*2
                    nc[0] = cubeSize*3 - 1
        if area[nc[0]][nc[1]] == '#':
            break
        coord = nc
        fc = facing
    return coord, fc

f1 = open('/Users/evgeny/python/workbook/data/advent2022/advent_22_2_score.txt','w')

nr = cmds.find('R')
nl = cmds.find('L')
while True:
    if nr < 0 or nl < nr:
        if nl < 0:
            coord, facing = move(int(cmds), facing, coord)
            f1.write('{} {} {}{}\n'.format(facing,coord,int(cmds),None))
            #print(1000 * (coord[0]+1) + 4*(coord[1]+1) + facing)
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
    f1.write('{} {} {}{}\n'.format(facing,coord,int(st),dir))
    #print(1000 * (coord[0]+1) + 4*(coord[1]+1) + facing)

f1.close()
