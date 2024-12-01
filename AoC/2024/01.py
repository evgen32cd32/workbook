from collections import Counter

with open('/Users/evgen/projects/workbook/data/advent2024/advent_01.txt','r') as f:
    l1 = []
    l2 = []
    for line in f.readlines():
        a,b = (int(x) for x in line.split())
        l1.append(a)
        l2.append(b)
l1.sort()
l2.sort()

d = Counter(l2)

# first answer
print(sum([abs(a-b) for a,b in zip(l1,l2)]))

# second answer
print(sum([x*d[x] for x in l1]))