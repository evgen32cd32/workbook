import sys;
from collections import Counter;


inp = [];
for line in sys.stdin:
	inp.append(line);

inp = ['1 2 1 2 2 2','2'];

dice = Counter([int(x) for x in inp[0].split()]);

if (len(dice) == 1):
	for d in dice:
		print(d);

ex = 0;
for d in dice:
	ex += d*dice[d];

ex = ex/6;

k = int(inp[1]);

coef = {};
for d in dice:
	coef[d] = [0,6-dice[d]];


for i in range(2,k):
	for d in dice:
		s = 0;
		for d2 in dice:
			if d == d2:
				continue;
			s += coef[d2][i-1];
		coef[d].append(s);

e1 = ex;
for i in range(2,k+1):
	p = 0;
	for d in dice:
		p += coef[d][i-1];
	p = p/(6**i);
	e1 = p*i*ex + (1-p)*e1;

print(e1);



