with open('/Users/evgeny/python/workbook/data/advent2023/advent_03.txt','r') as f:
    score = 0
    ar = []
    symbs = []
    for i,line in enumerate(f.readlines()):
        ar.append(list(line))
        if line[-1] != '\n':
            ar[-1].append('\n')
        for j,c in enumerate(line):
            if not c.isdigit() and c != '.' and c != '\n':
                symbs.append((i,j))
    #print(ar)
    for i,j in symbs:
        if i > 0 and j > 0 and ar[i-1][j-1].isdigit():
            a = j-1
            while a > 0 and ar[i-1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i-1]) and ar[i-1][a].isdigit():
                code = code*10 + int(ar[i-1][a])
                ar[i-1][a] = '.'
                a += 1
            score += code
        if i > 0 and ar[i-1][j].isdigit():
            a = j
            while a > 0 and ar[i-1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i-1]) and ar[i-1][a].isdigit():
                code = code*10 + int(ar[i-1][a])
                ar[i-1][a] = '.'
                a += 1
            score += code
        if i > 0 and j+1 < len(ar[i-1]) and ar[i-1][j+1].isdigit():
            a = j+1
            while a > 0 and ar[i-1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i-1]) and ar[i-1][a].isdigit():
                code = code*10 + int(ar[i-1][a])
                ar[i-1][a] = '.'
                a += 1
            score += code

        
        if j > 0 and ar[i][j-1].isdigit():
            a = j-1
            while a > 0 and ar[i][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i]) and ar[i][a].isdigit():
                code = code*10 + int(ar[i][a])
                ar[i][a] = '.'
                a += 1
            score += code
        if j+1 < len(ar[i]) and ar[i][j+1].isdigit():
            a = j+1
            code = 0
            while a < len(ar[i]) and ar[i][a].isdigit():
                code = code*10 + int(ar[i][a])
                ar[i][a] = '.'
                a += 1
            score += code
        

        if i+1 < len(ar) and j > 0 and ar[i+1][j-1].isdigit():
            a = j-1
            while a > 0 and ar[i+1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i+1]) and ar[i+1][a].isdigit():
                code = code*10 + int(ar[i+1][a])
                ar[i+1][a] = '.'
                a += 1
            score += code
        if i+1 < len(ar) and ar[i+1][j].isdigit():
            a = j
            while a > 0 and ar[i+1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i+1]) and ar[i+1][a].isdigit():
                code = code*10 + int(ar[i+1][a])
                ar[i+1][a] = '.'
                a += 1
            score += code
        if i+1 < len(ar) and j+1 < len(ar[i+1]) and ar[i+1][j+1].isdigit():
            a = j+1
            while a > 0 and ar[i+1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i+1]) and ar[i+1][a].isdigit():
                code = code*10 + int(ar[i+1][a])
                ar[i+1][a] = '.'
                a += 1
            score += code




# first answer
print(score)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_03.txt','r') as f:
    ans = 0
    ar = []
    symbs = []
    for i,line in enumerate(f.readlines()):
        ar.append(list(line))
        if line[-1] != '\n':
            ar[-1].append('\n')
        for j,c in enumerate(line):
            if c == '*':
                symbs.append((i,j))
    #print(ar)
    for i,j in symbs:
        score = []
        if i > 0 and j > 0 and ar[i-1][j-1].isdigit():
            a = j-1
            while a > 0 and ar[i-1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i-1]) and ar[i-1][a].isdigit():
                code = code*10 + int(ar[i-1][a])
                ar[i-1][a] = '.'
                a += 1
            score.append(code)
        if i > 0 and ar[i-1][j].isdigit():
            a = j
            while a > 0 and ar[i-1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i-1]) and ar[i-1][a].isdigit():
                code = code*10 + int(ar[i-1][a])
                ar[i-1][a] = '.'
                a += 1
            score.append(code)
        if i > 0 and j+1 < len(ar[i-1]) and ar[i-1][j+1].isdigit():
            a = j+1
            while a > 0 and ar[i-1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i-1]) and ar[i-1][a].isdigit():
                code = code*10 + int(ar[i-1][a])
                ar[i-1][a] = '.'
                a += 1
            score.append(code)

        
        if j > 0 and ar[i][j-1].isdigit():
            if len(score) > 1:
                continue
            a = j-1
            while a > 0 and ar[i][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i]) and ar[i][a].isdigit():
                code = code*10 + int(ar[i][a])
                ar[i][a] = '.'
                a += 1
            score.append(code)
        if j+1 < len(ar[i]) and ar[i][j+1].isdigit():
            if len(score) > 1:
                continue
            a = j+1
            code = 0
            while a < len(ar[i]) and ar[i][a].isdigit():
                code = code*10 + int(ar[i][a])
                ar[i][a] = '.'
                a += 1
            score.append(code)
        

        if i+1 < len(ar) and j > 0 and ar[i+1][j-1].isdigit():
            if len(score) > 1:
                continue
            a = j-1
            while a > 0 and ar[i+1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i+1]) and ar[i+1][a].isdigit():
                code = code*10 + int(ar[i+1][a])
                ar[i+1][a] = '.'
                a += 1
            score.append(code)
        if i+1 < len(ar) and ar[i+1][j].isdigit():
            if len(score) > 1:
                continue
            a = j
            while a > 0 and ar[i+1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i+1]) and ar[i+1][a].isdigit():
                code = code*10 + int(ar[i+1][a])
                ar[i+1][a] = '.'
                a += 1
            score.append(code)
        if i+1 < len(ar) and j+1 < len(ar[i+1]) and ar[i+1][j+1].isdigit():
            if len(score) > 1:
                continue
            a = j+1
            while a > 0 and ar[i+1][a-1].isdigit():
                a -= 1
            code = 0
            while a < len(ar[i+1]) and ar[i+1][a].isdigit():
                code = code*10 + int(ar[i+1][a])
                ar[i+1][a] = '.'
                a += 1
            score.append(code)
        if len(score) != 2:
            continue
        ans += score[0]*score[1]




# second answer
print(ans)