with open('/Users/evgeny/python/workbook/data/advent2022/advent_03.txt','r') as f:
    score = 0
    for line in f.readlines():
        cnt = int((len(line)-1)/2)
        a = set(line[:cnt])
        b = set(line[cnt:-1])
        item = a.intersection(b).pop()
        sc = ord(item) - ord('a') + 1
        if sc < 0:
            sc = ord(item) - ord('A') + 27
        score = score + sc

# first answer
print(score)


with open('/Users/evgeny/python/workbook/data/advent2022/advent_03.txt','r') as f:
    score = 0
    i = 0
    group = []
    for line in f.readlines():
        i = i + 1
        group.append(set(line[:-1]))
        if i == 3:
            item = group[0].intersection(group[1]).intersection(group[2]).pop()
            sc = ord(item) - ord('a') + 1
            if sc < 0:
                sc = ord(item) - ord('A') + 27
            score = score + sc
            i = 0
            group = [] 
print(score)

