gates = {}
wires = []
wiresd = {}

with open('/Users/evgen/projects/workbook/data/advent2024/advent_24.txt','r') as f:
    inp = f.readlines()
    for i,line in enumerate(inp):
        if line == '\n':
            break
        n,v = line.split(': ')
        gates[n] = (int(v) == 1)
    for j in range(i+1,len(inp)):
        ar = inp[j].split(' ')
        if ar[4][-1] == '\n':
            ar[4] = ar[4][:-1]
        if ar[0] not in gates:
            gates[ar[0]] = None
        if ar[2] not in gates:
            gates[ar[2]] = None
        if ar[4] not in gates:
            gates[ar[4]] = None
        wires.append((ar[0],ar[2],ar[1],ar[4]))
        wiresd[(min(ar[0],ar[2]),max(ar[0],ar[2]),ar[1])] = ar[4]

todo = sorted(wires,reverse=True)
new_todo = []
while len(todo) > 0:
    for g1,g2,op,go in todo:
        if gates[g1] is None or gates[g2] is None:
            new_todo.append((g1,g2,op,go))
            continue
        if op == 'AND':
            gates[go] = gates[g1] & gates[g2]
        if op == 'OR':
            gates[go] = gates[g1] | gates[g2]
        if op == 'XOR':
            gates[go] = gates[g1] ^ gates[g2]
    todo = new_todo
    new_todo = []

ans1 = 0
i = 0
while 'z'+'{:02d}'.format(i) in gates:
    if gates['z'+'{:02d}'.format(i)]:
        ans1 += 2**i
    i += 1

badis = []
ans2 = []
i = -1
xor1 = None
last = False
while 'z'+'{:02d}'.format(i+1) in gates:
    i += 1
    ci = '{:02d}'.format(i)
    xor_1 = xor1
    bad = True
    if ('x'+ci,'y'+ci,'XOR') not in wiresd:
        last = True
    else:
        xor1 = wiresd[('x'+ci,'y'+ci,'XOR')]
    if i == 0:
        if xor1 != 'z'+ci:
            badis.append(i)
        continue
    ci_1 = '{:02d}'.format(i-1)
    and_1 = wiresd[('x'+ci_1,'y'+ci_1,'AND')]
    if i == 1:
        or1 = and_1
        xor2 = wiresd[(min(xor1,and_1),max(xor1,and_1),'XOR')]
        if xor2 != 'z'+ci:
            badis.append(i)
        continue
    for _ in range(1):
        if (min(xor_1,or1),max(xor_1,or1),'AND') not in wiresd:
            continue
        and1 = wiresd[(min(xor_1,or1),max(xor_1,or1),'AND')]
        if (min(and1,and_1),max(and1,and_1),'OR') not in wiresd:
            continue
        or1 = wiresd[(min(and1,and_1),max(and1,and_1),'OR')]
        if not last:
            if (min(xor1,or1),max(xor1,or1),'XOR') not in wiresd:
                g1,g2,op = [k for k,v in wiresd.items() if v == 'z'+ci].pop()
                if xor1 == g1:
                    ans2.append(or1)
                    ans2.append(g2)
                    wiresd[[k for k,v in wiresd.items() if v == g2].pop()] = or1
                elif xor1 == g2:
                    ans2.append(or1)
                    ans2.append(g1)
                    wiresd[[k for k,v in wiresd.items() if v == g1].pop()] = or1
                elif or1 == g1:
                    ans2.append(xor1)
                    ans2.append(g2)
                    wiresd[[k for k,v in wiresd.items() if v == g2].pop()] = xor1
                elif or1 == g2:
                    ans2.append(xor1)
                    ans2.append(g1)
                    wiresd[[k for k,v in wiresd.items() if v == g1].pop()] = xor1
                continue
            xor2 = wiresd[(min(xor1,or1),max(xor1,or1),'XOR')]
        else:
            xor2 = or1
        if xor2 != 'z'+ci:
            ans2.append(xor2)
            ans2.append('z'+ci)
            wiresd[[k for k,v in wiresd.items() if v == 'z'+ci].pop()] = xor2
            continue
        bad = []
    if bad:
        badis.append(i)
    if len(ans2) == 8:
        break

#print(badis)

# first answer
print(ans1)

# second answer
print(','.join(sorted(ans2)))