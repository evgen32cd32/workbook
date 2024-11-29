with open('/Users/evgeny/python/workbook/data/advent2022/advent_20.txt','r') as f:
    cmds = [int(x) for x in f.readlines()]

ar = cmds.copy()
ari = [i for i in range(len(ar))]

for id, cmd in enumerate(cmds):
    i = ari.index(id)
    ni = i + cmd
    if ni < 0 or ni > len(ar):
        ni = ni % (len(ar) - 1)
    if i == ni:
        continue
    ar.pop(i)
    ari.pop(i)
    ar.insert(ni, cmd)
    ari.insert(ni, id)

i = ar.index(0)
a = [ar[(i+1000) % len(ar)], ar[(i+2000) % len(ar)], ar[(i+3000) % len(ar)]]
firstAns = sum(a)

# first answer
print(firstAns)
        
with open('/Users/evgeny/python/workbook/data/advent2022/advent_20.txt','r') as f:
    cmds = [int(x) * 811589153 for x in f.readlines()]

ar = [x for x in cmds]
ari = [i for i in range(len(ar))]

for _ in range(10):
    for id, cmd in enumerate(cmds):
        i = ari.index(id)
        ni = i + cmd
        if ni < 0 or ni > len(ar):
            ni = ni % (len(ar) - 1)
        if i == ni:
            continue
        v = ar.pop(i)
        ari.pop(i)
        ar.insert(ni, v)
        ari.insert(ni, id)

i = ar.index(0)
a = [ar[(i+1000) % len(ar)], ar[(i+2000) % len(ar)], ar[(i+3000) % len(ar)]]
seconAns = sum(a)

# second answer
print(seconAns)
        