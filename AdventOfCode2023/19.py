with open('/Users/evgeny/python/workbook/data/advent2023/advent_19.txt','r') as f:
    ans = 0
    wfs = {}
    parts = []
    def gr(a,b):
        return a > b
    def ls(a,b):
        return a < b
    fl = True
    for line in f.readlines():
        if line == '\n':
            fl = False
            continue
        if fl:
            name, x = line.split('{')
            rules = x.split('}')[0].split(',')
            wfs[name] = []
            for i,r in enumerate(rules):
                if i == len(rules)-1:
                    wfs[name].append(('x',gr,0,r))
                else:
                    rl, out = r.split(':')
                    wfs[name].append((rl[0],gr if rl[1] == '>' else ls,int(rl[2:]),out))
        else:
            if line[-1] == '\n':
                line = line[:-1]
            parts.append({x[0]:int(x[2:]) for x in line[1:-1].split(',')})
        
for x in parts:
    cur = 'in'
    while cur != 'A' and cur != 'R':
        for i,foo,b,nxt in wfs[cur]:
            if foo(x[i],b):
                cur = nxt
                break
    if cur == 'A':
        ans += sum(x.values())


# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_19.txt','r') as f:
    wfs = {}
    def gr(a,b):
        if a[1] <= b:
            return None, a
        if b < a[0]:
            return a, None
        return (b+1,a[1]), (a[0],b)
    def ls(a,b):
        if a[0] >= b:
            return None, a
        if b > a[1]:
            return a, None
        return (a[0],b-1), (b,a[1])
    for line in f.readlines():
        if line == '\n':
            break
        name, x = line.split('{')
        rules = x.split('}')[0].split(',')
        wfs[name] = []
        for i,r in enumerate(rules):
            if i == len(rules)-1:
                wfs[name].append(('x',gr,0,r))
            else:
                rl, out = r.split(':')
                wfs[name].append((rl[0],gr if rl[1] == '>' else ls,int(rl[2:]),out))
        
parts = {'x':(1,4000),'m':(1,4000),'a':(1,4000),'s':(1,4000)}

def checker(cur, x):
    ans = 0
    for i, foo, b, nxt in wfs[cur]:
        newi, oldi = foo(x[i],b)
        if newi is not None:
            nx = {k:v for k,v in x.items()}
            nx[i] = newi
            if nxt == 'A':
                vs = list(nx.values())
                cnts = [a1-a0+1 for a0,a1 in vs]
                mlp = 1
                for cnt in cnts:
                    mlp *= cnt
                ans += mlp
            elif nxt != 'R':
                ans += checker(nxt,nx)
        if oldi is None:
            break
        x[i] = oldi
    return ans

#second answer
print(checker('in', parts))
