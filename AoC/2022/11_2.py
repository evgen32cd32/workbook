from collections import deque
from copy import deepcopy

class Item:
    def __init__(self, number):
        self.remainders = {}
        self.init_value = number
    
    def calcRemainders(self, divisors):
        for d in divisors:
            self.remainders[d] = self.init_value % d

    def __mul__(self, other):
        nother = deepcopy(self)
        for k in nother.remainders:
            if type(other) == int:
                nother.remainders[k] = (nother.remainders[k] * other) % k
            else:
                nother.remainders[k] = (nother.remainders[k] * other.remainders[k]) % k
        return nother

    def __add__(self, other):
        nother = deepcopy(self)
        for k in nother.remainders:
            if type(other) == int:
                nother.remainders[k] = (nother.remainders[k] + other) % k
            else:
                nother.remainders[k] = (nother.remainders[k] + other.remainders[k]) % k
        return nother
    
    def checkIfDivided(self, div):
        return self.remainders[div] == 0

def multiply(item, multiplier):
    return item * multiplier

def addition(item, addendum):
    return item + addendum

def square(item, _):
    return item * item

class Monkey:
    def __init__(self, items, operation, param, division, trueMonkey, falseMonkey):
        self.items = deque(items)
        self.operation = operation
        self.param = param
        self.division = division
        self.nextMonkey = {True : trueMonkey, False : falseMonkey}
        self.inspectCount = 0
    
    def inspectItems(self):
        items = []
        self.inspectCount = self.inspectCount + len(self.items)
        for _ in  range(len(self.items)):
            item = self.items.popleft()
            item = self.operation(item, self.param)
            #item = item//3
            items.append((self.nextMonkey[item.checkIfDivided(self.division)], item))
        return items
    
    def getItem(self, item):
        self.items.append(item)

with open('/Users/evgeny/python/workbook/data/advent2022/advent_11.txt','r') as f:
    monkeys = []
    lines = f.readlines()
    i = 0
    divisors = []
    while i < len(lines):
        items = [Item(int(x.replace(',',''))) for x in lines[i+1].split()[2:]]
        divisors.append(int(lines[i+3].split()[3]))
        trueMonkey = int(lines[i+4].split()[5])
        falseMonkey = int(lines[i+5].split()[5])

        operationList = lines[i+2].split()[3:]
        if operationList[2] == 'old':
            operation = square
            param = None
        else:
            param = int(operationList[2])
            if operationList[1] == '+':
                operation = addition
            else:
                operation = multiply
        monkeys.append(Monkey(items,operation,param,divisors[-1],trueMonkey,falseMonkey))
        i = i + 7
    for monkey in monkeys:
        for item in monkey.items:
            item.calcRemainders(divisors)
    
    for _ in range(10000):
        for monkey in monkeys:
            items = monkey.inspectItems()
            for item in items:
                monkeys[item[0]].getItem(item[1])
        #if _ % 1000 == 0:
        #    print(_)
        #    for i, monkey in enumerate(monkeys):
        #        print('{} {}'.format(i, monkey.inspectCount))

#for i, monkey in enumerate(monkeys):
#    print('{} {}'.format(i, monkey.inspectCount))

secondAns = sorted([x.inspectCount for x in monkeys],reverse=True)[:2]

# second answer
print(secondAns[0]*secondAns[1])