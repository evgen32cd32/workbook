import sys;


inp = ['4',
'1 0 0 1',
'1 1',
'1 1',
'0',
'0'];

inp = [];
for line in sys.stdin:
	inp.append(line);

ne = int(inp[0]);

ill = set();

for i in range(ne):
	if inp[1][2*i] == '1':
		ill.add(i);

meets = {};

for i in range(ne):
	s = inp[i+2].split();
	if (s[0] != '0'):
		for c in s[1:]:
			m = int(c);
			if (not m in meets):
				meets[m] = set();
			meets[m].add(i);


for m in sorted(meets):
	for e in meets[m]:
		if e in ill:
			ill.update(meets[m]);
			break;


ans = [];
for i in range(ne):
	if i in ill:
		ans.append('1');
	else:
		ans.append('0');

print(' '.join(ans));

