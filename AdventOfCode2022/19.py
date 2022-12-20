from math import ceil
from datetime import datetime

blueprints = {}
with open('/Users/evgeny/python/workbook/data/advent2022/advent_19.txt','r') as f:
    for line in f.readlines():
        bp = {}
        splitted = line.split()
        bp['ore'] = (int(splitted[6]),0,0)
        bp['clay'] = (int(splitted[12]),0,0)
        bp['obs'] = (int(splitted[18]),int(splitted[21]),0)
        bp['geo'] = (int(splitted[27]),0,int(splitted[30]))
        blueprints[int(splitted[1][:-1])] = bp

#for k in blueprints:
#    print('{}:{}'.format(k,blueprints[k]))

#robotType = ['ore','clay','obs','geo']

def recursiveMaxGeode(bp, robots, minutes, res = [0, 0, 0]):
    mg = 0
    rtb = []
    if robots[2] > 0:
        rtb.append('geo')
    if robots[0] < bp['geo'][0] or robots[2] < bp['geo'][2]:
        if robots[1] > 0:
            rtb.append('obs')
        if robots[1] < bp['obs'][1]:
            rtb.append('clay')
        if robots[0] < max([x[0] for k, x in bp.items() if k != 'ore']):
            rtb.append('ore')
    for rt in rtb:
        mm = 0
        for i in range(3):
            if bp[rt][i] != 0:
                m = int(ceil((bp[rt][i] - res[i])/robots[i]))
                if m > mm:
                    mm = m
        mm += 1
        rs = res.copy()
        for i in range(3):
            rs[i] = rs[i] + mm * robots[i] - bp[rt][i]
        g = 0
        if rt == 'geo':
            g = minutes - mm
            if g < 0:
                g = 0
            rl = robots
        else:
            rl = robots.copy()
            if rt == 'ore':
                rl[0] += 1
            elif rt == 'clay':
                rl[1] += 1
            else:
                rl[2] += 1
        if minutes > mm + 1:
            g = g + recursiveMaxGeode(bp, rl, minutes - mm, rs)
        if g > mg:
            mg = g
    return mg

current_time = datetime.now().strftime("%H:%M:%S")
print(current_time)

#firstAns = 0
#for k in blueprints:
#    a = recursiveMaxGeode(blueprints[k], [1, 0, 0], 24)
#    current_time = datetime.now().strftime("%H:%M:%S")
#    print('{} {} {}'.format(current_time, k, a))
#    firstAns = firstAns + k * a
## first answer
#print(firstAns)

secondAns = 1
for i in range(1,4):
    if i in blueprints:
        a = recursiveMaxGeode(blueprints[i], [1, 0, 0], 32)
        current_time = datetime.now().strftime("%H:%M:%S")
        print('{} {} {}'.format(current_time, i, a))
        secondAns = secondAns * a
# second answer
print(secondAns)
