from collections import Counter, deque

with open('/Users/evgen/projects/workbook/data/advent2024/advent_22.txt','r') as f:
    secrets = [int(x) for x in f.readlines()]

seqs = Counter()

ans1 = 0
for x in secrets:
    seq = deque()
    seqx = Counter()
    for _ in range(2000):
        prev = x%10
        x = ((x<<6)^x)%16777216
        x = ((x>>5)^x)%16777216
        x = ((x<<11)^x)%16777216
        seq.append((x%10)-prev)
        if len(seq) == 4: 
            if tuple(seq) not in seqx:
                seqx[tuple(seq)] += x%10
            seq.popleft()
    ans1 += x
    seqs += seqx

# first answer
print(ans1)

# second answer
print(max([x for x in seqs.values()]))