from itertools import cycle

d = {}

def cmp(s1, s2):
    for c1,c2 in zip(s1,s2):
        if c2 != '?' and c1 != c2:
            return False
    return True

def rec(a, b):
    if len(a) == 0:
        return 0
    i = 0
    while i < len(a) and a[i] == '.':
        i += 1
    a = a[i:]
    if (a,b) in d:
        return d[(a,b)]
    ta = a
    ans = 0
    while len(a) >= sum(b) + len(b)-1:
        if cmp('#'*b[0],a):
            if len(b) == 1:
                if cmp(cycle('.'),a[b[0]:]):
                    ans += 1
            else:
                if cmp('.',a[b[0]]):
                    ans += rec(a[b[0]+1:],b[1:])
        if a[0] == '?':
            i = 1
            while i < len(a) and a[i] == '.':
                i += 1
            a = a[i:]
        else:
            break
    d[(ta,b)] = ans
    return ans

with open('/Users/evgeny/python/workbook/data/advent2023/advent_12.txt','r') as f:
    ans = 0
    for line in f.readlines():
        a, b  = line.split()
        i = 0
        while a[i] == '.':
            i += 1
        j = len(a) - 1
        while a[j] == '.':
            j -= 1
        a = a[i:j+1]
        b = tuple(int(x) for x in b.split(','))

        ans += rec(a,b)

        

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_12.txt','r') as f:
    ans = 0
    for line in f.readlines():
        a, b  = line.split()
        a = '?'.join([a,a,a,a,a])
        i = 0
        while a[i] == '.':
            i += 1
        j = len(a) - 1
        while a[j] == '.':
            j -= 1
        a = a[i:j+1]
        b = tuple(int(x) for x in b.split(','))*5

        ans += rec(a,b)

        

# second answer
print(ans)
