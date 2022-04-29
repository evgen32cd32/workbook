
inp = ['20',
'0.5 7.11',
'1.0 6.69',
'1.5 4.97',
'2.0 4.25',
'2.5 5.75',
'3.0 8.58',
'3.5 10.56',
'4.0 10.26',
'4.5 8.32',
'5.0 6.86',
'5.5 7.54',
'6.0 10.04',
'6.5 12.35',
'7.0 12.62',
'7.5 10.88',
'8.0 8.97',
'8.5 8.91',
'9.0 10.99',
'9.5 13.53',
'10.0 14.42'];


import sys;
import numpy as np;


inp = [];
for line in sys.stdin:
	inp.append(line);


n = int(inp[0]);


x = [];
y = [];


for i in range(1,n+1):
	s = inp[i].split();
	xi = float(s[0]);
	y.append(float(s[1]));
	x.append([np.tan(xi),np.power(np.cos(xi),2),np.power(np.sin(xi),2),np.sin(2*xi),np.sqrt(xi)]);



reg = np.linalg.lstsq(x,y,rcond=None);

res = reg[0];

a = '{:.2f}'.format(res[0]);
c = '{:.2f}'.format(res[1]**0.5);
b = '{:.2f}'.format(np.sign(res[3])*res[2]**0.5);
d = '{:.2f}'.format(res[4]);
print(str(a) + ' ' + str(b) + ' ' + str(c) + ' ' + str(d));

