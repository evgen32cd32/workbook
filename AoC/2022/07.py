from enum import Enum

class ObjType(Enum):
    File = 0
    Dir = 1

class GraphNode:
    def __init__(self, name, objType, parent, size=0):
        self.name = name
        self.objType = objType
        self.size = size
        self.parent = parent
        self.children = set()

dirArray = []

def calcTotalSize(node):
    global dirArray
    for child in node.children:
        if child.objType == ObjType.Dir:
            node.size = node.size + calcTotalSize(child)
    dirArray.append([node.size,node.name])
    return node.size

def printGraph(node, l=0):
    print('  '*l + node.name + ' ' + str(node.size))
    for child in node.children:
        printGraph(child, l+1)

with open('/Users/evgeny/python/workbook/data/advent2022/advent_07.txt','r') as f:
    root = GraphNode('/',ObjType.Dir,None)
    curDir = root
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        splitted = line.split()
        if splitted[0] == '$':
            if splitted[1] == 'cd':
                if splitted[2] == '/':
                    curDir = root
                elif splitted[2] == '..':
                    curDir = curDir.parent
                else:
                    curDir = [x for x in curDir.children if x.name == splitted[2]][0]
        else:
            if splitted[0] == 'dir':
                newNode = GraphNode(splitted[1],ObjType.Dir,curDir)
                curDir.children.add(newNode)
            else:
                newNode = GraphNode(splitted[1],ObjType.File,curDir,int(splitted[0]))
                curDir.children.add(newNode)
                curDir.size = curDir.size + newNode.size
calcTotalSize(root)
#printGraph(root)

dirArray.sort(key=lambda x : x[0])

firstAns = 0

spaceToFree = root.size - 40000000

ff = False
sf = False

for dir in dirArray:
    #print('{} {}'.format(dir[1],dir[0]))
    if dir[0] <= 100000:
        firstAns = firstAns + dir[0]
        ff = True
    if dir[0] >= spaceToFree and not sf:
        secondAns = dir[0]
        sf = True
    if ff and sf:
        break

# first answer
print(firstAns)

# second answer
print(secondAns)