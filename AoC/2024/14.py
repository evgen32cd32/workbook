from math import inf, log2

boundries = [101,103]

with open('/Users/evgen/projects/workbook/data/advent2024/advent_14.txt','r') as f:
    ar = [0,0,0,0]
    robots = []
    r2 = []
    for l in f.readlines():
        px,py,vx,vy = [int(z) for x in l.split(' ') for z in x.split('=')[1].split(',')]
        robots.append((px,vx,py,vy))
        r2.append((py,vy))
        px = (px + 100*vx)%boundries[0]
        py = (py + 100*vy)%boundries[1]
        if px < boundries[0]//2 and py < boundries[1]//2:
            ar[0] += 1
        if px > boundries[0]//2 and py < boundries[1]//2:
            ar[1] += 1
        if px < boundries[0]//2 and py > boundries[1]//2:
            ar[2] += 1
        if px > boundries[0]//2 and py > boundries[1]//2:
            ar[3] += 1

#i = 0
#diff = inf
#ans2 = 0
#while True:
#    i += 1
#    robots = [((a+b)%boundries[0],b,(c+d)%boundries[0],d) for a,b,c,d in robots]
#    mid = [0,0]
#    for x,_,y,__ in robots:
#        mid[0] += x
#        mid[1] += y
#    mid[0] = mid[0]/len(robots)
#    mid[1] = mid[1]/len(robots)
#    td = sum([log2(abs(x-mid[0])+1)+log2(abs(y-mid[0])+1) for x,_,y,__ in robots])
#    if td < diff:
#        diff = td
#        ans2 = i
#        print(i,mid,diff)
#        if diff < 100:
#            break
#    if i == 1000000:
#        break
#
#
#with open('/Users/evgen/projects/workbook/data/advent2024/advent_14.txt','r') as f:
#    out = []
#    for _ in range(boundries[1]):
#        out.append(['.']*boundries[0])
#    robots = []
#    r2 = []
#    for l in f.readlines():
#        px,py,vx,vy = [int(z) for x in l.split(' ') for z in x.split('=')[1].split(',')]
#        px = (px + i*vx)%boundries[0]
#        py = (py + i*vy)%boundries[1]
#        out[py][px] = '*'

# first answer
print(ar[0]*ar[1]*ar[2]*ar[3])

i = 50
while True:
    cin = input()
    cb = 'q'
    out = []
    for _ in range(boundries[1]):
        out.append([' ']*boundries[0])
    if cin == cb:
        i -= 103
    else:
        i += 103
    #nr = []
    for a,b,c,d in robots:
        out[(c+i*d)%boundries[1]][(a+i*b)%boundries[0]] = '*'
    #robots = nr
    for y in range(boundries[1]):
        print(''.join(out[y]))
    print(i)

#just solve 50+103x = 95+101y in natural numbers

# second answer
#print(ans2)