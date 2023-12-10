
with open('/Users/evgeny/python/workbook/data/advent2023/advent_10.txt','r') as f:
    pipes = []
    mp = []
    ist = -1
    for i,line in enumerate(f.readlines()):
        if line[-1] == '\n':
            line = line[:-1]
        pipes.append(line)
        mp.append([-1]*len(line))
        if ist == -1:
            jst = line.find('S')
            if jst > -1:
                ist = i
    mp[ist][jst] = 0
    cur = []
    if ist > 0 and pipes[ist-1][jst] in ('|','F','7'):
        cur.append((ist-1,jst))
    if ist < len(pipes)-1 and pipes[ist+1][jst] in ('|','L','J'):
        cur.append((ist+1,jst))
    if jst > 0 and pipes[ist][jst-1] in ('-','L','F'):
        cur.append((ist,jst-1))
    if jst < len(pipes[0])-1 and pipes[ist][jst+1] in ('-','7','J'):
        cur.append((ist,jst+1))
    i = 1
    while cur[0] != cur[1]:
        mp[cur[0][0]][cur[0][1]] = i
        mp[cur[1][0]][cur[1][1]] = i
        for j in range(2):
            if pipes[cur[j][0]][cur[j][1]] == '|':
                if cur[j][0] > 0 and mp[cur[j][0]-1][cur[j][1]] == -1:
                    cur[j] = (cur[j][0]-1,cur[j][1])
                else:
                    cur[j] = (cur[j][0]+1,cur[j][1])
            elif pipes[cur[j][0]][cur[j][1]] == '-':
                if cur[j][1] > 0 and mp[cur[j][0]][cur[j][1]-1] == -1:
                    cur[j] = (cur[j][0],cur[j][1]-1)
                else:
                    cur[j] = (cur[j][0],cur[j][1]+1)
            elif pipes[cur[j][0]][cur[j][1]] == 'L':
                if cur[j][0] > 0 and mp[cur[j][0]-1][cur[j][1]] == -1:
                    cur[j] = (cur[j][0]-1,cur[j][1])
                else:
                    cur[j] = (cur[j][0],cur[j][1]+1)
            elif pipes[cur[j][0]][cur[j][1]] == 'J':
                if cur[j][0] > 0 and mp[cur[j][0]-1][cur[j][1]] == -1:
                    cur[j] = (cur[j][0]-1,cur[j][1])
                else:
                    cur[j] = (cur[j][0],cur[j][1]-1)
            elif pipes[cur[j][0]][cur[j][1]] == '7':
                if cur[j][1] > 0 and mp[cur[j][0]][cur[j][1]-1] == -1:
                    cur[j] = (cur[j][0],cur[j][1]-1)
                else:
                    cur[j] = (cur[j][0]+1,cur[j][1])
            elif pipes[cur[j][0]][cur[j][1]] == 'F':
                if cur[j][0] < len(pipes)-1 and mp[cur[j][0]+1][cur[j][1]] == -1:
                    cur[j] = (cur[j][0]+1,cur[j][1])
                else:
                    cur[j] = (cur[j][0],cur[j][1]+1)
        i += 1
mp[cur[0][0]][cur[0][1]] = i
pipelength = 2*i

# first answer
print(i)


cur = (ist,jst)
if i > 0 and mp[cur[0]-1][cur[1]] == 1:
    cur = (ist-1,jst)
    direction = 'u'
elif j > 0 and mp[cur[0]][cur[1]-1] == 1:
    cur = (ist,jst-1)
    direction = 'l'
else:
    cur = (ist+1,jst)
    direction = 'd'

guessed = True
ar = []
while True:
    if direction == 'u':
        if cur[1] < len(mp[0])-1: 
            if mp[cur[0]][cur[1]+1] == -1:
                ar.append((cur[0],cur[1]+1))
                mp[ar[-1][0]][ar[-1][1]] = 0
        else:
            guessed = False
        if pipes[cur[0]][cur[1]] == '|':
            cur = (cur[0]-1,cur[1])
        elif pipes[cur[0]][cur[1]] == 'F':
            cur = (cur[0],cur[1]+1)
            direction = 'r'
        elif pipes[cur[0]][cur[1]] == '7':
            if cur[0] > 0: 
                if mp[cur[0]-1][cur[1]] == -1:
                    ar.append((cur[0]-1,cur[1]))
                    mp[ar[-1][0]][ar[-1][1]] = 0
            else:
                guessed = False
            cur = (cur[0],cur[1]-1)
            direction = 'l'
    elif direction == 'd': 
        if cur[1] > 0:
            if mp[cur[0]][cur[1]-1] == -1:
                ar.append((cur[0],cur[1]-1))
                mp[ar[-1][0]][ar[-1][1]] = 0
        else:
            guessed = False
        if pipes[cur[0]][cur[1]] == '|':
            cur = (cur[0]+1,cur[1])
        elif pipes[cur[0]][cur[1]] == 'L':
            if cur[0] < len(mp)-1:
                if mp[cur[0]+1][cur[1]] == -1:
                    ar.append((cur[0]+1,cur[1]))
                    mp[ar[-1][0]][ar[-1][1]] = 0
            else:
                guessed = False
            cur = (cur[0],cur[1]+1)
            direction = 'r'
        elif pipes[cur[0]][cur[1]] == 'J':
            cur = (cur[0],cur[1]-1)
            direction = 'l'
    elif direction == 'r':
        if cur[0] < len(mp)-1:
            if mp[cur[0]+1][cur[1]] == -1:
                ar.append((cur[0]+1,cur[1]))
                mp[ar[-1][0]][ar[-1][1]] = 0
        else:
            guessed = False
        if pipes[cur[0]][cur[1]] == '-':
            cur = (cur[0],cur[1]+1)
        elif pipes[cur[0]][cur[1]] == 'J':
            if cur[1] < len(mp[0])-1: 
                if mp[cur[0]][cur[1]+1] == -1:
                    ar.append((cur[0],cur[1]+1))
                    mp[ar[-1][0]][ar[-1][1]] = 0
            else:
                guessed = False
            cur = (cur[0]-1,cur[1])
            direction = 'u'
        elif pipes[cur[0]][cur[1]] == '7':
            cur = (cur[0]+1,cur[1])
            direction = 'd'
    elif direction == 'l':
        if cur[0] > 0: 
            if mp[cur[0]-1][cur[1]] == -1:
                ar.append((cur[0]-1,cur[1]))
                mp[ar[-1][0]][ar[-1][1]] = 0
        else:
            guessed = False
        if pipes[cur[0]][cur[1]] == '-':
            cur = (cur[0],cur[1]-1)
        elif pipes[cur[0]][cur[1]] == 'L':
            cur = (cur[0]-1,cur[1])
            direction = 'u'
        elif pipes[cur[0]][cur[1]] == 'F':
            if cur[1] > 0:
                if mp[cur[0]][cur[1]-1] == -1:
                    ar.append((cur[0],cur[1]-1))
                    mp[ar[-1][0]][ar[-1][1]] = 0
            else:
                guessed = False
            cur = (cur[0]+1,cur[1])
            direction = 'd'

    if mp[cur[0]][cur[1]] == 0:
        break

while len(ar) > 0:
    i, j = ar.pop()
    if i == 0 or i == len(mp)-1 or j == 0 or j == len(mp[0])-1:
        guessed = False
    if i > 0 and mp[i-1][j] == -1:
        mp[i-1][j] = 0
        ar.append((i-1,j))
    if i < len(mp)-1 and mp[i+1][j] == -1:
        mp[i+1][j] = 0
        ar.append((i+1,j))
    if j > 0 and mp[i][j-1] == -1:
        mp[i][j-1] = 0
        ar.append((i,j-1))
    if j < len(mp[0])-1 and mp[i][j+1] == -1:
        mp[i][j+1] = 0
        ar.append((i,j+1))

sq = -sum([x for line in mp for x in line if x == -1])
if guessed:
    sq = len(mp)*len(mp[0])-sq-pipelength

# second answer
print(sq)
#print(len(mp)*len(mp[0])-sq-pipelength)

#print(guessed)

#pretty = []
#for i in range(len(mp)):
#    a = ''
#    for j in range(len(mp[0])):
#        if mp[i][j] == 0:
#            a += '.'
#        elif mp[i][j] == -1:
#            a+='x'
#        elif pipes[i][j] == '-':
#            a+='═'
#        elif pipes[i][j] == '|':
#            a+='║'
#        elif pipes[i][j] == 'F':
#            a+='╔'
#        elif pipes[i][j] == '7':
#            a+='╗'
#        elif pipes[i][j] == 'L':
#            a+='╚'
#        elif pipes[i][j] == 'J':
#            a+='╝'
#    pretty.append(a)
#
#for x in pretty:
#    print(x)


