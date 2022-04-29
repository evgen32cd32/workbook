
def foo(a:dict)->dict:
	tmp = dict(a);
	tmp['z'] = 99;
	return tmp;

a = {1:'a',2:'b',3:'c'};

b = foo(a);


n = 1000;
k = 60;
p = 0;
for i in range(k):
	p += math.comb(n,i) * np.power(0.03,i) * np.power(.97,n-i);





def groupbysum(A,B):
	d = {};
	for i in ranhe(len(B)):
		if not B[i] in d:
			d[B[i]] = 0;
		d[B[i]] += A[i];
	return d;