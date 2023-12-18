with open('/Users/evgeny/python/workbook/data/advent2023/advent_18.txt','r') as f:
    lines = f.readlines()
    for part in range(2):
        i = 0
        j = 0
        hor = [] #(i,j1,j2,fl)
        ver = [] #(i1,i2,j)
        if part == 0:
            prev = lines[-1].split()[0]
        else:
            prev = lines[-1].split()[2][-2]
        for k,line in enumerate(lines):
            if part == 0:
                if k < len(lines)-1:
                    nxt = lines[k+1].split()[0]
                else:
                    nxt = lines[0].split()[0]
            else:
                if k < len(lines)-1:
                    nxt = lines[k+1].split()[2][-2]
                else:
                    nxt = lines[0].split()[2][-2]
            way, x, color = line.split()
            if part == 1:
                way = color[-2]
                x = int(color[2:7],16)
            else:
                x = int(x)
            #print(f'{way} {x}')
            if way == 'U' or way == '3':
                if x > 1:
                    ver.append((i-x+1,i-1,j))
                i -= x
            if way == 'D' or way == '1':
                if x > 1:
                    ver.append((i+1,i+x-1,j))
                i += x
            if way == 'L' or way == '2':
                hor.append((i,j-x,j,prev == nxt))
                j -= x
            if way == 'R' or way == '0':
                hor.append((i,j,j+x,prev == nxt))
                j += x
            prev = way

        ans = 0
        ver.sort()
        hor.sort()
        h = 0
        while h < len(hor):
            i = hor[h][0]
            ar = []
            while h < len(hor) and hor[h][0] == i:
                ar.append((hor[h][1],hor[h][2],hor[h][3]))
                h += 1
            if h < len(hor):
                v = 0
                while v < len(ver) and ver[v][0] <= i:
                    if ver[v][1] >= i:
                        ar.append((ver[v][2],ver[v][2],True))
                    v += 1
                i2 = hor[h][0]
                if i2 > i+1:
                    v = 0
                    ar2 = []
                    while v < len(ver) and ver[v][0] <= i+1:
                        if ver[v][1] >= i+1:
                            ar2.append(ver[v][2])
                        v += 1
                    ar2.sort()
                    ans += sum([ar2[2*n+1] - ar2[2*n] + 1 for n in range(len(ar2)//2)])*(i2-i-1)

            ar.sort()
            fl = False
            for j1,j2,vert in ar:
                ans += j2-j1+1
                if not vert:
                    if fl:
                        ans -= j2-j1+1
                    continue
                if not fl:
                    prev = j2
                    fl = True
                else:
                    ans += j1 - prev - 1
                    fl = False


        print(ans)

