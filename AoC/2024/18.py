edge = 70
bytes = 1024
#edge = 6
#bytes = 12

ar = {i+1j*j for i in range(edge+1) for j in range(edge+1)}

dirs = [-1,-1j,1,1j]

def get_path(start,end):
    to_visit = [(start,[start])]
    visited = {start}
    new_visit = []
    step = -1
    while len(to_visit) > 0:
        step += 1
        for cur, path in to_visit:
            if cur == end:
                #path.reverse()
                return path
            for way in dirs:
                if cur+way in ar and cur+way not in visited:
                    visited.add(cur+way)
                    new_visit.append((cur+way,path+[cur+way]))
        to_visit = new_visit
        new_visit = []
    return None

def out(cur,path=None):
    ot = []
    for _ in range(edge+1):
        ot.append(['#']*(edge+1))
    for k in ar:
        ot[int(k.imag)][int(k.real)] = '.'
    if path is not None:
        for p in path:
            ot[int(p.imag)][int(p.real)] = '+'
    ot[int(cur.imag)][int(cur.real)] = '@'
    for l in ot:
        print(''.join(l))
    print()

with open('/Users/evgen/projects/workbook/data/advent2024/advent_18.txt','r') as f:
    for k,line in enumerate(f.readlines()):
        if k == bytes:
            path = get_path(0, edge+edge*1j)
            steps = len(path)-1
            spath = set(path)
        i,j = [int(x) for x in line.split(',')]
        ar.remove((i+1j*j))
        if k >= bytes and (i+1j*j) in spath:
            #out((i+1j*j),path)
            path = get_path(0, edge+edge*1j)
            if path is None:
                break
            spath = set(path)

# first answer
print(steps)

# second answer
print(str(i)+','+str(j))