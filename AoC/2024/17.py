with open('/Users/evgen/projects/workbook/data/advent2024/advent_17.txt','r') as f:
    inp = f.readlines()
    regA = int(inp[0].split(':')[1])
    regB = int(inp[1].split(':')[1])
    regC = int(inp[2].split(':')[1])

    cmds = [int(x) for x in inp[4].split(':')[1].split(',')]

def combo(x):
    if x < 4:
        return x
    if x == 4:
        return regA
    if x == 5:
        return regB
    if x == 6:
        return regC
    assert()

ans1 = []
i = 0
#it = 0
#Program: 2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0
while i < len(cmds)-1:
    #it += 1
    cmd = cmds[i]
    op = cmds[i+1]
    if cmd == 0:
        regA = regA >> combo(op)
    if cmd == 1:
        regB = regB ^ op
    if cmd == 2:
        regB = combo(op) % 8
    if cmd == 3:
        if regA != 0:
            i = op
            #print(it,(cmd,op),regA,regB,regC)
            continue
    if cmd == 4:
        regB = regB ^ regC
    if cmd == 5:
        ans1.append(str(combo(op)%8))
    if cmd == 6:
        regB = regA >> combo(op)
    if cmd == 7:
        regC = regA >> combo(op)
    i += 2
    #print(it,(cmd,op),regA,regB,regC)

ans2 = [0]
for cmd in reversed(cmds):
    ans2 = [x*8+a for x in ans2 for a in range(8) if ((a^4)^((x*8+a)>>(a^1)))%8 == cmd]

# first answer
print(','.join(ans1))

# second answer
print(ans2[0])