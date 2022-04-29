import numpy as np;
import pandas as pd;
import itertools as it;
import statsmodels.api as sm;
import matplotlib.pyplot as plt;
import sklearn.model_selection as ms;
import sklearn.linear_model as lm;


# (a)
rng = np.random.default_rng();

x = rng.standard_normal(100);
eps = rng.standard_normal(100);


# (b)
y = 5 + 3 * x -2 * np.power(x,2) + np.power(x,3) + eps;

# (c)
df = pd.DataFrame({'y':y});
df['dummy'] = 1;
for i in range(1,11):
	df['x'+str(i)] = np.power(x,i);

cols = df.columns.tolist()[2:];

bestcols = {};
for i in range(1,11):
	rss = np.Inf;
	for subcols in it.combinations(cols,i):
		rssc = np.linalg.lstsq(df[['dummy']+list(subcols)],df.y,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			bestcols[i] = list(subcols);

res = pd.DataFrame();
for k in bestcols:
	r = sm.OLS(df.y,df[['dummy'] + bestcols[k]]).fit();
	res.loc[k,'cols'] = ','.join(bestcols[k]);
	res.loc[k,'rss'] = r.ssr;
	res.loc[k,'aic'] = r.aic;
	res.loc[k,'bic'] = r.bic;
	res.loc[k,'r2adj'] = r.rsquared_adj;

fig, ax = plt.subplots(2,2);
ax[0,0].plot(res.index,res['rss']);
ax[0,0].set_title('rss');
ax[1,0].plot(res.index,res['aic']);
ax[1,0].set_title('aic');
ax[0,1].plot(res.index,res['bic']);
ax[0,1].set_title('bic');
ax[1,1].plot(res.index,res['r2adj']);
ax[1,1].set_title('r2adj');
plt.show();


# (d)
# forward
bestcols = {};
bc = [];
cs = list(cols);
for i in range(1,11):
	rss = np.Inf;
	for c in cs:
		rssc = np.linalg.lstsq(df[['dummy']+list(bc) + [c]],df.y,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			bestcols[i] = list(list(bc) + [c]);
	cs.remove(bestcols[i][-1]);
	bc = bestcols[i];

res = pd.DataFrame();
for k in bestcols:
	r = sm.OLS(df.y,df[['dummy'] + bestcols[k]]).fit();
	res.loc[k,'cols'] = ','.join(bestcols[k]);
	res.loc[k,'rss'] = r.ssr;
	res.loc[k,'aic'] = r.aic;
	res.loc[k,'bic'] = r.bic;
	res.loc[k,'r2adj'] = r.rsquared_adj;

fig, ax = plt.subplots(2,2);
ax[0,0].plot(res.index,res['rss']);
ax[0,0].set_title('rss');
ax[1,0].plot(res.index,res['aic']);
ax[1,0].set_title('aic');
ax[0,1].plot(res.index,res['bic']);
ax[0,1].set_title('bic');
ax[1,1].plot(res.index,res['r2adj']);
ax[1,1].set_title('r2adj');
plt.show();

# backward
bestcols = {};
cs = list(cols);
bestcols[10] = list(cols);
for i in range(9,0,-1):
	rss = np.Inf;
	for subcols in it.combinations(cs,len(cs)-1):
		rssc = np.linalg.lstsq(df[['dummy']+list(subcols)],df.y,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			bestcols[i] = list(subcols);
	cs = list(bestcols[i]);

res = pd.DataFrame();
for k in bestcols:
	r = sm.OLS(df.y,df[['dummy'] + bestcols[k]]).fit();
	res.loc[k,'cols'] = ','.join(bestcols[k]);
	res.loc[k,'rss'] = r.ssr;
	res.loc[k,'aic'] = r.aic;
	res.loc[k,'bic'] = r.bic;
	res.loc[k,'r2adj'] = r.rsquared_adj;

fig, ax = plt.subplots(2,2);
ax[0,0].plot(res.index,res['rss']);
ax[0,0].set_title('rss');
ax[1,0].plot(res.index,res['aic']);
ax[1,0].set_title('aic');
ax[0,1].plot(res.index,res['bic']);
ax[0,1].set_title('bic');
ax[1,1].plot(res.index,res['r2adj']);
ax[1,1].set_title('r2adj');
plt.show();


# (e)
df_norm = df.copy();
df_norm[cols] = (df_norm[cols] - df_norm[cols].mean())/df_norm[cols].std();

lbd = np.power(10,np.linspace(-3,1,num=100));
reg = lm.LassoCV(alphas = lbd, cv = 10,max_iter = np.power(10,8));
reg.fit(df_norm[cols],df.y);

mse = pd.DataFrame(reg.mse_path_, index = reg.alphas_).transpose().mean();

plt.plot(mse);
plt.xscale('log');
plt.show();


# (f)
y = 2 + np.power(x,7) + eps;

df = pd.DataFrame({'y':y});
df['dummy'] = 1;
for i in range(1,11):
	df['x'+str(i)] = np.power(x,i);

cols = df.columns.tolist()[2:];

bestcols = {};
for i in range(1,11):
	rss = np.Inf;
	for subcols in it.combinations(cols,i):
		rssc = np.linalg.lstsq(df[['dummy']+list(subcols)],df.y,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			bestcols[i] = list(subcols);

res = pd.DataFrame();
for k in bestcols:
	r = sm.OLS(df.y,df[['dummy'] + bestcols[k]]).fit();
	res.loc[k,'cols'] = ','.join(bestcols[k]);
	res.loc[k,'rss'] = r.ssr;
	res.loc[k,'aic'] = r.aic;
	res.loc[k,'bic'] = r.bic;
	res.loc[k,'r2adj'] = r.rsquared_adj;

fig, ax = plt.subplots(2,2);
ax[0,0].plot(res.index,res['rss']);
ax[0,0].set_title('rss');
ax[1,0].plot(res.index,res['aic']);
ax[1,0].set_title('aic');
ax[0,1].plot(res.index,res['bic']);
ax[0,1].set_title('bic');
ax[1,1].plot(res.index,res['r2adj']);
ax[1,1].set_title('r2adj');
plt.show();

df_norm = df.copy();
df_norm[cols] = (df_norm[cols] - df_norm[cols].mean())/df_norm[cols].std();

lbd = np.power(10,np.linspace(-5,5,num=100));
reg = lm.LassoCV(alphas = lbd, cv = 10,max_iter = np.power(10,8));
reg.fit(df_norm[cols],df.y);

mse = pd.DataFrame(reg.mse_path_, index = reg.alphas_).transpose().mean();

plt.plot(mse);
plt.xscale('log');
plt.show();


