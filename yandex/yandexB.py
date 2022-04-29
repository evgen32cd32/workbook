import sys;

inp = [];
for line in sys.stdin:
	inp.append(line);




n = int(inp[0]);

cp = (0,0);
lp = [];
dist = 0;

for i in range(1,n+1):
	newp = tuple([int(x) for x in inp[i].split()]);
	dist += ((newp[0] - cp[0])**2 + (newp[1] - cp[1])**2)**0.5;
	i = len(lp);
	while i > 0:
		if (newp[1] < lp[i-1][1]):
			break;
		dist += ((newp[0] - lp[i-1][0])**2 + (newp[1] - lp[i-1][1])**2)**0.5;
		lp.pop();
		i -= 1;
	if (cp[1] > newp[1]):
		lp.append(cp);
	cp = newp;

print(dist);




inp = ['6','3 2','5 1','7 4','9 3','11 7','12 1'];