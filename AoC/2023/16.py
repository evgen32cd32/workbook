with open('/Users/evgeny/python/workbook/data/advent2023/advent_16.txt','r') as f:
    ar = []
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        ar.append(line)
    
    starts = []
    starts.extend([((i,0),'r') for i in range(len(ar))])
    starts.extend([((i,len(ar[0])-1),'l') for i in range(len(ar))])
    starts.extend([((0,j),'d') for j in range(len(ar[0]))])
    starts.extend([((len(ar)-1,j),'u') for j in range(len(ar[0]))])

    ans = 0
    first = True

    for st in starts:
        beams = [((st[0][0],st[0][1]),st[1])]
        hist = set()
        heatmap = []
        for i in range(len(ar)):
            heatmap.append([0]*len(ar[0]))

        while len(beams) > 0:
            coords, way = beams.pop()
            i,j = coords
            while i >= 0 and i < len(ar) and j >= 0 and j < len(ar[0]) and ((i,j),way) not in hist:
                heatmap[i][j] = 1
                hist.add(((i,j),way))
                if ar[i][j] == '.':
                    if way == 'r':
                        j += 1
                    elif way == 'l':
                        j -= 1
                    elif way == 'u':
                        i -= 1
                    elif way == 'd':
                        i += 1
                elif ar[i][j] == '/':
                    if way == 'r':
                        way = 'u'
                        i -= 1
                    elif way == 'l':
                        way = 'd'
                        i += 1
                    elif way == 'u':
                        way = 'r'
                        j += 1
                    elif way == 'd':
                        way = 'l'
                        j -= 1
                elif ar[i][j] == '\\':
                    if way == 'r':
                        way = 'd'
                        i += 1
                    elif way == 'l':
                        way = 'u'
                        i -= 1
                    elif way == 'u':
                        way = 'l'
                        j -= 1
                    elif way == 'd':
                        way = 'r'
                        j += 1
                elif ar[i][j] == '-':
                    if way == 'r':
                        j += 1
                    elif way == 'l':
                        j -= 1
                    elif way == 'u' or way == 'd':
                        way = 'l'
                        j -= 1
                        beams.append(((i,j+1),'r'))
                elif ar[i][j] == '|':
                    if way == 'r' or way == 'l':
                        way = 'u'
                        i -= 1
                        beams.append(((i+1,j),'d'))
                    elif way == 'u':
                        i -= 1
                    elif way == 'd':
                        i += 1
        tmp = sum([sum(x) for x in heatmap])
        if first:
            first = False
            # first answer
            print(tmp)
        if tmp > ans:
            ans = tmp



# second answer
print(ans)