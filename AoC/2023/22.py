class Block:
    def __init__(self,bot):
        self.top = set()
        self.bot = bot

with open('/Users/evgen/projects/workbook/data/advent2023/advent_22.txt','r') as f:
    ar = []
    for l in f.readlines():
        a,b = l.split('~')
        ar.append(tuple((min(x,y),max(x,y)) for x,y in zip(map(int,reversed(a.split(','))),map(int,reversed(b.split(','))))))
    ar.sort()
    G = {}
    blocks = []
    for i,bl in enumerate(ar):
        for z in range(bl[0][0]-1,-1,-1):
            bot = {G[(z,x,y)] for x in range(bl[1][0],bl[1][1]+1) for y in range(bl[2][0],bl[2][1]+1) if (z,x,y) in G}
            if len(bot) > 0:
                break
        z += 1
        blocks.append(Block(bot))
        for x in range(bl[1][0],bl[1][1]+1):
            for y in range(bl[2][0],bl[2][1]+1):
                for nz in range(z,z + bl[0][1] - bl[0][0] + 1):
                    G[(nz,x,y)] = i
        for j in bot:
            blocks[j].top.add(i)
    #for i,bl in enumerate(blocks):
    #    print(chr(ord('A')+i),{chr(ord('A')+j) for j in bl.bot},{chr(ord('A')+j) for j in bl.top})
    #    #print([k for k in G if G[k]==i])

ans2 = 0
for i,bl in enumerate(blocks):
    fall = {i}
    tocheck = bl.top.copy()
    while len(tocheck) > 0:
        tc = tocheck.pop()
        if len(blocks[tc].bot - fall) == 0:
            fall.add(tc)
            tocheck.update(blocks[tc].top)
    ans2 += len(fall) - 1

# first answer
print(sum([1 for i,bl in enumerate(blocks) if len(bl.top) == 0 or all([len(blocks[j].bot - {i}) > 0 for j in bl.top])]))

# second answer
print(ans2)