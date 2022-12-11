from collections import deque

class Monkey:
    def __init__(self, items, operation, division, trueMonkey, falseMonkey):
        self.items = deque(items)
        self.operation = operation
        self.division = division
        self.nextMonkey = {True : trueMonkey, False : falseMonkey}
        self.inspectCount = 0
    
    def inspectItems(self):
        items = []
        self.inspectCount = self.inspectCount + len(self.items)
        for _ in  range(len(self.items)):
            old = self.items.popleft()
            item = eval(self.operation)//3
            items.append((self.nextMonkey[item % self.division == 0], item))
        return items
    
    def getItem(self, item):
        self.items.append(item)


with open('/Users/evgeny/python/workbook/data/advent2022/advent_11.txt','r') as f:
    monkeys = []
    lines = f.readlines()
    i = 0
    while i < len(lines):
        items = [int(x.replace(',','')) for x in lines[i+1].split()[2:]]
        operation = ' '.join(lines[i+2].split()[3:])
        division = int(lines[i+3].split()[3])
        trueMonkey = int(lines[i+4].split()[5])
        falseMonkey = int(lines[i+5].split()[5])
        monkeys.append(Monkey(items,operation,division,trueMonkey,falseMonkey))
        i = i + 7
    
    for _ in range(20):
        for monkey in monkeys:
            items = monkey.inspectItems()
            for item in items:
                monkeys[item[0]].getItem(item[1])

firstAns = sorted([x.inspectCount for x in monkeys],reverse=True)[:2]

# first answer
print(firstAns[0]*firstAns[1])