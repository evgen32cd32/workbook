from functools import cmp_to_key

def parseLine(line):
    return recursiveParse(line)[0][0]

def recursiveParse(line):
    lst = []
    obj = None
    i = 0
    while i < len(line):
        if line[i] == ']':
            break
        if line[i].isdigit():
            if obj is None:
                obj = int(line[i])
            else:
                obj = obj * 10 + int(line[i])
        elif line[i] == ',':
            lst.append(obj)
            obj = None
        elif line[i] == '[':
            obj, j = recursiveParse(line[i+1:])
            i = i + j + 1
        i = i + 1
    if obj is not None:
        lst.append(obj)
    return tuple(lst), i

def recursiveComparer(left, right):
    for i in range(min([len(left),len(right)])):
        l = left[i]
        r = right[i]
        if type(l) == int:
            if type(r) == int:
                if l < r:
                    return 1
                if l > r:
                    return -1
            else:
                res = recursiveComparer([l],r)
                if res != 0:
                    return res
        else:
            if type(r) == int:
                res = recursiveComparer(l,[r])
                if res != 0:
                    return res
            else:
                res = recursiveComparer(l,r)
                if res != 0:
                    return res
    if len(left) < len(right):
        return 1
    if len(right) < len(left):
        return -1
    return 0

with open('/Users/evgeny/python/workbook/data/advent2022/advent_13.txt','r') as f:
    lines = f.readlines()
    i = 0
    pi = 1
    firstAns = 0
    a = ((2),)
    b = ((6),)
    packetList = [a,b]
    while i < len(lines):
        left = parseLine(lines[i])
        right = parseLine(lines[i+1])
        if recursiveComparer(left,right) == 1:
            firstAns = firstAns + pi
        packetList.append(left)
        packetList.append(right)
        i = i + 3
        pi = pi + 1

packetList.sort(key=cmp_to_key(recursiveComparer), reverse= True)
secondAns = (packetList.index(a)+1) * (packetList.index(b)+1)

# first answer
print(firstAns)

# second answer
print(secondAns)