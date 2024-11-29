from collections import deque
from copy import deepcopy

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]

class BigNumber:
    def __init__(self, number):
        self.decompose(number)

    def decompose(self,number):
        self.number = {}
        for p in primeNumbers:
            self.number[p] = 0
            while number % p == 0:
                self.number[p] = self.number[p] + 1
                number = number // p
        self.number[0] = number
    
    def compose(self):
        number = 1
        for p in primeNumbers:
            number = number * p**self.number[p]
        return number * self.number[0]

    def __mul__(self, other):
        if type(other) == int:
            nother = BigNumber(other)
        else:
            nother = deepcopy(other)
        for p in primeNumbers:
            nother.number[p] = nother.number[p] + self.number[p]
        nother.number[0] = nother.number[0] * self.number[0]
        return nother

    def __add__(self, other):
        if type(other) == int:
            return BigNumber(self.compose() + other)
        else:
            return BigNumber(self.compose() + other.compose())
    
    def checkIfDivided(self, div):
        return self.number[div] > 0

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

with open('/Users/evgeny/python/workbook/data/advent2022/advent_11_test.txt','r') as f:
    monkeys = []
    lines = f.readlines()
    i = 0
    while i < len(lines):
        items = [BigNumber(int(x.replace(',',''))) for x in lines[i+1].split()[2:]]
        division = int(lines[i+3].split()[3])
        trueMonkey = int(lines[i+4].split()[5])
        falseMonkey = int(lines[i+5].split()[5])

        operationList = lines[i+2].split()[3:]
        if operationList[2] == 'old':
            operation = square
            param = None
        else:
            param = BigNumber(int(operationList[2]))
            if operationList[1] == '+':
                operation = addition
            else:
                operation = multiply
        monkeys.append(Monkey(items,operation,param,division,trueMonkey,falseMonkey))
        i = i + 7
    
    for _ in range(1000):
        for monkey in monkeys:
            items = monkey.inspectItems()
            for item in items:
                monkeys[item[0]].getItem(item[1])
        if _ % 10 == 0:
            print(_)
            for i, monkey in enumerate(monkeys):
                print('{} {}'.format(i, monkey.inspectCount))

for i, monkey in enumerate(monkeys):
    print('{} {}'.format(i, monkey.inspectCount))

secondAns = sorted([x.inspectCount for x in monkeys],reverse=True)[:2]

# second answer
print(secondAns[0]*secondAns[1])