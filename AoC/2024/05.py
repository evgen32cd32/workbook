with open('/Users/evgen/projects/workbook/data/advent2024/advent_05.txt','r') as f:
    rules = {}
    rl = True
    ans1 = 0
    ans2 = 0
    for line in f.readlines():
        if line == '\n':
            rl = False
            continue
        if rl:
            r = line.split('|')
            pg = r[1][:-1]
            if pg not in rules:
                rules[pg] = set()
            rules[pg].add(r[0])
            continue
        tofind = set()
        if line[-1] == '\n':
            line = line[:-1]
        good = True
        ar = line.split(',')
        for p in ar:
            if p in tofind:
                good = False
                break
            if p in rules:
                tofind.update(rules[p])
        if good:
            ans1 += int(ar[len(ar)//2])
        else:
            sar = set(ar)
            nar = [x for x in sar if x not in rules]
            sar.difference_update(nar)
            while len(sar) > 0:
                tar = [x for x in sar if all([a not in sar for a in rules[x]])]
                nar.extend(tar)
                sar.difference_update(tar)
            ans2 += int(nar[len(nar)//2])

# first answer
print(ans1)

# second answer
print(ans2)