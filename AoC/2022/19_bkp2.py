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
    lib[''] = {'robots':(1,0,0),'res':(1,0,0),'min':minutes}

    def recGetLib(s):
        if s in lib:
            return lib[s]
        prev = recGetLib(s[:-1])
        if prev is None:
            lib[s] = None
            return None
        mins = 0
        for i in range(3):
            if bp[s[-1]][i] == 0:
                continue
            m = int(ceil((bp[s[-1]][i] - prev['res'][i])/prev['robots'][i]))
            if m > mins:
                mins = m
        if mins >= prev['min'] - 1:
            lib[s] = None
            return None
        robots = tuple(x + 1 if i == robotId[s[-1]] else x for i, x in enumerate(prev['robots']))
        res = tuple(x + prev['robots'][i] * (mins + 1) - bp[s[-1]][i] for i, x in enumerate(prev['res']))
        lib[s] = {'robots':robots,'res':res,'min':prev['min']-mins-1}
        #print('{} {}'.format(lib[s],s))
        return lib[s]
    
    def valid(s):
        c = s.find('c')
        b = s.find('b')
        g = s.find('g')
        return c >= 0 and c < b and b < g
    
    #print(recGetLib('cccbcbgg'))
    #print(recGetLib('cccbcbgcg'))
    #print(recGetLib('ooccccccbbbbobg'))
    #print(recGetLib('ooccccccbbbbobgbg'))
    #print(recGetLib('ooccccccbbbbobgbgog'))
    
    print(recGetLib('cbg'))
    #cccbcbgg
    k = 1
    sol = {}
    maxg = -1
    while True:
        k = k + 1
        fl = False
        for t in product(robotType, repeat=k):
            s = ''.join(t) + 'g'
            if not valid(s):
                continue
            res = recGetLib(s)
            if res is None:
                continue
            tg = res['min'] - 1
            i = s[:-1].rfind('g')
            if i > -1:
                tg = tg + sol[s[:i+1]]
            sol[s] = tg
            if maxg < tg:
                fl = True
                maxg = tg
        if fl or len(sol) == 0:
            continue
        break
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
