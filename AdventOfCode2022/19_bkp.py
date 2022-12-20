from math import ceil
from datetime import datetime
from itertools import product

blueprints = {}
with open('/Users/evgeny/python/workbook/data/advent2022/advent_19_test.txt','r') as f:
    for line in f.readlines():
        bp = {}
        splitted = line.split()
        bp['o'] = (int(splitted[6]),0,0)
        bp['c'] = (int(splitted[12]),0,0)
        bp['b'] = (int(splitted[18]),int(splitted[21]),0)
        bp['g'] = (int(splitted[27]),0,int(splitted[30]))
        blueprints[int(splitted[1][:-1])] = bp

for k in blueprints:
    print('{}:{}'.format(k,blueprints[k]))

robotType = ['o','c','b','g']
robotId = {'o' : 0, 'c' : 1, 'b' : 2, 'g' : 3}

def maxGeode(bp, minutes):
    lib = {}
    lib[''] = {'robots':(1,0,0),'res':(1,0,0),'min':minutes,'dem':(0,None,None)}

    def recGetLib(s):
        if s in lib:
            return lib[s]
        prev = recGetLib(s[:-1])
        if prev is None or prev['min'] < 0:
            lib[s] = None
            return None
        mins = 0
        dem = prev['dem']
        for i in range(3):
            if bp[s[-1]][i] == 0:
                continue
            m = int(ceil((bp[s[-1]][i] - prev['res'][i])/prev['robots'][i]))
            if m > mins:
                mins = m
                if m > prev['dem'][0]:
                    dem = (m, robotType[i], len(s)-1)
        robots = tuple(x + 1 if i == robotId[s[-1]] else x for i, x in enumerate(prev['robots']))
        res = tuple(x + prev['robots'][i] * (mins + 1) - bp[s[-1]][i] for i, x in enumerate(prev['res']))
        lib[s] = {'robots':robots,'res':res,'min':prev['min']-mins-1,'dem':dem}
        #print('{} {}'.format(lib[s],s))
        return lib[s]
    
    def calcG(s):
        g = 0
        for i in (i for i, ch in enumerate(s) if ch == 'g'):
            m = lib[s[:i+1]]['min'] - 1
            if m > 0:
                g += m
        return g
    
    sol = {}
    s = 'cbg'
    while True:
        sol[s] = recGetLib(s)
        if sol[s] is None:
            del sol[s]
            break
        print('{} {}'.format(sol[s],s))
        if sol[s]['min'] >= 1:
            s = s + 'g'
            continue
        i = sol[s]['dem'][2]
        r = sol[s]['dem'][1]
        s = s[:i] + r + s[i:]
    maxg = -1
    for k in sol:
        g = calcG(k)
        if maxg < g:
            maxg = g
            print(k)
    return maxg

current_time = datetime.now().strftime("%H:%M:%S")

firstAns = 0
print(current_time)
for k in blueprints:
    a = maxGeode(blueprints[k], 24)
    current_time = datetime.now().strftime("%H:%M:%S")
    print('{} {} {}'.format(current_time, k, a))
    firstAns = firstAns + k * a
# first answer
print(firstAns)

#secondAns = 1
#for i in range(1,3):
#    a = maxGeode(blueprints[i], 32)
#    current_time = datetime.now().strftime("%H:%M:%S")
#    print('{} {} {}'.format(current_time, i, a))
#    secondAns = secondAns * a
#
## second answer
#print(secondAns)
