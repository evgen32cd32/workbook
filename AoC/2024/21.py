from itertools import permutations
from math import inf

with open('/Users/evgen/projects/workbook/data/advent2024/advent_21.txt','r') as f:
    codes = [x[:-1] if x[-1] == '\n' else x for x in f.readlines()]

numkeys = {'7':0,'8':1j,'9':2j,'4':1,'5':1+1j,'6':1+2j,'1':2,'2':2+1j,'3':2+2j,'0':3+1j,'A':3+2j}
numblank = 3
dirkeys = {'^':1j,'A':2j,'<':1,'v':1+1j,'>':1+2j}
dirblank = 0

def foo(start,end,weights,keys,blank):
    delta = keys[end] - keys[start]
    path = [(1,'v') if round(delta.real) > 0 else (-1,'^')]*round(abs(delta.real)) + [(1j,'>') if round(delta.imag) > 0 else (-1j,'<')]*round(abs(delta.imag))
    spathes = set([x for x in permutations(path)])
    res = inf
    for p in spathes:
        sm = 0
        cur = keys[start]
        for i in range(-1,len(p)):
            if i >= 0:
                cur += p[i][0]
            if cur == blank:
                break
            sm += weights[('A' if i == -1 else p[i][1],'A' if i+1 == len(p) else p[i+1][1])]
        if cur != blank:
            if cur != keys[end]:
                assert()
            res = min(res,sm)
    return res

rc = []
rc.append({(k1,k2):round(abs(v2.real-v1.real)+abs(v2.imag-v1.imag))+1 for k1,v1 in dirkeys.items() for k2,v2 in dirkeys.items()})

for i in range(24):
    r1_r2 = {}
    for k1 in dirkeys:
        for k2 in dirkeys:
            r1_r2[(k1,k2)] = foo(k1,k2,rc[-1],dirkeys,dirblank)
    rc.append(r1_r2)

# first answer
print(sum([int(cd[:-1])*sum([foo('A' if i==0 else cd[i-1],cd[i],rc[1],numkeys,numblank) for i in range(len(cd))]) for cd in codes]))

# second answer
print(sum([int(cd[:-1])*sum([foo('A' if i==0 else cd[i-1],cd[i],rc[-1],numkeys,numblank) for i in range(len(cd))]) for cd in codes]))