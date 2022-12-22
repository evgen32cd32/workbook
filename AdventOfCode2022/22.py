area = []
with open('/Users/evgeny/python/workbook/data/advent2022/advent_22.txt','r') as f:
    area = f.readlines()
    cmds = area[-1][:-1]
    area = [x[:-1] for x in area[:-2]]

mx = max([len(x) for x in area])
for i in range(len(area)):
    area[i] = area[i] + ' '*(mx - len(area[i]))

# r d l u
# 0 1 2 3
facing = 0
cf = {'L': -1, 'R': 1}
coord = [0, area[0].find('.')]

def move(steps, facing, coord):
    delta = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    for _ in range(steps):
        nc = [coord[i] + delta[facing][i] for i in range(2)]
        if nc[0] < 0 or (facing == 3 and area[nc[0]][nc[1]] == ' '):
            for i in range(len(area)-1,-1,-1):
                if area[i][nc[1]] == '.':
                    coord[0] = i
                    break
                if area[i][nc[1]] == '#':
                    break
            continue
        if nc[0] >= len(area) or (facing == 1 and area[nc[0]][nc[1]] == ' '):
            for i in range(len(area)):
                if area[i][nc[1]] == '.':
                    coord[0] = i
                    break
                if area[i][nc[1]] == '#':
                    break
            continue
        if nc[1] < 0 or (facing == 2 and area[nc[0]][nc[1]] == ' '):
            for i in range(len(area[0])-1,-1,-1):
                if area[nc[0]][i] == '.':
                    coord[1] = i
                    break
                if area[nc[0]][i] == '#':
                    break
            continue
        if nc[1] >= len(area[0]) or (facing == 0 and area[nc[0]][nc[1]] == ' '):
            for i in range(len(area[0])):
                if area[nc[0]][i] == '.':
                    coord[1] = i
                    break
                if area[nc[0]][i] == '#':
                    break
            continue
        if area[nc[0]][nc[1]] == '#':
            break
        coord = nc
    return coord

nr = cmds.find('R')
nl = cmds.find('L')
while True:
    if nr < 0 or nl < nr:
        if nl < 0:
            coord = move(int(cmds), facing, coord)
            break
        dir = 'L'
        nr -= nl + 1
        nl = cmds.find('L',nl+1) - nl - 1
    else:
        dir = 'R'
        nl -= nr + 1
        nr = cmds.find('R',nr+1) - nr - 1
    st, cmds = cmds.split(dir,1)
    coord = move(int(st), facing, coord)
    facing = (facing + cf[dir]) % 4

print(1000 * (coord[0]+1) + 4*(coord[1]+1) + facing)
