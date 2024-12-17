from random import choice

class Node:
    def __init__(self,id):
        self.id = id
        self.edges = set()

class Edge:
    def __init__(self,id,nodes=None):
        self.id = id
        self.nodes = nodes
    
    def contruction(self):
        it = iter(self.nodes)
        n1 = next(it)
        n2 = next(it)
        # n2 -> n1
        trm = {self.id}
        n1.edges.remove(self)
        n2.edges.remove(self)
        for e in n2.edges:
            if n1 in e.nodes:
                n1.edges.remove(e)
                trm.add(e.id)
                continue
            e.nodes.remove(n2)
            e.nodes.add(n1)
            n1.edges.add(e)
        return n2.id,trm

d = {}
nodes = []
edges = []
with open('/Users/evgen/projects/workbook/data/advent2023/advent_25.txt','r') as f:
    for line in f.readlines():
        a, ar = line.split(': ')
        ar = ar.split(' ')
        if a not in d:
            d[a] = len(nodes)
            nodes.append(Node(d[a]))
        for x in ar:
            if x[-1] == '\n':
                x = x[:-1]
            if x not in d:
                d[x] = len(nodes)
                nodes.append(Node(d[x]))
            edges.append(Edge(len(edges),{nodes[d[a]],nodes[d[x]]}))
            nodes[d[a]].edges.add(edges[-1])
            nodes[d[x]].edges.add(edges[-1])

tnodes = [Node(i) for i in range(len(nodes))]
tedges = [Edge(i) for i in range(len(edges))]

def initialize():
    for i in range(len(nodes)):
        tnodes[i].edges = {tedges[e.id] for e in nodes[i].edges}
    for i in range(len(edges)):
        tedges[i].nodes = {tnodes[n.id] for n in edges[i].nodes}
    return tnodes.copy(), tedges.copy()

ear = []
#i = 0
while len(ear) != 3:
    #i += 1
    #if i%100 == 0:
    #    print(i,len(ear))
    nar, ear = initialize()
    while len(nar) > 2:
        nid,etr = choice(ear).contruction()
        nar = [x for x in nar if x.id != nid]
        ear = [x for x in ear if x.id not in etr]

st = [n.id for n in ear[0].nodes]
rmv = {e.id for e in ear}
vis = [set(),set()]
for i in range(2):
    to_visit = {st[i]}
    new_visit = set()
    while len(to_visit) > 0:
        for j in to_visit:
            vis[i].add(j)
            new_visit.update([n.id for e in nodes[j].edges for n in e.nodes if n.id not in vis[i] and e.id not in rmv])
        to_visit = new_visit
        new_visit = set()

# first answer
print(len(vis[0])*len(vis[1]))