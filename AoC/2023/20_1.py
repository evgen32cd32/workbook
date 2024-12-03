from collections import deque

deq = deque()

class Flipflop:
    def __init__(self, name):
        self.type = 'ff'
        self.name = name
        self.children = []
        self.status = False
    
    def signal(self, high, source=None):
        #print(f'{source} -{high}> {self.name}')
        if high:
            return
        self.status = not self.status
        deq.extend([(ch, self.status, self.name) for ch in self.children])

class Conjunction:
    def __init__(self, name):
        self.type = 'con'
        self.name = name
        self.children = []
        self.ar = {}
    
    def signal(self, high, source):
        #print(f'{source} -{high}> {self.name}')
        self.ar[source] = high
        deq.extend([(ch, not all(self.ar.values()), self.name) for ch in self.children])

class Broadcast:
    def __init__(self, name='broadcaster'):
        self.type = 'br'
        self.name = name
        self.children = []
    
    def signal(self, high, source):
        #print(f'{source} -{high}> {self.name}')
        deq.extend([(ch, high, self.name) for ch in self.children])

class Button:
    def __init__(self, name = 'button'):
        self.type = 'bt'
        self.name = name
        self.broadcast = None
    
    def signal(self, high, source):
        deq.append((self.broadcast, False, self.name))

class Dummy:
    def __init__(self, name):
        self.type = 'dm'
        self.name = name

    def signal(self, high, source):
        #print(f'{source} -{high}> {self.name}')
        pass


with open('/Users/evgen/projects/workbook/data/advent2023/advent_20.txt','r') as f:
    d = {}
    for line in f.readlines():
        mod, children = line.split(' -> ')
        if children[-1] == '\n':
            children = children[:-1]
        childar = children.split(', ')
        if mod[0] == '%':
            name = mod[1:]
            d[name] = (Flipflop(name),childar)
        elif mod[0] == '&':
            name = mod[1:]
            d[name] = (Conjunction(name),childar)
        else:
            name = mod
            d[name] = (Broadcast(name),childar)
    for k,v in d.items():
        for x in v[1]:
            if x in d:
                v[0].children.append(d[x][0])
                if d[x][0].type == 'con':
                    d[x][0].ar[k] = False
            else:
                v[0].children.append(Dummy(x))
    button = Button()
    button.broadcast = d['broadcaster'][0]
    counter = {True:0,False:0}
    for _ in range(1000):
        deq.append((button,None, None))
        while len(deq) > 0:
            mod, high, source = deq.popleft()
            if high is not None:
                counter[high] += 1
            #print(counter[True],counter[False])
            mod.signal(high, source)
        #print(counter[True],counter[False])
        
# first answer
print(counter[True]*counter[False])

# second answer
#print(task(4,10))