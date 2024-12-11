with open('/Users/evgen/projects/workbook/data/advent2024/advent_11.txt','r') as f:
    todo = [int(x) for x in f.readline().split()]

d = {}

def rec(x,bl):
    if (x,bl) in d:
        return d[(x,bl)]
    if bl == 0:
        d[(x,0)] = 1
        return 1
    if x == 0:
        d[(x,bl)] = rec(1,bl-1)
    elif len(str(x))%2 == 0:
        l = len(str(x))//2
        d[(x,bl)] = rec(int(str(x)[:l]),bl-1) + rec(int(str(x)[l:]),bl-1)
    else:
        d[(x,bl)] = rec(x*2024,bl-1)
    return d[(x,bl)]

# first answer
print(sum([rec(x,25) for x in todo]))

# second answer
print(sum([rec(x,75) for x in todo]))