from itertools import combinations

with open('/Users/evgeny/python/workbook/data/advent2023/advent_12.txt','r') as f:
    ans = 0
    for line in f.readlines():
        a, b  = line.split()
        b = [int(x) for x in b.split(',')]
        unk_ar = []
        brk = 0
        for i,c in enumerate(a):
            if c == '?':
                unk_ar.append(i)
            if c == '#':
                brk += 1
        if len(unk_ar) + brk == sum(b):
            ans += 1
            continue
        for t in combinations(unk_ar, len(unk_ar) - (sum(b) - brk)):
            at = list(a)
            for i in t:
                at[i] = '.'
            at = [x for x in (''.join(at)).split('.') if x != '']
            if len(at) != len(b):
                continue
            fl = False
            for x, y in zip(at,b):
                if len(x) != y:
                    fl = True
                    break
            if fl:
                continue
            ans += 1

        

# first answer
print(ans)
