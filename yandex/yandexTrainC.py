import sys;
import re;

inp = [];
for line in sys.stdin:
	inp.append(line);

inp = ['3','Moscow 2','XXXXXXXX.X.X.X.X.X.XXXXX Kvartal','XXXXXXXXX.X.X.X.X.X.XXXX Kvartet','Minsk 1','XX.XXXXX........XXXXXXXX Toloka','Berlin 2',
	'XX..XXXXXXXXXXXXXXXXXXXX Mitte','XXXXXXXXXXXXXXXX.....XXX Lustgarten','4','3 Moscow Minsk Berlin','2 Moscow Minsk','2 Minsk Berlin','2 Moscow Berlin'];



nc = int(inp[0]);

db = {}

off = 1;
for i in range(nc):
	s = inp[off].split();
	db[s[0]] = [set()];
	off += 1;
	for j in range(int(s[1])):
		s2 = inp[off+j].split();
		a = set([m.start() for m in re.finditer('\.',s2[0])]);
		db[s[0]][0].update(a);
		db[s[0]].append([s2[1],a]);
	off += int(s[1]);

nt = int(inp[off]);
off += 1;

for i in range(nt):
	s = inp[off + i].split()[1:];
	a = db[s[0]][0];
	for c in s[1:]:
		a = a.intersection(db[c][0]);
	if (len(a) == 0):
		print('No');
	else:
		for e in a:
			b = set([e]);
			break;
		a = b;
		roomlist = '';
		for c in s:
			b = set();
			j = 0;
			room = '';
			while (len(b) == 0):
				j += 1;
				b = a.intersection(db[c][j][1]);
				room = db[c][j][0];
			roomlist += ' ' + room;
		print('Yes' + roomlist);



print(db);
