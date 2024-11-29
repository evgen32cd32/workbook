with open('/Users/evgeny/python/workbook/data/advent2023/advent_01.txt','r') as f:
    ans1 = 0
    for line in f.readlines():
        if line == '\n':
             continue
        for c in line:
            if c.isdigit():
                ans1 += 10*int(c)
                break
        for c in reversed(line):
            if c.isdigit():
                ans1 += int(c)
                break

# first answer
print(ans1)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_01.txt','r') as f:
    ans2 = 0
    d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for line in f.readlines():
        if line == '\n':
             continue
        for i in range(len(line)):
            c = line[i]
            if c.isdigit():
                ans2 += 10*int(c)
                break
            fl = False
            for k in d:
                if line[i:].startswith(k):
                    ans2 += 10*d[k]
                    fl = True
                    break
            if fl:
                break
        for i in range(len(line)-1,-1,-1):
            c = line[i]
            if c.isdigit():
                ans2 += int(c)
                break
            fl = False
            for k in d:
                if line[:i+1].endswith(k):
                    ans2 += d[k]
                    fl = True
                    break
            if fl:
                break

# second answer
print(ans2)