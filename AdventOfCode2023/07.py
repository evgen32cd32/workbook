from collections import Counter

def foo1(inp):
    hand = inp[0]
    strength = {'A':12, 'K':11, 'Q':10, 'J':9, 'T':8, '9':7, '8':6, '7':5, '6':4, '5':3, '4':2, '3':1, '2':0}
    d = Counter(hand)
    hs = 0
    if len(d) == 1:
        hs = 6
    elif len(d) == 2:
        if 1 in d.values():
            hs = 5
        else:
            hs = 4
    elif len(d) == 3:
        if 3 in d.values():
            hs = 3
        else:
            hs = 2
    elif len(d) == 4:
        hs = 1
    for c in hand:
        hs = hs*100 + strength[c]
    return hs

def foo2(inp):
    hand = inp[0]
    strength = {'A':12, 'K':11, 'Q':10, 'T':9, '9':8, '8':7, '7':6, '6':5, '5':4, '4':3, '3':2, '2':1, 'J':0}
    d = Counter(hand)
    hs = 0
    jks = d['J']
    del d['J']
    if len(d) <= 1:
        hs = 6
    elif len(d) == 2:
        if 1 in d.values():
            hs = 5
        else:
            hs = 4
    elif len(d) == 3:
        if 3 in d.values() or jks > 0:
            hs = 3
        else:
            hs = 2
    elif len(d) == 4:
        hs = 1
    for c in hand:
        hs = hs*100 + strength[c]
    return hs

with open('/Users/evgeny/python/workbook/data/advent2023/advent_07.txt','r') as f:
    ar = [(line.split()[0],int(line.split()[1])) for line in f.readlines()]

# first answer
print(sum([x[1]*(i+1) for i, x in enumerate(sorted(ar,key=foo1))]))

# second answer
print(sum([x[1]*(i+1) for i, x in enumerate(sorted(ar,key=foo2))]))