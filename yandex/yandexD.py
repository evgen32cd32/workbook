

def rd(a):
	return np.sin(a);


def rd(a):
	if a < 0.5:
		return 0;
	else:
		return 0.5;



def diff(y,i,h):
	return (y[i+1] - y[i-1])/(2*h);




def rd(a):
	print(a,flush=True);
	return float(input());




n = 30000;

h = 1./(n+1);


y = [0,0];
x = [-h,0];

for i in range(1,n+1):
	y.append(rd(i*h));
	x.append(i*h);

y.append(1);
y.append(1);

x.append(1);
x.append(1+h);


ans = 0;

for i in range(1,len(y)-2):
	#ans += h * (y[i]*diff(y,i,h) + y[i+1]*diff(y,i+1,h))/2;
	#ans += (y[i+2]*y[i+1] - y[i]*y[i-1])/4;
	ans += (x[i]*(y[i+1]-y[i]) + x[i+1]*(y[i+2]-y[i+1]))/2;


print(ans);
