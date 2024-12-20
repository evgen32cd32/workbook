from collections import Counter

with open('/Users/evgen/projects/workbook/data/advent2024/advent_20.txt','r') as f:
    ar = {i+1j*j:c for i,l in enumerate(f.readlines()) for j,c in enumerate(l) if c in '.ES'}
    start = [k for k,v in ar.items() if v == 'S'].pop()
    end = [k for k,v in ar.items() if v == 'E'].pop()

    directions = [1,-1j,-1,1j]

    path = {start:0}
    cur = start
    while cur != end:
        cur = [cur+way for way in directions if cur+way in ar and cur+way not in path].pop()
        path[cur] = len(path)
    
# first answer
print(len([path[k+2*way]-v-2 for k,v in path.items() for way in directions if k+2*way in ar and k+2*way in path and path[k+2*way] > v+101]))

ans2 = Counter()

chl = 20

pot = {k:v for k,v in path.items() if round(abs(k.real-start.real) + abs(k.imag-start.imag)) <= chl}
cur = start
while cur != end:
    ans2 += Counter([v-path[cur]-round(abs(k.real-cur.real)+abs(k.imag-cur.imag)) for k,v in pot.items() if v-path[cur]-round(abs(k.real-cur.real)+abs(k.imag-cur.imag)) >= 100])
    for way in directions:
        if cur+way in path and path[cur+way] > path[cur]:
            for i in range(-chl,chl+1):
                old = cur + i*1j*way - way*(chl-abs(i))
                if old in pot:
                    del pot[old]
                new = cur+way + i*1j*way + way*(chl-abs(i))
                if new in path:
                    pot[new] = path[new]
            cur += way
            break

#for a,b in sorted([(k,v) for k,v in ans2.items()]):
#    print(b,a)

# second answer
print(sum( v for v in ans2.values()))