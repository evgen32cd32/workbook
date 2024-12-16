with open('/Users/evgen/projects/workbook/data/advent2024/advent_16.txt','r') as f:
    ar = {i+1j*j:c for i,l in enumerate(f.readlines()) for j,c in enumerate(l) if c in '.ES'}
    start = [k for k,v in ar.items() if v == 'S'].pop()
    stway = 1j
    rotcost = 1000
    stcost = 1
    cnts = {(start,stway):0}
    to_check = [(start,stway,set())]
    to_do = []
    ans1 = None
    while len(to_check) > 0:
        for cur, way, visited in to_check:
            new = cur
            nvis = visited.copy()
            while new in ar and new not in visited:
                if (new,way) not in cnts:
                    cnts[(new,way)] = cnts[(new-way,way)]+stcost
                if new != cur and cnts[(new-way,way)]+stcost > cnts[(new,way)]:
                    break
                if ar[new] == 'E':
                    if ans1 is None:
                        ans1 = cnts[(new,way)]
                        best = {new}
                    if ans1 == cnts[(new,way)]:
                        best.update(nvis)
                if (new,way*1j) not in cnts or cnts[(new,way*1j)] == cnts[(new,way)]+rotcost:
                    cnts[(new,way*1j)] = cnts[(new,way)]+rotcost
                    to_do.append((new,way*1j,nvis.copy()))
                if (new,-way*1j) not in cnts or cnts[(new,-way*1j)] == cnts[(new,way)]+rotcost:
                    cnts[(new,-way*1j)] = cnts[(new,way)]+rotcost
                    to_do.append((new,-way*1j,nvis.copy()))
                nvis = nvis.union({new})
                new = new + way
        to_check = to_do
        to_do = []

#out = []
#for i in range(max([int(k.real) for k in ar])+2):
#    out.append(['#']*(max([int(k.imag) for k in ar])+2))
#for k in ar:
#    out[int(k.real)][int(k.imag)] = 'O' if k in best else '.'
#
#for l in out:
#    print(''.join(l))

# first answer
print(ans1)

# second answer
print(len(best))