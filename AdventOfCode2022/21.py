monkeys = {}

class Monkey:
    def __init__(self, name, value = None, m1 = None, m2 = None, operation = None):
        self.name = name
        self.value = value
        self._m1 = m1
        self._m2 = m2
        self._o = operation
    
    def getValue(self):
        if self.value is None:
            self.value = self._o(monkeys[self._m1].getValue(),monkeys[self._m2].getValue())
        return self.value

with open('/Users/evgeny/python/workbook/data/advent2022/advent_21_test.txt','r') as f:
    for line in  f.readlines():
        splitted = line.split()
        name = splitted[0][:-1]
        if splitted[1].isdigit():
            monkeys[name] = Monkey(name,int(splitted[1]))
        else:
            if splitted[2] == '+':
                op = lambda x,y:x+y
            elif splitted[2] == '-':
                op = lambda x,y:x-y
            elif splitted[2] == '*':
                op = lambda x,y:x*y
            else:
                op = lambda x,y:x//y
            monkeys[name] = Monkey(name,None,splitted[1],splitted[3],op)

print(monkeys['root'].getValue())

#for k in monkeys:
#    print('{} {}'.format(k, monkeys[k].getValue()))
