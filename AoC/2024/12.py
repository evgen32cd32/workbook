with open('/Users/evgen/projects/workbook/data/advent2024/advent_12.txt','r') as f:
    ar = {i+1j*j:c for i,l in enumerate(f.readlines()) for j,c in enumerate(l) if c != '\n'}

directions = [1j,-1,-1j,1]

ar1 = ar.copy()
regions = []

def rec(ch,k):
    if k in ar1 and ar1[k] == ch:
        del ar1[k]
        return {k} | {x for dr in directions for x in rec(ch,k+dr)}
    return set()

class Region:
    def __init__(self,let,art):
        self.let = let
        self.ar = art
        self.per = sum([1 for x in art for dr in directions if x+dr not in ar or ar[x+dr] != let])

        self.sides = 0

        re = sorted({x.real for x in self.ar})
        im = sorted({x.imag*1j for x in self.ar},key=lambda y: y.imag)
        def lookthrough(iar,jar,i1):
            for i in iar:
                tsf = False
                lsf = False
                for j in jar:
                    cur = i+j
                    if tsf:
                        if cur not in art or (cur-i1) in art:
                            tsf = False
                    else:
                        if cur in art and (cur-i1) not in art:
                            tsf = True
                            self.sides += 1
                    if lsf:
                        if cur not in art or (cur+i1) in art:
                            lsf = False
                    else:
                        if cur in art and (cur+i1) not in art:
                            lsf = True
                            self.sides += 1
        lookthrough(re,im,1)
        lookthrough(im,re,1j)


while len(ar1) > 0:
    sq,let = next(iter(ar1.items()))
    regions.append(Region(let,rec(let,sq)))

# first answer
print(sum([reg.per*len(reg.ar) for reg in regions]))

# second answer
print(sum([reg.sides*len(reg.ar) for reg in regions]))