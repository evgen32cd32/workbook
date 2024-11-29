with open('/Users/evgeny/python/workbook/data/advent2023/advent_02.txt','r') as f:
    ans = 0
    for gi, line in enumerate(f.readlines()):
        d = {'red':12, 'green':13, 'blue':14}
        games = line.split()
        fl = False
        for i in range(3,len(games),2):
            if games[i][-1] == ',' or games[i][-1] == ';':
                games[i] = games[i][:-1]
            if d[games[i]] < int(games[i-1]):
                fl = True
                break
        if fl:
            continue
        ans += gi + 1

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_02.txt','r') as f:
    ans = 0
    for gi, line in enumerate(f.readlines()):
        d = {'red':0, 'green':0, 'blue':0}
        games = line.split()
        fl = False
        for i in range(3,len(games),2):
            if games[i][-1] == ',' or games[i][-1] == ';':
                games[i] = games[i][:-1]
            #d[games[i]] -= int(games[i-1])
            if d[games[i]] < int(games[i-1]):
                d[games[i]] = int(games[i-1])
        ans += d['red'] * d['green'] * d['blue']

# second answer
print(ans)