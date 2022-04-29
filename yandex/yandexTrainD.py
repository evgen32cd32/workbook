import sys;
from collections import deque;

n k 
a1 a2 a3 ak

5 3
1 2 5 4 3

n = 6;
k = 1;
s = '6 2 3 1 2 3';

s = '';
n = 0;
k = 0;
i = 0;
for line in sys.stdin:
	if (i == 0):
		c = line.split();
		n = int(c[0]);
		k = int(c[1]);
	else:
		s = line;
	i += 1;

queue = deque();
d = {};
ans = 0;
sm = 0;
missing = set();

for i in range(1,n+1):
	d[i] = 0;
	if i <= k:
		missing.add(i);

for c in s.split():
	a = int(c);
	if (len(queue) == 0 and a > k):
		continue;
	queue.append(a);
	sm += a;
	#print(a);
	#print(d);
	#print(queue);
	if (len(queue) > 1 and queue[0] == a):
		sm -= queue[0];
		queue.popleft();
		while(d[queue[0]] > 1 or queue[0] > k):
			d[queue[0]] -= 1;
			sm -= queue.popleft();
	else:
		d[a] += 1;
	missing.discard(a);
	if (len(missing) == 0):
		if (ans == 0 or ans > sm):
			ans = sm;
		missing.add(queue[0]);
		d[queue[0]] -= 1;
		sm -= queue.popleft();
		if (len(queue) > 0):
			while(d[queue[0]] > 1 or queue[0] > k):
				d[queue[0]] -= 1;
				sm -= queue.popleft();

print(ans);
