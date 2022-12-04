with open('/Users/evgeny/python/workbook/data/advent2022/advent_04.txt','r') as f:
    cnt = 0
    for line in f.readlines():
        pair = [list(map(int,x.split('-'))) for x in line[:-1].split(',')]
        if pair[0][0] == pair[1][0]:
            cnt = cnt + 1
            continue
        pair.sort(key= lambda x : x[0])
        if pair[0][1] >= pair[1][1]:
            cnt = cnt + 1

# first answer
print(cnt)


with open('/Users/evgeny/python/workbook/data/advent2022/advent_04.txt','r') as f:
    cnt = 0
    for line in f.readlines():
        pair = [list(map(int,x.split('-'))) for x in line[:-1].split(',')]
        if pair[0][0] == pair[1][0]:
            cnt = cnt + 1
            continue
        pair.sort(key= lambda x : x[0])
        if pair[0][1] >= pair[1][0]:
            cnt = cnt + 1

# second answer
print(cnt)