from math import inf

ar = []
with open('/Users/evgen/projects/workbook/data/advent2023/advent_17.txt','r') as f:
    for line in f.readlines():
        ar.append([int(x) for x in line if x.isdigit()])
    
drs = {'u':['l','r'],
       'd':['r','l'],
       'l':['d','u'],
       'r':['u','d']}

def task(mins,maxs):    
    hm = []
    for _ in range(len(ar)):
        hm.append([])
        for __ in range(len(ar[0])):
            hm[-1].append({})
    
    for way in drs:
        hm[0][0][way] = {maxs-mins:0}

    ar1 = [(0,0,0,'r',maxs-mins),(0,0,0,'d',maxs-mins)]
    ar2 = []

    ans1 = inf

    def check(nh,ni,nj,way,ns):
        if nh >= ans1:
            return []
        
        out = []
        d = hm[ni][nj]

        for w,s in zip([way]+drs[way],[ns-1,maxs-mins,maxs-mins]):
            if s < 0:
                continue
            if w not in d:
                d[w] = {s:nh}
                out.append((w,s))
            else:
                fl = True
                for a in range(maxs-mins,s-1,-1):
                    if a in d[w] and d[w][a] <= nh:
                        fl = False
                        break
                if fl:
                    d[w][s] = nh
                    out.append((w,s))
        return out

        
    while len(ar1) > 0:
        for heat,i,j,way,steps in ar1:
            if i == len(ar)-1 and j == len(ar[0])-1:
                ans1 = min([heat,ans1])
            step = mins if steps == maxs-mins else 1
            ni = i
            nj = j
            nh = heat
            if way == 'u' and i-step >= 0:
                ni = i-step
                for a in range(1,step+1):
                    nh += ar[i-a][j]
            elif way == 'd' and i+step < len(ar):
                ni = i+step
                for a in range(1,step+1):
                    nh += ar[i+a][j]
            elif way == 'l' and j-step >= 0:
                nj = j-step
                for a in range(1,step+1):
                    nh += ar[i][j-a]
            elif way == 'r' and j+step < len(ar[0]):
                nj = j+step
                for a in range(1,step+1):
                    nh += ar[i][j+a]
            else:
                continue

            for w,s in check(nh,ni,nj,way,steps):
                ar2.append((nh,ni,nj,w,s))
        ar1 = ar2
        ar2 = []
    return ans1

# first answer
print(task(1,3))

# second answer
print(task(4,10))