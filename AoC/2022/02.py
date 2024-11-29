# 0 A X Rock
# 1 B Y Paper
# 2 C Z Scissors

with open('/Users/evgeny/python/workbook/data/advent2022/advent_02.txt','r') as f:
    score = 0
    for line in f.readlines():
        opp,me = [ord(x) for x in line.split()]
        opp = opp - ord('A')
        me = me - ord('X')
        score = score + me + 1
        res = me - opp
        if res == 0:
            score = score + 3
        if res == 1 or res == -2:
            score = score + 6

# first answer
print(score)


# 0 A Rock
# 1 B Paper
# 2 C Scissors

# -1 X Lose
# 0 Y Draw
# 1 Z Win

with open('/Users/evgeny/python/workbook/data/advent2022/advent_02.txt','r') as f:
    score = 0
    for line in f.readlines():
        opp,res = [ord(x) for x in line.split()]
        opp = opp - ord('A')
        res = res - ord('Y')
        score = score + (res + 1) * 3
        me = opp + res
        if me == 3:
            me = 0
        if me == -1:
            me = 2
        score = score + me + 1

# second answer
print(score)