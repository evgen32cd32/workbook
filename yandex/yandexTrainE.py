import sys;
import numpy as np;

rng = np.random.default_rng();

inp = [];
for i in range(1000):
	x1 = rng.uniform(-1,1);
	x2 = rng.uniform(-1,1);
	x3 = rng.uniform(-1,1);
	x4 = rng.uniform(-1,1);
	x5 = rng.uniform(-1,1);
	f = x1**2 + 2*x2**2 - 3*x3**2 + x4**2 + 2*x5**2 \
		- 2*x1*x2 + 3*x1*x3 - 4*x1*x4 - x1*x5 + 2*x2*x3 \
		+ x2*x4 - x2*x5 + 3*x3*x4 - 5*x3*x5 + 2*x4*x5 \
		+ 3*x1 - 3*x2 + 5*x3 + x4 - 2*x5 + 3;
	inp.append(str(x1) + '\t' + str(x2) + '\t' + str(x3) + '\t' + str(x4) + '\t' + str(x5) + '\t' + str(f));


x = [];
y = [];
xpred = [];
for line in sys.stdin:
	s = line.split();
	if (len(s) == 6):
		y.append(float(s[-1]));
	xi = [float(s[0])**2,float(s[1])**2,float(s[2])**2,float(s[3])**2,float(s[4])**2,
		float(s[0])*float(s[1]),float(s[0])*float(s[2]),float(s[0])*float(s[3]),float(s[0])*float(s[4]),
		float(s[1])*float(s[2]),float(s[1])*float(s[3]),float(s[1])*float(s[4]),float(s[2])*float(s[3]),
		float(s[2])*float(s[4]),float(s[3])*float(s[4]),float(s[0]),float(s[1]),float(s[2]),float(s[3]),float(s[4]),1];
	if (len(s) == 6):
		x.append(xi);
	else:
		xpred.append(xi);

reg = np.linalg.lstsq(x,y,rcond=None);

for i in np.dot(xpred,reg[0]):
	print(i);

