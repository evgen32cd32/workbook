with open('/Users/evgeny/python/workbook/data/advent2022/advent_05.txt','r') as f:
    n = 0
    d = {}
    cratesFl = True
    commandsFl = False
    for line in f.readlines():
        if cratesFl:
            if n == 0:
                n = int(len(line)/4)
                for i in range(0,n):
                    d[i+1] = []
            for i in range(0,n):
                c = line[1 + i * 4]
                if c.isdigit():
                    cratesFl = False
                    for k in d:
                        d[k].reverse()
                    break
                if c != ' ':
                    d[i+1].append(c)
        elif line.startswith('move'):
            commandsFl = True
        if commandsFl:
            splitted = line.split()
            for i in range(int(splitted[1])):
                d[int(splitted[5])].append(d[int(splitted[3])].pop())

ans  = ''
for k in d:
    ans = ans + d[k].pop()

# first answer
print(ans)


with open('/Users/evgeny/python/workbook/data/advent2022/advent_05.txt','r') as f:
    n = 0
    d = {}
    cratesFl = True
    commandsFl = False
    for line in f.readlines():
        if cratesFl:
            if n == 0:
                n = int(len(line)/4)
                for i in range(0,n):
                    d[i+1] = []
            for i in range(0,n):
                c = line[1 + i * 4]
                if c.isdigit():
                    cratesFl = False
                    for k in d:
                        d[k].reverse()
                    break
                if c != ' ':
                    d[i+1].append(c)
        elif line.startswith('move'):
            commandsFl = True
        if commandsFl:
            splitted = line.split()
            cnt = int(splitted[1])
            frm = int(splitted[3])
            to = int(splitted[5])
            d[to] = d[to] + d[frm][-cnt:]
            d[frm] = d[frm][:-cnt]

ans  = ''
for k in d:
    ans = ans + d[k].pop()

# second answer
print(ans)
