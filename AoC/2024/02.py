with open('/Users/evgen/projects/workbook/data/advent2024/advent_02.txt','r') as f:
    ans1 = 0
    ans2 = 0
    for line in f.readlines():
        #part 1

        #prev = None
        #asc = None
        #good = True
        #for x in line.split():
        #    a = int(x)
        #    if prev is not None:
        #        diff = a - prev
        #        if asc is None:
        #            asc = diff > 0
        #        if (asc == (diff <= 0)) or abs(diff) < 1 or abs(diff) > 3:
        #            good = False
        #            break
        #    prev = a
        #if good:
        #    ans1 += 1
        
        #part 2 + 1
        def checkBad(sign, x):
            return x*sign < 0 or abs(x) < 1 or abs(x) > 3
        prev = None
        sign = 0
        diff2 = []
        for x in line.split():
            if prev is not None:
                diff2.append(int(x) - prev)
                sign += -1 if diff2[-1] < 0 else 1
            prev = int(x)
        if sign == 0:
            sign = 1
        err = [i for i,x in enumerate(diff2) if checkBad(sign, x)]
        if len(err) == 0:
            ans1 += 1
            continue
        if len(err) == 2 and err[1] - err[0] == 1 and not checkBad(sign, diff2[err[1]] + diff2[err[0]]):
            ans2 += 1
            continue
        if len(err) == 1:
            if err[0] == 0 or err[0] == len(diff2) - 1:
                ans2 += 1
                continue
            if not checkBad(sign, diff2[err[0]] + diff2[err[0] + 1]) or not checkBad(sign, diff2[err[0]] + diff2[err[0] - 1]):
                ans2 += 1

# first answer
print(ans1)

# second answer
print(ans2 + ans1)