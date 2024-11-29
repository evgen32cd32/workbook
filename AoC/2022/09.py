from decimal import Decimal, ROUND_HALF_UP

def moveTail(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    if abs(dx) < 2 and abs(dy) < 2:
        return tail
    tail[0] = tail[0] + int(Decimal(dx/2).to_integral_value(rounding=ROUND_HALF_UP))
    tail[1] = tail[1] + int(Decimal(dy/2).to_integral_value(rounding=ROUND_HALF_UP))
    return tail

with open('/Users/evgeny/python/workbook/data/advent2022/advent_09.txt','r') as f:
    rope = [[0,0] for _ in range(10)]
    trail1 = set()
    trail9 = set()
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        direction, steps = line.split()
        for _ in range(int(steps)):
            if direction == 'U':
                rope[0][1] = rope[0][1] + 1
            elif direction == 'D':
                rope[0][1] = rope[0][1] - 1
            elif direction == 'L':
                rope[0][0] = rope[0][0] - 1
            elif direction == 'R':
                rope[0][0] = rope[0][0] + 1
            for i in range(9):
                rope[i+1] = moveTail(rope[i],rope[i+1])
            trail1.add(tuple(rope[1]))
            trail9.add(tuple(rope[9]))
            #print('{} {}'.format(head,tail))

# first answer
print(len(trail1))

# second answer
print(len(trail9))

#out = []
#for i in range(21):
#    out.append(['.']*27)
#
#for x in trail9:
#    if x == 0:
#        x = (0,0)
#    out[x[1]+5][x[0]+11] = '#'
#
#for i in range(len(out)):
#    print(''.join(out[-1-i]))
#
#print(trail1)