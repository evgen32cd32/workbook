import sys
sys.setrecursionlimit(10000000)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_17.txt','r') as f:
    ar = []
    hm = []
    for line in f.readlines():
        ar.append([int(x) for x in line if x.isdigit()])
        hm.append([])
        for _ in range(len(ar[0])):
            hm[-1].append({})

    queue = set()
    
    def rec(i,j,way,steps):
        def check(h,a,b,w,s):
            if a == len(ar)-1 and b == len(ar)-1:
                h.append(ar[a][b])
            elif (w,s) in hm[a][b]:
                h.append(hm[a][b][(w,s)])
            else:
                if (a,b,w,s) not in queue:
                    
                    h.append(rec(a,b,w,s))
            return h
        heats = []
        if steps < 3:
            if way == 'u' and i > 0:
                heats = check(heats,i-1,j,'u',steps+1)
            if way == 'd' and i < len(ar)-1:
                heats = check(heats,i+1,j,'d',steps+1)
            if way == 'l' and j > 0:
                heats = check(heats,i,j-1,'l',steps+1)
            if way == 'r' and j < len(ar[0])-1:
                heats = check(heats,i,j+1,'r',steps+1)
        if way == 'l' or way == 'r':
            if i > 0:
                heats = check(heats,i-1,j,'u',1)
            if i < len(ar)-1:
                heats = check(heats,i+1,j,'d',1)
        if way == 'u' or way == 'd':
            if j > 0:
                heats = check(heats,i,j-1,'l',1)
            if j < len(ar[0])-1:
                heats = check(heats,i,j+1,'r',1)
        heat = ar[i][j] + min(heats)
        hm[i][j][(way,steps)] = heat
        return heat
    
# first answer
print(rec(0,0,'r',0))