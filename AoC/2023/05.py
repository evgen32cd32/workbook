with open('/Users/evgeny/python/workbook/data/advent2023/advent_05.txt','r') as f:
    lines = f.readlines()
    ar1 = {int(x) for x  in lines[0].split()[1:]}
    i = 3
    while i < len(lines):
        ar2 = set()
        while i<len(lines) and lines[i] != '\n':
            b,a,r = [int(x) for x in lines[i].split()]
            for x in ar1.copy():
                if x >= a and x < a+r:
                    ar2.add(b+x-a)
                    ar1.remove(x)
                    #print(f'{ar1} {ar2}')
            i += 1
        ar1  = ar2.union(ar1)
        #print(f'{ar1}')
        i += 2

# first answer
print(min(ar1))



with open('/Users/evgeny/python/workbook/data/advent2023/advent_05.txt','r') as f:
    lines = f.readlines()
    ar = lines[0].split()[1:]
    d1 = {}
    for i in range(len(ar)//2):
        d1[int(ar[2*i])] = int(ar[2*i+1])
    i = 3
    while i < len(lines):
        d2 = {}
        while i<len(lines) and lines[i] != '\n':
            b,a,r = [int(x) for x in lines[i].split()]
            for x in list(d1.keys()):
                if x < a+r and x+d1[x] > a:
                    if x+d1[x] > a+r:
                        d1[a+r] = x+d1[x] - (a+r)
                    d2[b + max([x,a]) - a] = min([a+r,x+d1[x]]) - max([x,a])
                    if x >= a:
                        del d1[x]
                    else:
                        d1[x] = a - x
                    #print(d2)
            i += 1
        for k, v in d1.items():
            d2[k] = v
        d1 = d2
        #print(f'cycle: {d1}')
        i += 2

# second answer
print(min(d1.keys()))