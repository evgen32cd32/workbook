from math import inf

def foo(add,maxpress):
    with open('/Users/evgen/projects/workbook/data/advent2024/advent_13.txt','r') as f:
        c = [3,1]
        x = [0,0]
        y = [0,0]
        ans = 0
        for i,line in enumerate(f.readlines()):
            if i%4 == 3:
                continue
            if i%4 == 0:
                x[0], y[0] = [int(ta.split('+')[1]) for ta in line.split(',')]
                continue
            if i%4 == 1:
                x[1], y[1] = [int(ta.split('+')[1]) for ta in line.split(',')]
                continue
            if i%4 == 2:
                X, Y = [int(ta.split('=')[1])+add for ta in line.split(',')]
                d = y[1]*x[0] - y[0]*x[1]
                if d == 0:
                    if X//x[0] != Y//y[0] or X%x[0] != Y%y[0]:
                        continue
                    li = 1
                    hi = 0
                    if x[0]/c[0] < x[1]/c[1]:
                        li = 0
                        hi = 1
                    for a in range(min(maxpress,X//x[li]),-1,-1):
                        b = (X - a*x[li])//x[hi]
                        if (X - a*x[li])%x[hi] == 0:
                            ans += c[li]*a + c[hi]*b
                            break
                else:
                    n = [y[1]*X-x[1]*Y,x[0]*Y-y[0]*X]
                    if n[0]%d == 0 and n[1]%d == 0:
                        ans += c[0]*n[0]//d + c[1]*n[1]//d
    return ans

# first answer
print(foo(0,100))

# second answer
print(foo(10000000000000,inf))