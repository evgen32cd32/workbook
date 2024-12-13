import sys
sys.setrecursionlimit(10000)

with open('/Users/evgen/projects/workbook/data/advent2023/advent_23.txt','r') as f:
    ar = {i+1j*j:c for i,l in enumerate(f.readlines()) for j,c in enumerate(l) if c in '.^<>v'}
    re = [k.real for k in ar]
    start = [x for x in ar if x.real == min(re)].pop()
    end = [x for x in ar if x.real == max(re)].pop()

    directions = {-1:'^',1j:'>',-1j:'<',1:'v'}

class Road:
    def __init__(self,id):
        self.id = id
        self.edge = {}
        self.l = 1
        self.one_side = {}

crossroads = {}

startroad = Road(0)
roadsdict = {0:startroad}

def recGraph(r,cur,prev):
    nar = [cur+x for x in directions if cur+x in ar and cur+x != prev]
    while len(nar) == 1:
        prev = cur
        cur = nar[0]
        r.l += 1
        nar = [cur+x for x in directions if cur+x in ar and cur+x != prev]
    if len(nar) == 0:
        if cur == end:
            r.edge[end] = None
            r.one_side[(True,end)] = None
            r.one_side[(False,end)] = None
        return
    if cur not in crossroads:
        crossroads[cur] = set()
    crossroads[cur].add(r)
    r.edge[cur] = prev
    direction = cur-prev
    if ar[prev] in '.' + directions[direction]:
        r.one_side[(False,cur)] = prev
    if ar[prev] in '.' + directions[-direction]:
        r.one_side[(True,cur)] = prev
    for x in nar:
        if x not in {k for xr in crossroads[cur] for v,k in xr.edge.items() if cur == v}:
            idroad = len(roadsdict)
            newroad = Road(idroad)
            roadsdict[idroad] = newroad
            crossroads[cur].add(newroad)
            newroad.edge[cur] = x
            direction = cur-x
            if ar[x] in '.' + directions[direction]:
                newroad.one_side[(False,cur)] = x
            if ar[x] in '.' + directions[-direction]:
                newroad.one_side[(True,cur)] = x
            recGraph(newroad,x,cur)

recGraph(startroad,start+1,start)

def foo(one_sided):
    fd = {}
    for i,road in roadsdict.items():
        if i == 0:
            continue
        if one_sided:
            available = [(x[1],e) for x,e in road.one_side.items() if x[0]]
            available_exit = [(x[1],e) for x,e in road.one_side.items() if not x[0]]
        else:
            available = road.edge.items()
            available_exit = road.edge.items()
        if end in {x for x,_ in available}:
            continue
        for cross, edge in available:
            othercrosses = [x for x,_ in available_exit if x != cross]
            if len(othercrosses) > 2:
                assert()
            if len(othercrosses) == 1:
                othercross = othercrosses.pop()
            if one_sided:
                fd[(road.id,edge)] = [(x.id,z) for x in crossroads[othercross] for y,z in x.one_side.items() if y[0] and y[1] == othercross and x.id != road.id]
            else:
                fd[(road.id,edge)] = [(x.id,z) for x in crossroads[othercross] for y,z in x.edge.items() if y == othercross and x.id != road.id]

    for cr in crossroads.values():
        xar = [x for x in cr if end in x.edge]
        if len(xar) > 0:
            endroadid = xar[0].id
            preend = {x.id for x in cr if x.id != endroadid}
            break
    
    def check_road(visit,roadid):
        return (visit//(2**roadid))%2 == 1
    
    def add_road(visit,roadid):
        return visit if check_road(visit,roadid) else visit + 2**roadid

    firstcross = next(iter(startroad.edge.keys()))
    if one_sided:
        todo = [(x.id,z) for x in crossroads[firstcross] for y,z in x.one_side.items() if y[0] and x.id != 0 and y[1] == firstcross]
    else:
        todo = [(x.id,z) for x in crossroads[firstcross] for y,z in x.edge.items() if x.id != 0 and y == firstcross]
    poststart = {x[0] for x in todo}
    todo = [(a,b,sum(add_road(0,x) for x in poststart),str(a)) for a,b in todo]

    vv = set()

    ans2 = 0
    while len(todo) > 0:
        crid,edge,v,path = todo.pop()
        vv.add((crid,edge,v))
        if crid in preend:
            ans2 = max(ans2,sum([roadsdict[int(x)].l for x in path.split(' ')] + [roadsdict[endroadid].l,startroad.l]))
            continue
        newv = v
        for ncrid, _ in fd[(crid,edge)]:
            newv = add_road(newv,ncrid)
        if v == newv:
            continue
        for ncrid, nedge in fd[(crid,edge)]:
            if check_road(v,ncrid):
                continue
            if (ncrid,nedge,v) in vv:
                continue
            todo.append((ncrid,nedge,newv,path + ' ' + str(ncrid)))
    return ans2


# first answer
print(foo(True))

# second answer
print(foo(False))