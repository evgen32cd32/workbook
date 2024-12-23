graph = {}

with open('/Users/evgen/projects/workbook/data/advent2024/advent_23.txt','r') as f:
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        a,b = line.split('-')
        if a not in graph:
            graph[a] = set()
        if b not in graph:
            graph[b] = set()
        graph[a].add(b)
        graph[b].add(a)

ans1 = set()

maxnet = 2
ans2 = None

visited = {a}
to_visit = {a}
new_visit = set()
while len(to_visit) > 0:
    for node in to_visit:
        if node[0] == 't':
            for nb in graph[node]:
                for x in graph[node] & graph[nb]:
                    ans1.add(tuple(sorted([node,nb,x])))
        for nb in graph[node]:
            inter = graph[node] & graph[nb]
            if len(inter) > maxnet-2:
                ar = [node,nb]
                while len(inter) > 0:
                    new = next(iter(inter))
                    ar.append(new)
                    inter = inter & graph[new]
                if len(ar) > maxnet:
                    ans2 = sorted(ar)
                    maxnet = len(ar)
            if nb not in visited:
                visited.add(nb)
                new_visit.add(nb)
    to_visit = new_visit
    new_visit = set()

# first answer
print(len(ans1))

# second answer
print(','.join(ans2))