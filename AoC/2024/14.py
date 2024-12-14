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

# first answer
print(ar[0]*ar[1]*ar[2]*ar[3])