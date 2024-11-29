with open('/Users/evgeny/python/workbook/data/advent2022/advent_01.txt','r') as f:
    elfs = [0]
    for line in f.readlines():
        if line == '\n':
            elfs.append(0)
            continue
        elfs[-1] = elfs[-1] + int(line)

#print(elfs)

# first answer
print(max(elfs))

# second answer
print(sum(sorted(elfs,reverse=True)[:3]))