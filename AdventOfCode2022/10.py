class CPUCRT:
    def __init__(self):
        self.cycle = 0
        self.checkpoint = 20
        self.x = 1
        self.screen = [['.'] * 40 for _ in range(6)]
        self.firstAns = 0
    
    def process(self):
        layer = int(self.cycle/40)
        pos = self.cycle - layer * 40
        if abs(self.x - pos) < 2:
            self.screen[layer][pos] = '#'
        self.cycle = self.cycle + 1
        if self.cycle == self.checkpoint:
            self.firstAns = self.firstAns + self.x * self.checkpoint
            self.checkpoint = self.checkpoint +40

with open('/Users/evgeny/python/workbook/data/advent2022/advent_10.txt','r') as f:
    dev = CPUCRT()
    for line in f.readlines():
        splitted = line.split()
        dev.process()
        if splitted[0] == 'addx':
            dev.process()
            dev.x = dev.x + int(splitted[1])
        

# first answer
print(dev.firstAns)

# second answer
for l in dev.screen:
    print(''.join(l))