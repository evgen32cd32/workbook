from copy import deepcopy

with open('/Users/evgen/projects/workbook/data/advent2024/advent_06.txt','r') as f:
    lines = f.readlines()
    ar = {i+1j*j:[c=='^',False,False,False] for i,line in enumerate(lines) for j,c in enumerate(line) if c in '.^'}
    ans2 = 0
    maxi = len(lines)
    maxj = len(lines[-1])
    cur = [x for x in ar if ar[x][0]][0]
    curdir = 0
    dirs = [-1,1j,1,-1j]
    loops = set()
    while(True):
        new = cur + dirs[curdir]
        if new.real < 0 or new.imag < 0 or new.real == maxi or new.imag == maxj:
            break
        if new in ar:
            if not any(ar[new]):
                cl = cur
                cdl = curdir
                arl = deepcopy(ar)
                del arl[new]
                while(True):
                    nl = cl + dirs[cdl]
                    if nl.real < 0 or nl.imag < 0 or nl.real == maxi or nl.imag == maxj:
                        break
                    if nl in arl:
                        cl = nl
                    else:
                        cdl = (cdl+1)%4
                    if arl[cl][cdl]:
                        loops.add(new)
                        break
                    arl[cl][cdl] = True
            cur = new
        else:
            curdir = (curdir + 1) % 4
        if ar[cur][curdir]:
            break
        ar[cur][curdir] = True

# first answer
print(sum([any(x) for x in ar.values()]))

# second answer
print(len(loops))