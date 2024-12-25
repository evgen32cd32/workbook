locks = []
keys = []

cur = set()
ci = 0

with open('/Users/evgen/projects/workbook/data/advent2024/advent_25.txt','r') as f:
    for i,line in enumerate(f.readlines()):
        if line == '\n':
            if 0 in cur:
                locks.append(cur)
            else:
                keys.append(cur)
            cur = set()
            ci = i+1
            continue
        for j,c in enumerate(line):
            if c == '#':
                cur.add(i-ci+1j*j)
    if 0 in cur:
        locks.append(cur)
    else:
        keys.append(cur)

# first answer
print(sum([len(k & l) == 0 for k in keys for l in locks]))