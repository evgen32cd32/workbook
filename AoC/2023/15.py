with open('/Users/evgeny/python/workbook/data/advent2023/advent_15.txt','r') as f:
    ans = 0
    for cmd in f.readline().split(','):
        hsh = 0
        for c in cmd:
            hsh += ord(c)
            hsh *= 17
            hsh = hsh % 256
        #print(hsh)
        ans += hsh

# first answer
print(ans)



class Box:
    def __init__(self,hsh):
        self.ind = hsh
        self.d = {}
        self.itemslen = 0

with open('/Users/evgeny/python/workbook/data/advent2023/advent_15.txt','r') as f:
    boxes = {i:Box(i) for i in range(256)}
    for cmd in f.readline().split(','):
        hsh = 0
        rmfl = False
        if cmd[-1] == '-':
            rmfl = True
            lbl = cmd[:-1]
        else:
            lbl, focal = cmd.split('=')
            focal = int(focal)
        for c in lbl:
            hsh += ord(c)
            hsh *= 17
            hsh = hsh % 256
        if rmfl:
            if lbl in boxes[hsh].d:
                del boxes[hsh].d[lbl]
            continue
        if lbl in boxes[hsh].d:
            boxes[hsh].d[lbl] = (boxes[hsh].d[lbl][0],focal)
        else:
            boxes[hsh].d[lbl] = (boxes[hsh].itemslen,focal)
            boxes[hsh].itemslen += 1
    ans = 0
    for hsh, b in boxes.items():
        #print(b.d)
        for ind, ln in enumerate(sorted([x for x in b.d.values()])):
            ans += (hsh+1)*(ind+1)*ln[1]

# second answer
print(ans)