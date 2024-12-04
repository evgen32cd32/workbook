with open('/Users/evgen/projects/workbook/data/advent2023/advent_21.txt','r') as f:
    start = None
    ar = f.readlines()
    for i in range(len(ar)-1):
        ar[i] = ar[i][:-1]
        j = ar[i].find('S')
        if j >= 0:
            start = (i,j)
            ar[i] = ar[i][:j] + '.' + ar[i][j+1:]
    if start is None:
        j = ar[-1].find('S')
        start = (len(ar)-1,j)
        ar[i] = ar[-1][:j] + '.' + ar[-1][j+1:]

def foo(start, steps):
    ar1 = {start}
    ar2 = set()
    for _ in range(steps):
        for i,j in ar1:
            if i > 0 and ar[i-1][j] != '#':
                ar2.add((i-1,j))
            if i < len(ar)-1 and ar[i+1][j] != '#':
                ar2.add((i+1,j))
            if j > 0 and ar[i][j-1] != '#':
                ar2.add((i,j-1))
            if j < len(ar[0])-1 and ar[i][j+1] != '#':
                ar2.add((i,j+1))
        ar1 = ar2
        ar2 = set()
    return len(ar1)

st = (0, 0, start[0], start[1])
vis = {True:{st},False:set()}
ar1 = {st}
ar2 = set()
fl = True
table = {}
#for _ in range(66+131*4+130):
#    fl = not fl
#    for a,b,i,j in ar1:
#        if i > 0 and ar[i-1][j] != '#' and (a,b,i-1,j) not in vis[fl]:
#            ar2.add((a,b,i-1,j))
#        if i < len(ar)-1 and ar[i+1][j] != '#' and (a,b,i+1,j) not in vis[fl]:
#            ar2.add((a,b,i+1,j))
#        if j > 0 and ar[i][j-1] != '#' and (a,b,i,j-1) not in vis[fl]:
#            ar2.add((a,b,i,j-1))
#        if j < len(ar[0])-1 and ar[i][j+1] != '#' and (a,b,i,j+1) not in vis[fl]:
#            ar2.add((a,b,i,j+1))
#
#        if i == 0 and ar[-1][j] != '#' and (a-1,b,len(ar)-1,j) not in vis[fl]:
#            ar2.add((a-1,b,len(ar)-1,j))
#            if (a-1,b) not in table:
#                table[(a-1,b)] = (_,len(ar)-1,j)
#        if i == len(ar)-1 and ar[0][j] != '#' and (a+1,b,0,j) not in vis[fl]:
#            ar2.add((a+1,b,0,j))
#            if (a+1,b) not in table:
#                table[(a+1,b)] = (_,0,j)
#        if j == 0 and ar[i][-1] != '#' and (a,b-1,i,len(ar[0])-1) not in vis[fl]:
#            ar2.add((a,b-1,i,len(ar[0])-1))
#            if (a,b-1) not in table:
#                table[(a,b-1)] = (_,i,len(ar[0])-1)
#        if j == len(ar[0])-1 and ar[i][0] != '#' and (a,b+1,i,0) not in vis[fl]:
#            ar2.add((a,b+1,i,0))
#            if (a,b+1) not in table:
#                table[(a,b+1)] = (_,i,0)
#    vis[fl] = vis[fl].union(ar2)
#    ar1 = ar2
#    ar2 = set()

for x in table:
    if x[0] > 0 and x[1] >= 0:
        print(x,table[x])

O = foo(start,131)
E = foo(start,132)

univs = (26501365-66)//131
leftover = (26501365-66)%131

edgeover = leftover - 66
preedge = leftover + 65

oc = (univs+1)*(univs-1)
ec = (univs+1)*univs*2 - oc

ans2 = (oc*O + ec*E) \
    + foo((65,130),leftover)+foo((65,0),leftover)+foo((0,65),leftover)+foo((130,65),leftover) \
    + univs*(foo((0,0),preedge)+foo((0,130),preedge)+foo((130,0),preedge)+foo((130,130),preedge)) \
    + (univs+1)*(foo((0,0),edgeover)+foo((0,130),edgeover)+foo((130,0),edgeover)+foo((130,130),edgeover)) + O
        
# first answer
print(foo(start,64))

# second answer
print(ans2)


#G = {i+j*1j:c for i,r in enumerate(open('/Users/evgen/projects/workbook/data/advent2023/advent_21.txt'))
#              for j,c in enumerate(r) if c in '.S'}
#
#done = []
#todo = {x for x in G if G[x]=='S'}
#cmod = lambda x: complex(x.real%131, x.imag%131)
#
#for s in range(3 * 131):
#    if s == 64: print(len(todo))
#    if s%131 == 65: done.append(len(todo))
#
#    todo = {p+d for d in {1, -1, 1j, -1j}
#                for p in todo if cmod(p+d) in G}
#
#f = lambda n,a,b,c: a+n*(b-a+(n-1)*(c-b-b+a)//2)
#print(f(26501365 // 131, *done))
#605247138198755