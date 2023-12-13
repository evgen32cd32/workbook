with open('/Users/evgeny/python/workbook/data/advent2023/advent_13.txt','r') as f:
    ans = 0
    ars = []
    ar = []
    for line in f.readlines():
        if line == '\n':
            ars.append(ar)
            ar = []
        else:
            if line[-1] == '\n':
                line = line[:-1]
            ar.append(line)
    ars.append(ar)
    for ar in ars:
        for i in range (1,len(ar)):
            found = True
            for a,b in zip(ar[i:],reversed(ar[:i])):
                if a != b:
                    found = False
                    break
            if not found:
                continue
            ans += 100*i
            #print(i)
            #for j,x in enumerate(ar):
            #    if j == i:
            #        print('-'*len(x))
            #    print(x)
            break
        if not found:
            for i in range(1,len(ar[0])):
                found = True
                for x in ar:
                    for a, b in zip(x[i:],reversed(x[:i])):
                        if a != b:
                            found = False
                            break
                    if not found:
                        break
                if not found:
                    continue
                ans += i
                #print(100*i)
                #for x in ar:
                #    print(x[:i]+'|'+x[i:])
                break

# first answer
print(ans)

with open('/Users/evgeny/python/workbook/data/advent2023/advent_13.txt','r') as f:
    ans = 0
    ars = []
    ar = []
    for line in f.readlines():
        if line == '\n':
            ars.append(ar)
            ar = []
        else:
            if line[-1] == '\n':
                line = line[:-1]
            ar.append(line)
    ars.append(ar)
    for ar in ars:
        for i in range (1,len(ar)):
            diff = 0
            for a,b in zip((c for x in ar[i:] for c in x),(c for x in reversed(ar[:i]) for c in x)):
                if a != b:
                    diff += 1
                    if diff > 1:
                        break
            if diff != 1:
                continue
            ans += 100*i
            #print(i)
            #for j,x in enumerate(ar):
            #    if j == i:
            #        print('-'*len(x))
            #    print(x)
            break
        if diff != 1:
            for i in range(1,len(ar[0])):
                diff = 0
                for x in ar:
                    for a, b in zip(x[i:],reversed(x[:i])):
                        if a != b:
                            diff += 1
                            if diff > 1:
                                break
                    if diff > 1:
                        break
                if diff != 1:
                    continue
                ans += i
                #print(100*i)
                #for x in ar:
                #    print(x[:i]+'|'+x[i:])
                break

# second answer
print(ans)