from collections import deque

with open('/Users/evgen/projects/workbook/data/advent2024/advent_09.txt','r') as f:
    ans2 = 0
    data = []
    spaces = deque()
    i = 0
    j = 0
    inp = f.readline()
    while j < len(inp):
        x = int(inp[j])
        data.extend([(i+k,j//2) for k in range(x)])
        i += x
        j += 1
        if j < len(inp):
            x = int(inp[j])
            spaces.extend([i+k for k in range(x)])
            i += x
            j += 1
    ndata = []
    while len(spaces) > 0 and spaces[0] < data[-1][0]:
        ndata.append((spaces.popleft(),data.pop()[1]))
    ans1 = sum([a*b for a,b in data+ndata])

with open('/Users/evgen/projects/workbook/data/advent2024/advent_09.txt','r') as f:
    ans2 = 0
    data = []
    spaces = []
    i = 0
    j = 0
    inp = f.readline()
    while j < len(inp):
        x = int(inp[j])
        if x > 0:
            data.append((i,x,j//2))
        i += x
        j += 1
        if j < len(inp):
            x = int(inp[j])
            if x > 0:
                spaces.append((i,x))
            i += x
            j += 1
    ndata = []
    while len(data) > 0:
        x = data.pop()
        ni = x[0]
        for j in range(len(spaces)):
            sp = spaces[j]
            if sp[0] >= x[0]:
                break
            if sp[1] >= x[1]:
                ni = sp[0]
                if sp[1] == x[1]:
                    spaces = spaces[:j] + spaces[j+1:]
                else:
                    spaces[j] = (sp[0]+x[1],sp[1]-x[1])
                break
        ndata.append((ni,x[1],x[2]))
        #pa = 0
        #for a,b,c in sorted(ndata+data):
        #    if pa < a:
        #        print('.'*(a-pa),end='')
        #    print(str(c)*b,end='')
        #    pa = a+b
        #print('\n',end='')
    ans2 = sum([(a+i)*c for a,b,c in ndata for i in range(b)])

# first answer
print(ans1)

# second answer
print(ans2)