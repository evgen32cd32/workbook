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

for k in blueprints:
    print('{}:{}'.format(k,blueprints[k]))

robotType = ['ore','clay','obs','geo']

def recursiveMaxGeode(bp, robots, minutes, res = [0, 0, 0]):
    if minutes <= 1:
        return 0
    mg = 0
    for r, rt in enumerate(robotType):
        fl = False
        mm = 0
        for i in range(3):
            if bp[rt][i] != 0:
                if robots[i] == 0:
                    fl = True
                    break
                m = int(ceil((bp[rt][i] - res[i])/robots[i]))
                if m > mm:
                    mm = m
        if fl:
            continue
        rs = res.copy()
        for i in range(3):
            rs[i] = rs[i] + (mm + 1) * robots[i] - bp[rt][i]
        g = 0
        if rt == 'geo':
            g = minutes - mm - 1
            if g < 0:
                g = 0
            rl = robots
        else:
            rl = robots.copy()
            rl[r] = rl[r] + 1
        g = g + recursiveMaxGeode(bp, rl, minutes - mm - 1, rs)
        if g > mg:
            mg = g
    return mg

current_time = datetime.now().strftime("%H:%M:%S")

#firstAns = 0
#print(current_time)
#for k in blueprints:
#    a = recursiveMaxGeode(blueprints[k], [1, 0, 0], 24)
#    current_time = datetime.now().strftime("%H:%M:%S")
#    print('{} {} {} {}'.format(current_time, k, a))
#    firstAns = firstAns + k * a
## first answer
#print(firstAns)

secondAns = 1
for i in range(1,4):
    a = recursiveMaxGeode(blueprints[i], [1, 0, 0], 32)
    current_time = datetime.now().strftime("%H:%M:%S")
    print('{} {} {}'.format(current_time, i, a))
    secondAns = secondAns * a
# second answer
print(secondAns)
