def findLast(s,fl):
    ar = s.split("don't()")
    if len(ar) > 1:
        fl = False
    ar = ar[-1].split("do()")
    if len(ar) > 1:
        fl = True
    return fl

with open('/Users/evgen/projects/workbook/data/advent2024/advent_03.txt','r') as f:
    ans1 = 0
    ans2 = 0
    fl = True
    for line in f.readlines():
        ar_mul = line.split('mul(')
        fl = findLast(ar_mul[0],fl)
        for x in ar_mul[1:]:
            a1 = 0
            i = 0
            while i < len(x) and x[i].isdigit():
                a1 = int(x[i]) + a1 * 10
                i += 1
            if i == 0 or i == len(x) or x[i] != ',':
                continue
            a2 = 0
            j = 0
            while i+j+1 < len(x) and x[i+j+1].isdigit():
                a2 = int(x[i+j+1]) + a2 * 10
                j += 1
            if j == 0 or i+j+1 == len(x) or x[i+j+1] != ')':
                continue
            ans1 += a1 * a2
            if fl:
                ans2 += a1 * a2
            fl = findLast(x,fl)

# first answer
print(ans1)

# second answer
print(ans2)