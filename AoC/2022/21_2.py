monkeys = {}
getvd = {}

add = lambda x,y:x+y
subs = lambda x,y:x-y
multi = lambda x,y:x*y
div = lambda x,y:x//y

class Monkey:
    def __init__(self, name, value = None, m1 = None, m2 = None, op = None):
        self.name = name
        self.value = value
        self._m1 = m1
        self._m2 = m2
        self.op = op
    
    def getValue(self):
        if self.value is None:
            self.value = self.op(monkeys[self._m1].getValue(),monkeys[self._m2].getValue())
        return self.value
    
    def getMonkeyValue(self, name):
        if self.name == 'root':
            if name == self._m1:
                self.value = monkeys[self._m2].getValue()
            else:
                self.value = monkeys[self._m1].getValue()
            monkeys[name].value = self.value
            return self.value
        if self.value is None:
            monkeys[getvd[self.name]].getMonkeyValue(self.name)
        if name == self._m1:
            if self.op == subs:
                monkeys[name].value = self.value + monkeys[self._m2].getValue()
            if self.op == div:
                monkeys[name].value = self.value * monkeys[self._m2].getValue()
            other = self._m2
        else:
            if self.op == subs:
                monkeys[name].value = monkeys[self._m1].getValue() - self.value
            if self.op == div:
                monkeys[name].value = monkeys[self._m1].getValue() // self.value
            other = self._m1
        if self.op == add:
            monkeys[name].value = self.value - monkeys[other].getValue()
        if self.op == multi:
            monkeys[name].value = self.value // monkeys[other].getValue()
        return monkeys[name].value


with open('/Users/evgeny/python/workbook/data/advent2022/advent_21.txt','r') as f:
    for line in  f.readlines():
        splitted = line.split()
        name = splitted[0][:-1]
        if name == 'humn':
            monkeys[name] = Monkey(name)
            continue
        if splitted[1].isdigit():
            monkeys[name] = Monkey(name,int(splitted[1]))
        else:
            if splitted[2] == '+':
                op = add
            elif splitted[2] == '-':
                op = subs
            elif splitted[2] == '*':
                op = multi
            else:
                op = div
            monkeys[name] = Monkey(name,None,splitted[1],splitted[3],op)
            getvd[splitted[1]] = name
            getvd[splitted[3]] = name

#for k in getvd:
#    print('{} {}'.format(k,getvd[k]))

print(monkeys[getvd['humn']].getMonkeyValue('humn'))
    

