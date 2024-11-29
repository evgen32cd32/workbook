class SNAFU:
    def __init__(self, str):
        self.value = str
    
    def __int__(self):
        num = 0
        for ch in self.value:
            a = 0
            if ch.isdigit():
                a = int(ch)
            elif ch == '-':
                a = -1
            elif ch == '=':
                a = -2
            else:
                continue
            num = num*5 + a
        return num



sum = 0
with open('/Users/evgeny/python/workbook/data/advent2022/advent_25.txt','r') as f:
    for line in f.readlines():
        sum += int(SNAFU(line[:-1]))

print(sum)
firstAns = ''
while sum > 0:
    s = sum % 5
    if s < 3:
        firstAns = str(s) + firstAns
        sum = sum // 5
        continue
    if s == 4:
        firstAns = '-' + firstAns
    if  s == 3:
        firstAns = '=' + firstAns
    sum = (sum // 5) + 1

print(firstAns)
