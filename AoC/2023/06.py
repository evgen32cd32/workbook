import math

with open('/Users/evgeny/python/workbook/data/advent2023/advent_06.txt','r') as f:
    ans1 = 1
    lines = f.readlines()
    times = [int(x) for x in lines[0].split()[1:]]
    dists = [int(x) for x in lines[1].split()[1:]]
    for t,l in zip(times,dists):
        d = t**2 - 4*l
        x1 = (t - math.sqrt(d))/2
        x2 = (t + math.sqrt(d))/2
        xl = math.ceil(min([x1,x2]))
        xh = math.floor(max([x1,x2]))
        ans1 *= (xh-xl+1)
    t2 = int(''.join(lines[0].split()[1:]))
    l2 = int(''.join(lines[1].split()[1:]))
    d = t2**2 - 4*l2
    x1 = (t2 - math.sqrt(d))/2
    x2 = (t2 + math.sqrt(d))/2
    ans2 = math.floor(max([x1,x2])) - math.ceil(min([x1,x2])) + 1

# first answer
print(ans1)

# second answer
print(ans2)