with open('/Users/evgeny/python/workbook/data/advent2023/advent_04.txt','r') as f:
    ans = 0
    for line in f.readlines():
        win, my = line.split('|')
        win = {int(x) for x in win.split()[2:]}
        cnt = 0
        for x in my.split():
            if int(x) in win:
                cnt += 1
        if cnt > 0:
            ans += 2**(cnt-1)

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_04.txt','r') as f:
    d = {0:1}
    for i,line in enumerate(f.readlines()):
        if i not in d:
            d[i] = 1
        win, my = line.split('|')
        win = {int(x) for x in win.split()[2:]}
        cnt = 0
        for x in my.split():
            if int(x) in win:
                cnt += 1
        for j in range(1, cnt+1):
            if i+j not in d:
                d[i+j] = 1
            d[i+j] += d[i]
            

# second answer
#print(d)
print(sum(d.values()))