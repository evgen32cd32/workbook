with open('/Users/evgeny/python/workbook/data/advent2023/advent_14.txt','r') as f:
    ans = 0
    ar = []
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        if len(ar) == 0:
            ar = [c for c in line]
        else:
            for i in range(len(line)):
                ar[i] += line[i]
    #print(ar)
    for x in ar:
        space = 0
        for i,c in enumerate(x):
            if c =='#':
                space = i+1
            if c == 'O':
                ans += len(ar) - space
                #print(ans)
                space += 1
# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_14.txt','r') as f:
    d = {}
    lib = []
    ar = []
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        l = len(line)
        ar.extend([c for c in line])
    s = ''.join(ar)
    while s not in d:
        lib.append(s)
        d[s] = len(lib) - 1
        #print('north')
        for i in range(l):
            space = i
            for j in range(len(ar)//l):
                if ar[i+j*l] == '#':
                    space = i+(j+1)*l
                if ar[i+j*l] == 'O':
                    ar[i+j*l] = '.'
                    ar[space] = 'O'
                    space += l
        #for j in range(len(ar)//l):
        #    print(''.join(ar[j*l:(j+1)*l]))
        #print('west')
        for j in range(len(ar)//l):
            space = j*l
            for i in range(l):
                if ar[i+j*l] == '#':
                    space = i+1+(j)*l
                if ar[i+j*l] == 'O':
                    ar[i+j*l] = '.'
                    ar[space] = 'O'
                    space += 1
        #for j in range(len(ar)//l):
        #    print(''.join(ar[j*l:(j+1)*l]))
        #print('south')
        for i in range(l):
            space = len(ar)-l+i
            for j in range((len(ar)//l)-1,-1,-1):
                if ar[i+j*l] == '#':
                    space = i+(j-1)*l
                if ar[i+j*l] == 'O':
                    #print(space)
                    #print(i+j*l)
                    ar[i+j*l] = '.'
                    ar[space] = 'O'
                    space -= l
        #for j in range(len(ar)//l):
        #    print(''.join(ar[j*l:(j+1)*l]))
        #print('east')
        for j in range(len(ar)//l):
            space = (j+1)*l-1
            for i in range(l-1,-1,-1):
                if ar[i+j*l] == '#':
                    space = i-1+(j)*l
                if ar[i+j*l] == 'O':
                    ar[i+j*l] = '.'
                    ar[space] = 'O'
                    space -= 1
        #for j in range(len(ar)//l):
        #    print(''.join(ar[j*l:(j+1)*l]))
        s = ''.join(ar)
    cycle = len(lib)-d[s]
    s = lib[d[s]+(1000000000-d[s])%cycle]
    ans = 0
    for i in range(l):
        for j in range(len(ar)//l):
            if s[i+j*l] == 'O':
                ans += len(ar)//l - j

# second answer
print(ans)