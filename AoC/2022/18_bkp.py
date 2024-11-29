cubes = {}
lava = []

minMaxCoord = [[1000000, 0] for _ in range(3)]

with open('/Users/evgeny/python/workbook/data/advent2022/advent_18.txt','r') as f:
    for line in f.readlines():
        lv = tuple(int(x) for x in line.split(','))
        lava.append(lv)
        cubes[lv] = 'l'
        for i in range(3):
            if lv[i] < minMaxCoord[i][0]:
                minMaxCoord[i][0] = lv[i]
            if lv[i] > minMaxCoord[i][1]:
                minMaxCoord[i][1] = lv[i]

print(minMaxCoord)

directions = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,-1],[0,0,1]]

def labelAir(coord):
    cubes[coord] = 'tmp'
    if    (coord[0] - 1 < minMaxCoord[0][0]) or (coord[0] + 1 > minMaxCoord[0][1]) \
       or (coord[1] - 1 < minMaxCoord[1][0]) or (coord[1] + 1 > minMaxCoord[1][1]) \
       or (coord[2] - 1 < minMaxCoord[2][0]) or (coord[2] + 1 > minMaxCoord[2][1]):
        cubes[coord] = 'o'
        return
    # x - 1
    for d in directions:
        nc = (coord[0] + d[0], coord[1] + d[1], coord[2] + d[2])
        if nc not in cubes:
            labelAir(nc)
        if cubes[nc] == 'o' or cubes[nc] == 'i':
            cubes[coord] = cubes[nc]
            return
    cubes[coord] = 'i'


firstAns = 0
secondAns = 0

for lv in lava:
    for d in directions:
        neighbor = (lv[0] + d[0], lv[1] + d[1], lv[2] + d[2])
        if neighbor not in cubes:
            labelAir(neighbor)
        if cubes[neighbor] == 'o':
            firstAns = firstAns + 1
            secondAns = secondAns + 1
        if cubes[neighbor] == 'i':
            firstAns = firstAns + 1
     
for k in cubes:
    if cubes[k] == 'tmp':
        print(k)

print(firstAns)
print(secondAns)

