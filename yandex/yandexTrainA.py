import numpy as np;

rng = np.random.default_rng();

def generate1():
	a = rng.uniform(0,1);
	b = rng.uniform(0,1);
	return (a*np.cos(2*np.pi*b),a*np.sin(2*np.pi*b));

def generate2():
	while True:
		x = rng.uniform(-1,1);
		y = rng.uniform(-1,1);
		if x**2 + y**2 > 1:
			continue;
		return (x,y);


import sys;


def tester(line):
	ls = line.split();
	ex2 = 0;
	ex = 0;
	ey2 = 0;
	ey = 0;
	n = len(ls)//2;
	for i in range(n):
		ex += float(ls[2*i]);
		ex2 += float(ls[2*i])**2;
		ey += float(ls[2*i+1]);
		ey2 += float(ls[2*i+1])**2;
	vx = 12*(ex2/n - (ex/n)**2 - 1./6.);
	vy = 12*(ey2/n - (ey/n)**2 - 1./6.);
	if vx*vx + vy*vy >= 0.25:
		return 2;
	else:
		return 1;


for line in sys.stdin:
	print(tester(line));




err = 0;
for i in range(100):
	s1 = '';
	s2 = '';
	for i in range(1000):
		a,b = generate1();
		s1 += ' ' + str(a) + ' ' + str(b);
		a,b = generate2();
		s2 += ' ' + str(a) + ' ' + str(b);
	if tester(s1) == 2:
		err +=1;
	if tester(s2) == 1:
		err +=1;

print(err);







