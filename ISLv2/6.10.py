import numpy as np;
import pandas as pd;
import itertools as it;
import sklearn.linear_model as lm;

import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import sklearn.model_selection as ms;
import sklearn.linear_model as lm;
import itertools as it;
import sklearn.decomposition as skld;
import sklearn.cross_decomposition as cd;
import statsmodels.multivariate.pca as smpca;


# (a)
rng = np.random.default_rng();
df = pd.DataFrame();

for i in range(1,21):
	df['x'+str(i)] = rng.normal(-1 + 2 * rng.random(),0.5 + 1.5 * rng.random(),1000);

eps = rng.standard_normal(1000);
b = rng.integers(-5,6,20);

df['y'] = df.dot(b) + eps;
df['dummy'] = 1;


# (b)
train = df.sample(frac = 0.1);
test = df.loc[~df.index.isin(train.index)];


# (c)
cols = train.columns.tolist()[:-2];
res = pd.DataFrame();
k = 0;
cp = 0;
for i in range(0,len(cols) + 1):
	rss = np.Inf;
	for subcols in it.combinations(cols,i):
		k += 1;
		rssc = np.linalg.lstsq(train[['dummy']+list(subcols)],train.y,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			res.loc[i,'cols'] = ','.join(subcols);
			res.loc[i,'rss'] = rss;
		cpn = np.floor(k*1000/np.power(2,len(cols)))/10;
		if cpn > cp:
			cp = cpn;
			print(cp);

plt.plot(res.index,res.rss);
plt.show();


# (d)
reg = lm.LinearRegression();
for i in range(0,len(cols) + 1):
	if i == 0:
		res.loc[i,'test_rss'] = np.mean(np.power(test.y.mean() - test.y,2));
		continue;
	res.loc[i,'reg'] = reg.fit(train[res.loc[i,'cols'].split(',')],train.y);
	pre = res.loc[i,'reg'].predict(test[res.loc[i,'cols'].split(',')]).transpose()[0];
	res.loc[i,'test_rss'] = np.mean(np.power(pre - test.y,2));

plt.plot(res.index,res.test_rss);
plt.show();


# (g)
beta = pd.DataFrame({'true':b}, index = df.columns.tolist()[:-2]);

f = pd.DataFrame();
for i in range(0,len(cols) + 1):
	beta[str(i)] = 0;
	if i == 0:
		f.loc[i,'l'] = np.sqrt(np.sum(np.power(beta.true - beta[str(i)],2)));
		continue;
	cs = res.loc[i,'cols'].split(',');
	for k in range(len(cs)):
		beta.loc[cs[k],str(i)] = res.loc[i,'reg'].coef_[k];
	f.loc[i,'l'] = np.sqrt(np.sum(np.power(beta.true - beta[str(i)],2)));

plt.plot(f.index,f.l);
plt.show();






