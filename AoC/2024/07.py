with open('/Users/evgen/projects/workbook/data/advent2024/advent_07.txt','r') as f:
    inp = f.readlines()
def foo(ops):
    ans1 = 0
    for line in inp:
        ar = line.split(':')
        res = int(ar[0])
        ar = [int(x) for x in ar[1].split()]
        for i in range(ops**(len(ar))):
            r = ar[0]
            for j in range(1,len(ar)):
                if (i//(ops**(j-1)))%ops == 0:
                    r *= ar[j]
                elif (i//(ops**(j-1)))%ops == 1:
                    r += ar[j]
                else:
                    r = int(str(r)+str(ar[j]))
                if r > res:
                    break
            if r == res:
                ans1 += res
                break
    return ans1

# first answer
print(foo(2))

# second answer
print(foo(3))