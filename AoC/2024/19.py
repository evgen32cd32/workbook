from functools import cache

with open('/Users/evgen/projects/workbook/data/advent2024/advent_19.txt','r') as f:
    inp = f.readlines()
    towels = set(inp[0][:-1].split(', '))
    designs = [s[:-1] if s[-1] == '\n' else s for s in inp[2:]]

@cache
def rec2(des):
    ans = 0
    if des in towels:
        ans += 1
    return ans + sum(rec2(des[i:]) for i in range(1,len(des)) if des[:i] in towels)

res = [rec2(x) for x in designs]

#for a,b in zip(designs,res):
#    print(a,b)

# first answer
print(sum([x > 0 for x in res]))

# second answer
print(sum([x for x in res]))