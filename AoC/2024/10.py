from collections import Counter

with open('/Users/evgen/projects/workbook/data/advent2024/advent_10.txt','r') as f:
    ar = {i+1j*j:int(c) for i,l in enumerate(f.readlines()) for j,c in enumerate(l) if c.isdigit()}
    st = [k for k,v in ar.items() if v == 0]
    dirs = [1,-1,1j,-1j]
    ans1 = 0
    ans2 = 0
    for s in st:
        v = set()
        u9 = set()
        tv = Counter({s:1})
        ntv = Counter()
        for h in range(1,10):
            for cur,r in tv.items():
                ntv += Counter({cur+drs:r for drs in dirs if cur+drs in ar and ar[cur+drs] == h})
            tv = ntv
            if len(tv) == 0:
                r = 0
                break
            ntv = Counter()
        ans1 += len(tv)
        ans2 += sum([r for r in tv.values()])
            

# first answer
print(ans1)

# second answer
print(ans2)