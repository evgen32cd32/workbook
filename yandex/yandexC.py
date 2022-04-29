import sys;
import numpy as np;


inp = [3,1,2,3,1,1];



inp = [];
for line in sys.stdin:
	inp.append(int(line));



y = inp[1:];

ey = np.mean(y);
my = np.median(y);

print(ey);
print(my);
print(my);

