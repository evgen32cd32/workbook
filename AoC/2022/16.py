from collections import deque
from itertools import repeat
from copy import deepcopy

class Valve:
    def __init__(self, name, rate, neighbors):
        self.name = name
        self.rate = rate
        self.neighbors = neighbors
        self.stepsToNevs = {}
    
    def __str__(self) -> str:
        return '{}: {}; {}'.format(self.name,self.rate,self.neighbors)
        
valveDict = {}
nevs = []
with open('/Users/evgeny/python/workbook/data/advent2022/advent_16.txt','r') as f:
    for line in f.readlines():
        splitted = line.split()
        name = splitted[1]
        rate = int(splitted[4].split('=')[1][:-1])
        nv = Valve(name, rate,[x.replace(',','') for x in splitted[9:]])
        valveDict[name] = nv
        if rate > 0:
            nevs.append(name)

def distanceBetweenTwoValves(valve1, valve2):
    d = deque()
    d.append((valve1, 1))
    visited = set()
    while len(d) > 0:
        valve, s = d.popleft()
        if valve in visited:
            continue
        visited.add(valve)
        v = valveDict[valve]
        if valve2 in v.neighbors:
            return s
        d.extend(zip(v.neighbors,repeat(s+1)))
    return None

for nev in nevs:
    a = distanceBetweenTwoValves('AA', nev)
    valveDict['AA'].stepsToNevs[nev] = a
    for nev2 in nevs:
        if nev != nev2 and nev2 not in valveDict[nev].stepsToNevs:
            a = distanceBetweenTwoValves(nev, nev2)
            valveDict[nev].stepsToNevs[nev2] = a
            valveDict[nev2].stepsToNevs[nev] = a

def printAfteOpen():
    for nev in nevs:
        print('{}:{}'.format(nev,valveDict[nev].stepsToNevs))
    print('')


print('AA:{}'.format(valveDict['AA'].stepsToNevs))
printAfteOpen()

def maxPressure(valvesLeft, workers):
    workers.sort(key=lambda x: x[0])
    while(len(workers) > 0):
        w = workers.pop()
        steps = w[0]
        mp = 0
        mv = None
        mstack = []
        for valve in valvesLeft:
            ns = steps - valveDict[w[1]].stepsToNevs[valve] - 1
            if ns <= 0:
                continue
            vl = valvesLeft.copy()
            vl.remove(valve)
            nv = valveDict[valve]
            nw = workers.copy()
            nw.append((ns,valve))
            a, stack = maxPressure(vl, nw)
            p = nv.rate * ns + a
            if p > mp:
                mp = p
                mv = valve
                mstack = stack
        if mv is not None:
            mstack.append(mv)
            return mp, mstack
    return 0, []
    

pressureDict = {}
for i in range(2):#30//4 + 1):
    workers = [(30 - i * 4, 'AA') for _ in range(i+1)]
    pressureDict[i+1] = maxPressure(set(nevs), workers)
    print('{} {}'.format(i+1, pressureDict[i+1]),flush=True)

#print(maxPressure(set(['BA','CA','DA','EA','OA','PA']),[(10,'KA'),(10,'NA')]))
#print(maxPressure(set(['BA','CA','DA']),[(3,'EA'),(6,'PA')]))