from itertools import repeat

with open('/Users/evgeny/python/workbook/data/advent2022/advent_08.txt','r') as f:
    treeArray = []
    treeMarker = []
    treeScore = []
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        treeArray.append([int(x) for x in line])
        treeMarker.append([0 for _ in line])
        treeScore.append([1 for _ in line])
        ls = set()
        rs = set()
        N = len(line)
        for i in range(N-2):
            ls.add(treeArray[-1][i])
            rs.add(treeArray[-1][N-i-1])
            if all(treeArray[-1][i+1] > x for x in ls):
                treeMarker[-1][i+1] = 1
            if all(treeArray[-1][N-i-2] > x for x in rs):
                treeMarker[-1][N-i-2] = 1
            cnt = 1
            k = i
            while k > 0 and treeArray[-1][i+1] > treeArray[-1][k]:
                k = k - 1
                cnt = cnt + 1
            treeScore[-1][i+1] = treeScore[-1][i+1] * cnt
            cnt = 1
            k = N-i-1
            while k < N-1 and treeArray[-1][N-i-2] > treeArray[-1][k]:
                k = k + 1
                cnt = cnt + 1
            treeScore[-1][N-i-2] = treeScore[-1][N-i-2] * cnt
    for j in range(1,len(treeArray[0])-1):
        ts = set()
        bs = set()
        N = len(treeArray)
        for i in range(N-2):
            ts.add(treeArray[i][j])
            bs.add(treeArray[N-i-1][j])
            if all(treeArray[i+1][j] > x for x in ts):
                treeMarker[i+1][j] = 1
            if all(treeArray[N-i-2][j] > x for x in bs):
                treeMarker[N-i-2][j] = 1
            cnt = 1
            k = i
            while k > 0 and treeArray[i+1][j] > treeArray[k][j]:
                k = k - 1
                cnt = cnt + 1
            treeScore[i+1][j] = treeScore[i+1][j] * cnt
            cnt = 1
            k = N-i-1
            while k < N-1 and treeArray[N-i-2][j] > treeArray[k][j]:
                k = k + 1
                cnt = cnt + 1
            treeScore[N-i-2][j] = treeScore[N-i-2][j] * cnt


treeMarker[0][:] = repeat(1,len(treeMarker[0]))
treeMarker[-1][:] = repeat(1,len(treeMarker[0]))
treeScore[0][:] = repeat(0,len(treeScore[0]))
treeScore[-1][:] = repeat(0,len(treeScore[0]))
for i in range(1,len(treeMarker)-1):
    treeMarker[i][0] = 1
    treeMarker[i][-1] = 1
    treeScore[i][0] = 0
    treeScore[i][-1] = 0

firstAns = sum([sum(x) for x in treeMarker])

secondAns = max([max(x) for x in treeScore])


#for i in range(len(treeArray)):
#    print('{} {}'.format(treeArray[i],treeScore[i]))

# first answer
print(firstAns)

# second answer
print(secondAns)
