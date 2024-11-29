from itertools import cycle
from math import lcm

class Node:
    def __init__(self, v) -> None:
        self.v = v
        self.left = None
        self.right = None

with open('/Users/evgeny/python/workbook/data/advent2023/advent_08.txt','r') as f:
    lines = f.readlines()
    instr = lines[0][:-1]
    d = {}
    for i in range(2,len(lines)):
        a, _, l, r = lines[i].split()
        if a not in d:
            d[a] = Node(a)
        l = l[1:-1]
        r = r[:-1]
        if l not in d:
            d[l] = Node(l)
        if r not in d:
            d[r] = Node(r)
        d[a].left = d[l]
        d[a].right = d[r]
    cur = d['AAA']
    ans = 0
    for c in cycle(instr):
        ans += 1
        if c == 'L':
            cur = cur.left
        else:
            cur = cur.right
        if cur.v == 'ZZZ':
            break

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_08.txt','r') as f:
    lines = f.readlines()
    instr = lines[0][:-1]
    d = {}
    start = []
    fin = []
    for i in range(2,len(lines)):
        a, _, l, r = lines[i].split()
        if a not in d:
            d[a] = Node(a)
        l = l[1:-1]
        r = r[:-1]
        if l not in d:
            d[l] = Node(l)
        if r not in d:
            d[r] = Node(r)
        d[a].left = d[l]
        d[a].right = d[r]
        if a[-1] == 'A':
            start.append(d[a])
        if a[-1] == 'Z':
            fin.append(d[a])
    
    endcycles = {}
    for node in fin:
        cur = node
        i = 0
        for c in cycle(instr):
            i += 1
            cur = cur.left if c == 'L' else cur.right
            if cur.v[-1] == 'Z':
                endcycles[node] = (cur, i)
                break
    
    startoZ = {}
    for node in start:
        cur = node
        i = 0
        for c in cycle(instr):
            i += 1
            cur = cur.left if c == 'L' else cur.right
            if cur.v[-1] == 'Z':
                startoZ[node] = (cur, i)
                break
    #print({k.v:(v[0].v,v[1]) for k,v in endcycles.items()})
    #print({k.v:(v[0].v,v[1]) for k,v in startoZ.items()})

# second answer
print(lcm(*[x[1] for x in endcycles.values()]))