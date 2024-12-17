import re
from random import randrange, sample, random

class Hail:
    def __init__(self,x,y,z,vx,vy,vz):
        self.p = [x,y,z]
        self.v = [vx,vy,vz]

with open('/Users/evgen/projects/workbook/data/advent2023/advent_24.txt','r') as f:
    hails = [Hail(*(int(x) for x in re.split(', |@ ',l))) for l in f.readlines()]

#bounds = [7,27]
bounds = [200000000000000,400000000000000]
ans1 = 0

for i in range(len(hails)-1):
    for j in range(i+1,len(hails)):
        h1 = hails[i]
        h2 = hails[j]
        if h1 == h2:
            continue
        d = h1.v[0]*h2.v[1] - h2.v[0]*h1.v[1]
        if d != 0:
            x = ((h1.p[1]-h2.p[1])*h1.v[0]*h2.v[0] - h1.p[0]*h2.v[0]*h1.v[1] + h2.p[0]*h1.v[0]*h2.v[1])/d
            y = ((h2.p[0]-h1.p[0])*h1.v[1]*h2.v[1] - h2.p[1]*h2.v[0]*h1.v[1] + h1.p[1]*h1.v[0]*h2.v[1])/d
            #print(f'{h1.p} @ {h1.v}')
            #print(f'{h2.p} @ {h2.v}')
            #print(x,y,'\n')
            if x >= bounds[0] and x <= bounds[1] and y >= bounds[0] and y <= bounds[1] and (x-h1.p[0])*h1.v[0] >= 0 and (x-h2.p[0])*h2.v[0] >= 0:
                ans1 += 1

hn = len(hails)

#h0 = Hail(sum([x.p[0] for x in hails])//hn,sum([x.p[1] for x in hails])//hn,sum([x.p[2] for x in hails])//hn,0,0,0)
#t = [0]*hn
#g = 1
#tol = 0.00001
#df = {(i,j):(h0.p[i] - hails[j].p[i] + t[j]*(h0.v[i] - hails[j].v[i])) for i in range(3) for j in range(hn)}
#f = sum([x*x for x in df.values()])
#it = 0
#while f > tol:
#    it += 1
#    dfdx = [2*sum([df[(i,j)] for j in range(hn)]) for i in range(3)]
#    dfdv = [2*sum([df[(i,j)]*t[j] for j in range(hn)]) for i in range(3)]
#    dfdt = [2*sum([(h0.v[i]-hails[j].v[i])*df[(i,j)] for i in range(3)]) for j in range(hn)]
#    fn = f*10
#    while fn >= f:
#        dx = [-x/g for x in dfdx]
#        dv = [-x/g for x in dfdv]
#        dt = [-x/g for x in dfdt]
#        h0.p = [h0.p[i]+dx[i] for i in range(3)]
#        h0.v = [h0.v[i]+dv[i] for i in range(3)]
#        t = [t[j]+dt[j] for j in range(hn)]
#        df = {(i,j):(h0.p[i] - hails[j].p[i] + t[j]*(h0.v[i] - hails[j].v[i])) for i in range(3) for j in range(hn)}
#        fn = sum([x*x for x in df.values()])
#        if fn > f:
#            g = g*10
#            h0.p = [h0.p[i]-dx[i] for i in range(3)]
#            h0.v = [h0.v[i]-dv[i] for i in range(3)]
#            t = [t[j]-dt[j] for j in range(hn)]
#        if fn == f:
#            g = g//10
#    f = fn
#    if it%10000 == 0:
#        print(it,h0.p,h0.v,t,f)
#    pass

def calcf(h):
    h0 = Hail(*[round(x) for x in h.p+h.v])
    df = {(i,j):(hails[j].v[i]*h0.p[0] - h0.v[i]*h0.p[0] + hails[j].p[0]*h0.v[i] - hails[j].p[0]*hails[j].v[i] + \
                 h0.v[0]*h0.p[i] - hails[j].v[0]*h0.p[i] - hails[j].p[i]*h0.v[0] + hails[j].v[0]*hails[j].p[i]) for i in range(1,3) for j in range(hn)}
    return sum([x*x for x in df.values()])

maxp = max([x.p[i] for x in hails for i in range(3)])
maxv = max([abs(x.v[i]) for x in hails for i in range(3)])
har = [Hail(randrange(maxp),randrange(maxp),randrange(maxp),randrange(maxv),randrange(maxv),randrange(maxv)) for _ in range(60)]
inds = set(i for i in range(60))
cr = 0.9
fr = 0.8
tol = 0.00001
#it = 0
f = calcf(har[0])
while f > tol:
    #it += 1
    for i in range(len(har)):
        h0 = har[i]
        fx = calcf(har[0])
        ha,hb,hc = [har[x] for x in sample(list(inds.difference({i})),3)]
        r = randrange(6)
        y = [0]*6
        for j in range(6):
            if j == r or random() < cr:
                if j < 3:
                    y[j] = ha.p[j] +fr*(hb.p[j]-hc.p[j])
                else:
                    y[j] = ha.v[j-3] +fr*(hb.v[j-3]-hc.v[j-3])
            else:
                y[j] = h0.p[j] if j < 3 else h0.v[j-3]
        hy = Hail(*y)
        fy = calcf(hy)
        if fy <= fx:
            har[i] = hy
        f = min([f,fx,fy])
    #if it%1000 == 0:
    #    print(it,h0.p,h0.v,f)

# first answer
print(ans1)

# second answer
for h in har:
    if calcf(h) < tol:
        print(sum([round(x) for x in h.p]))
        #print(it,h.p,h.v,f)
        break