with open('/Users/evgeny/python/workbook/data/advent2023/advent_11.txt','r') as f:
    ar = []
    for line in f.readlines():
        if line[-1] == '\n':
             line = line[:-1]
        if len(ar) == 0:
            ar = ['']*len(line)
        for i,c in enumerate(line):
            ar[i] = ar[i] + c
        if line.find('#') == -1:
            for i,c in enumerate(line):
                ar[i] = ar[i] + c
    lines = ar
    ar = ['']*len(lines[0])
    for line in lines:
        for i,c in enumerate(line):
            ar[i] = ar[i] + c
        if line.find('#') == -1:
            for i,c in enumerate(line):
                ar[i] = ar[i] + c
    galaxies = []
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j] == '#':
                galaxies.append((i,j))
    ans = 0
    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_11.txt','r') as f:
    galaxies = []
    for i,line in enumerate(f.readlines()):
        if line[-1] == '\n':
             line = line[:-1]
        for j,c in enumerate(line):
            if c == '#':
                galaxies.append([i,j])
    ind = 0
    a = 0
    for i in range(len(galaxies)):
        if galaxies[i][0] != ind:
            ind += 1
        while galaxies[i][0] != ind:
            ind += 1
            a += 999999
        galaxies[i][0] += a

    galaxies.sort(key=lambda x: x[1])

    ind = 0
    a = 0
    for i in range(len(galaxies)):
        if galaxies[i][1] != ind:
            ind += 1
        while galaxies[i][1] != ind:
            ind += 1
            a += 999999
        galaxies[i][1] += a
    ans = 0
    for i in range(len(galaxies)):
        for j in range(i+1,len(galaxies)):
            ans += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

# second answer
print(ans)