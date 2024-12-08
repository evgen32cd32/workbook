with open('/Users/evgen/projects/workbook/data/advent2024/advent_08.txt','r') as f:
    inp = f.readlines()
    maxi = len(inp)-1
    maxj = len(inp[-1])-1
    d = {}
    for i,l in enumerate(inp):
        for j,c in enumerate(l):
            if c not in '.\n':
                if c not in d:
                    d[c] = set()
                d[c].add(i+1j*j)
    ans1 = set()
    ans2 = set()
    for v in d.values():
        if len(v) > 0:
            ans2.update(v)
        for a1 in v:
            for a2 in v:
                if a1 != a2:
                    delta = a1-a2
                    na = a1 + delta
                    if na.real >= 0 and na.real <= maxi and na.imag >= 0 and na.imag <= maxj:
                        ans1.add(na)
                    while na.real >= 0 and na.real <= maxi and na.imag >= 0 and na.imag <= maxj:
                        ans2.add(na)
                        na += delta

# first answer
print(len(ans1))

# second answer
print(len(ans2))