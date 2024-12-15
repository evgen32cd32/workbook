with open('/Users/evgen/projects/workbook/data/advent2024/advent_15.txt','r') as f:
    mp = []
    cmds = ''
    fl = False
    for line in f.readlines():
        if line == '\n':
            fl = True
            continue
        if not fl:
            mp.append(line)
        if fl:
            cmds += line
    ar = {i+j*1j:c for i,l in enumerate(mp) for j,c in enumerate(l) if c in '.@O'}
    ar2 = {}
    for k,v in ar.items():
        ar2[k + 1j*k.imag] = '[' if v == 'O' else v
        nv = v
        if v == 'O':
            nv = ']'
        if v == '@':
            nv = '.'
        ar2[k + 1j*k.imag + 1j] = nv
    start = [k for k,v in ar.items() if v == '@'].pop()
    ar[start] = '.'
    directions = {'^':-1,'v':1,'<':-1j,'>':1j}
    cur = start
    for cmd in cmds:
        if cmd not in directions:
            continue
        way = directions[cmd]
        n = 0
        tmp = cur + way
        while tmp in ar and ar[tmp] == 'O':
            n += 1
            tmp += way
        if tmp in ar:
            cur += way
            if n > 0:
                ar[tmp] = 'O'
                ar[cur] = '.'
        #print(cmd)
        #out = []
        #for i in range(len(mp)):
        #    out.append(['#']*(len(mp[0])-1))
        #for k,v in ar.items():
        #    out[int(k.real)][int(k.imag)] = v
        #out[int(cur.real)][int(cur.imag)] = '@'
        #for l in out:
        #    print(''.join(l))

    start = [k for k,v in ar2.items() if v == '@'].pop()
    directions = {'^':-1,'v':1,'<':-1j,'>':1j}
    cur = start
    for cmd in cmds:
        if cmd not in directions:
            continue
        way = directions[cmd]
        if way.real == 0:
            tmp = cur + way
            while tmp in ar2 and ar2[tmp] != '.':
                tmp += way
            if tmp in ar2:
                while ar2[tmp] != '@':
                    ar2[tmp] = ar2[tmp - way]
                    tmp -= way
                ar2[tmp] = '.'
                cur += way
        else:
            to_check = [{cur+way}]
            new_check = set()
            fl = True
            while len(to_check[-1]) > 0: 
                for tmp in to_check[-1]:
                    if tmp not in ar2:
                        fl = False
                        break
                    if ar2[tmp] == ']':
                        new_check.update({tmp+way,tmp+way-1j})
                    if ar2[tmp] == '[':
                        new_check.update({tmp+way,tmp+way+1j})
                if not fl:
                    break
                to_check.append(new_check)
                new_check = set()
            if fl:
                for i in range(len(to_check)-2,-1,-1):
                    for tmp in to_check[i]:
                        ar2[tmp] = ar2[tmp-way]
                        ar2[tmp-way] = '.'
                cur += way
        #print(cmd)
        #out = []
        #for i in range(len(mp)):
        #    out.append(['#']*((len(mp[0])-1)*2))
        #for k,v in ar2.items():
        #    out[int(k.real)][int(k.imag)] = v
        #for l in out:
        #    print(''.join(l))

# first answer
print(sum([100*int(x.real) + int(x.imag) for x in ar if ar[x] == 'O']))

# second answer
print(sum([100*int(x.real) + int(x.imag) for x in ar2 if ar2[x] == '[']))