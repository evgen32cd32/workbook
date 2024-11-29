with open('/Users/evgeny/python/workbook/data/advent2023/advent_09.txt','r') as f:
    ans = 0
    for line in f.readlines():
        diff = []
        diff.append([int(x) for x in line.split()])
        while any(x != 0 for x in diff[-1]):
            diff.append([diff[-1][i]-diff[-1][i-1] for i in range(1,len(diff[-1]))])
        for i in range(len(diff)-2,-1,-1):
            diff[i].append(diff[i][-1] + diff[i+1][-1])
        ans += diff[0][-1]

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_09.txt','r') as f:
    for line in f.readlines():
        ans = 0
        diff = []
        diff.append([int(x) for x in reversed(line.split())])
        while any(x != 0 for x in diff[-1]):
            diff.append([diff[-1][i]-diff[-1][i-1] for i in range(1,len(diff[-1]))])
        for i in range(len(diff)-2,-1,-1):
            diff[i].append(diff[i][-1] + diff[i+1][-1])
        ans += diff[0][-1]

# second answer
print(ans)
