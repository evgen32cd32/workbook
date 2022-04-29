import numpy as np;
import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import sklearn.model_selection as ms;
import sklearn.linear_model as lm;
import itertools as it;
import sklearn.decomposition as skld;
import sklearn.cross_decomposition as cd;
import statsmodels.multivariate.pca as smpca;

hitters = pd.read_csv('~/Downloads/datasets/Hitters.csv');
hitters = hitters.dropna();

hitters["dummy"] = 1;

hitters["League_int"] = 0;
hitters.loc[hitters.League == 'N', "League_int"] = 1;
hitters["Division_int"] = 0;
hitters.loc[hitters.Division == 'W', "Division_int"] = 1;
hitters["NewLeague_int"] = 0;
hitters.loc[hitters.NewLeague == 'N', "NewLeague_int"] = 1;

cols = hitters.columns.tolist();
cols.remove('Salary');
cols.remove('League');
cols.remove('Division');
cols.remove('NewLeague');
cols.remove('dummy');

#best

b0 = hitters.Salary.mean();
curp = 0;

results = [[0, [], [[b0],[np.power((hitters.Salary - b0).std(),2)]]]];
for i in range(1,np.power(2,len(cols))):
	subcols = ['dummy'];	
	for j in range(len(cols)):
		if i & 1 << j != 0:
			subcols.append(cols[j]);
	#print(bin(i));
	#print(subcols);
	#results.append([len(subcols),subcols,smf.ols(formula='Salary ~ ' + ' + '.join(subcols),data=hitters).fit()]);
	results.append([len(subcols)-1,subcols,np.linalg.lstsq(hitters[subcols],hitters.Salary,rcond=None)[:2]]);
	newp = np.floor(100*i/np.power(2,len(cols)));
	if newp > curp:
		curp = newp;
		print(curp);

best = {};

for i in range(len(results)):
	if (not results[i][0] in best) or results[best[results[i][0]]][2][1][0] > results[i][2][1][0]:
		best[results[i][0]] = i;

for i in range(2,10):
	print(results[best[i]][1]);

fres = {};
for k in best:
	if k == 0:
		continue;
	fres[k] = smf.ols(formula='Salary ~ ' + ' + '.join(results[best[k]][1]) + ' -1', data = hitters).fit();

ar = [];
for k in fres:
	ar.append([k,fres[k].ssr,fres[k].aic,fres[k].bic,fres[k].rsquared_adj]);
ar = np.array(ar);
df = pd.DataFrame(ar,columns = ['k','rss','aic','bic','r2adj']);

fig, ax = plt.subplots(2,2);
ax[0,0].plot(df.k,df['rss']);
ax[0,0].set_title('rss');
ax[1,0].plot(df.k,df['aic']);
ax[1,0].set_title('aic');
ax[0,1].plot(df.k,df['bic']);
ax[0,1].set_title('bic');
ax[1,1].plot(df.k,df['r2adj']);
ax[1,1].set_title('r2adj');
plt.show();

print(df.loc[df.aic==df.aic.min(),'k']);
print(df.loc[df.bic==df.bic.min(),'k']);
print(df.loc[df.r2adj==df.r2adj.max(),'k']);

#forward

forward = {};
cl = cols.copy();
subcols = ['dummy'];
for i in range(1,len(cols)+1):
	rss = np.Inf;
	for c in cl:
		rssc = np.linalg.lstsq(hitters[subcols + [c]],hitters.Salary,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			newc = c;
	cl.remove(newc);
	subcols = subcols + [newc];
	forward[i] = subcols.copy();


#backward

backward = {};
cl = cols.copy();
subcols = ['dummy'] + cl;
for i in range(len(cols),0,-1):
	rss = np.Inf;
	for c in cl:
		newcols = subcols.copy();
		newcols.remove(c);
		rssc = np.linalg.lstsq(hitters[newcols],hitters.Salary,rcond=None)[1][0];
		if rssc < rss:
			rss = rssc;
			newc = c;
	cl.remove(newc);
	subcols.remove(newc);
	print(str(i) + ' ' + str(subcols));
	backward[i] = subcols.copy();


#Validation set

train = hitters.sample(frac=0.5);
test = hitters[~hitters.index.isin(train.index)];

curp = 0;
results = [];
for i in range(1,np.power(2,len(cols))):
	subcols = ['dummy'];
	for j in range(len(cols)):
		if i & 1 << j != 0:
			subcols.append(cols[j]);
	results.append([len(subcols)-1,subcols,np.linalg.lstsq(train[subcols],train.Salary,rcond=None)[:2]]);
	newp = np.floor(100*i/np.power(2,len(cols)));
	if newp > curp:
		curp = newp;
		print(curp);

best = {};

for i in range(len(results)):
	if (not results[i][0] in best) or results[best[results[i][0]]][2][1][0] > results[i][2][1][0]:
		best[results[i][0]] = i;

fres = {};
for k in best:
	fres[k] = smf.ols(formula='Salary ~ ' + ' + '.join(results[best[k]][1]) + ' -1', data = train).fit();

pred = {}
for k in fres:
	pred[k] = pd.DataFrame(fres[k].predict(test), columns = ['pred']);
	pred[k]['true'] = test.Salary;

rss = {}
for k in pred:
	rss[k] = np.sum(np.power(pred[k].true - pred[k].pred,2));

df = pd.DataFrame(rss,index=['rss']).transpose();
df.loc[df.rss == df.rss.min()];

trainparams = fres[5].params;
rss = np.Inf;
for subcols in it.combinations(cols,5):
	rssc = np.linalg.lstsq(hitters[['dummy']+list(subcols)],hitters.Salary,rcond=None)[1][0];
	if rssc < rss:
		rss = rssc;
		newc = list(subcols);

result = smf.ols(formula='Salary ~ ' + ' + '.join(newc), data = hitters).fit();
print(result.params);
print(trainparams);

#CV

pc = 0;
curp = 0;
mod = [];
kf = ms.KFold(n_splits=10, shuffle = True);
for traini,testi in kf.split(hitters):
	mod.append({});
	train = hitters.iloc[traini];
	test = hitters.iloc[testi];
	for i in range(1,len(cols)+1):
		rss = np.Inf;
		for subcols in it.combinations(cols,i):
			pc += 1;
			newp = np.floor(10*pc/np.power(2,len(cols)));
			if newp > curp:
				curp = newp;
				print(curp);
			rssc = np.linalg.lstsq(hitters[['dummy']+list(subcols)],hitters.Salary,rcond=None)[1][0];
			if rssc < rss:
				rss = rssc;
				newc = list(subcols);
		pred = smf.ols(formula='Salary ~ ' + ' + '.join(newc),data=train).fit().predict(test);
		mod[-1][i] = np.sum(np.power(pred - test.Salary,2));

res = {};
for k in mod[0]:
	res[k] = [];
	for i in range(len(mod)):
		res[k].append(mod[i][k]);

df = pd.DataFrame(res);

rss = np.Inf;
for subcols in it.combinations(cols,9):
	rssc = np.linalg.lstsq(hitters[['dummy']+list(subcols)],hitters.Salary,rcond=None)[1][0];
	if rssc < rss:
		rss = rssc;
		newc = list(subcols);

result = smf.ols(formula='Salary ~ ' + ' + '.join(newc), data = hitters).fit();
print(result.params);

# ridge regression

hitters_stand = hitters.copy();
hitters_stand[cols] = hitters_stand[cols]/hitters_stand[cols].std();
hitters_norm = hitters_stand.copy();
hitters_norm[cols] = hitters_norm[cols] - hitters_norm[cols].mean();

df = {};
reg = sm.OLS(hitters.Salary,hitters[['dummy'] + cols]);
df['sm'] = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.full(20,np.power(10,i));
	lbd[0] = 0;
	df['sm'].loc[i,'lambda'] = np.power(10,i);
	df['sm'].loc[i,'reg'] = reg.fit_regularized(alpha = lbd, L1_wt = 0);

reg = sm.OLS(hitters_stand.Salary,hitters_stand[['dummy'] + cols]);
df['sm_stand'] = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.full(20,np.power(10,i));
	lbd[0] = 0;
	df['sm_stand'].loc[i,'lambda'] = np.power(10,i);
	df['sm_stand'].loc[i,'reg'] = reg.fit_regularized(alpha = lbd, L1_wt = 0);

reg = sm.OLS(hitters_norm.Salary,hitters_norm[['dummy'] + cols]);
df['sm_norm'] = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.full(20,np.power(10,i));
	lbd[0] = 0;
	df['sm_norm'].loc[i,'lambda'] = np.power(10,i);
	df['sm_norm'].loc[i,'reg'] = reg.fit_regularized(alpha = lbd, L1_wt = 0);

df['skl'] = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.power(10,i);
	reg = lm.Ridge(alpha = lbd);
	df['skl'].loc[i,'lambda'] = lbd;
	df['skl'].loc[i,'reg'] = reg.fit(hitters[cols],hitters.Salary);

df['skl_stand'] = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.power(10,i);
	reg = lm.Ridge(alpha = lbd);
	df['skl_stand'].loc[i,'lambda'] = lbd;
	df['skl_stand'].loc[i,'reg'] = reg.fit(hitters_stand[cols],hitters_stand.Salary);

df['skl_norm'] = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.power(10,i);
	reg = lm.Ridge(alpha = lbd);
	df['skl_norm'].loc[i,'lambda'] = lbd;
	df['skl_norm'].loc[i,'reg'] = reg.fit(hitters_norm[cols],hitters_norm.Salary);

sm_stand = df['sm_stand'].iloc[50].reg;
skl_stand = df['skl_stand'].iloc[50].reg;
sm_norm = df['sm_norm'].iloc[50].reg;
skl_norm = df['skl_norm'].iloc[50].reg;

pre_sm_s = sm_stand.predict();
pre_sm_n = sm_norm.predict();
pre_skl_s = skl_stand.predict(hitters_stand[cols]);
pre_skl_n = skl_norm.predict(hitters_norm[cols]);

mse_sm_s = np.sum(np.power(hitters_stand.Salary-pre_sm_s,2)) + df['sm_stand'].iloc[50,0]*np.sum(np.power(sm_stand.params[1:],2));
mse_sm_n = np.sum(np.power(hitters_norm.Salary-pre_sm_n,2)) + df['sm_norm'].iloc[50,0]*np.sum(np.power(sm_norm.params[1:],2));
mse_skl_s = np.sum(np.power(hitters_stand.Salary-pre_skl_s,2)) + df['skl_stand'].iloc[50,0]*np.sum(np.power(skl_stand.coef_,2));
mse_skl_n = np.sum(np.power(hitters_norm.Salary-pre_skl_n,2)) + df['skl_norm'].iloc[50,0]*np.sum(np.power(skl_norm.coef_,2));

#['AtBat', 'Hits', 'HmRun', 'Runs', 'RBI', 'Walks', 'Years', 'CAtBat', 'CHits', 'CHmRun', 'CRuns', 'CRBI', 'CWalks', 'PutOuts', 'Assists', 'Errors', 'League_int', 'Division_int', 'NewLeague_int']

b_p = [407.356,0.037,0.138,0.525,0.231,0.240,0.29,1.108,0.003,0.012,0.088,0.023,0.024,0.025,0.016,0.003,-0.021,0.085,-6.215,0.301];

pre_b_s = hitters_stand[['dummy'] + cols].dot(b_p);
pre_b_n = hitters_norm[['dummy'] + cols].dot(b_p);

mse_b_s = np.sum(np.power(hitters_stand.Salary-pre_b_s,2)) + df['skl_stand'].iloc[50,0]*np.sum(np.power(b_p,2));
mse_b_n = np.sum(np.power(hitters_norm.Salary-pre_b_n,2)) + df['skl_norm'].iloc[50,0]*np.sum(np.power(b_p,2));

skl_ = df['skl'].iloc[50].reg;
pre_skl = skl_.predict(hitters[cols]);
mse_skl = np.sum(np.power(hitters.Salary-pre_skl,2)) + df['skl'].iloc[50,0]*np.sum(np.power(skl_.coef_,2));


reg = lm.Ridge(alpha = 50);
reg.fit(hitters[cols],hitters.Salary);
print(reg.coef_);

train = hitters_stand.sample(frac = 0.5);
test = hitters_stand[~hitters_stand.index.isin(train.index)];

reg = lm.Ridge(alpha = 4);
reg.fit(train[cols],train.Salary);

pre = reg.predict(test[cols]);
mse = np.sum(np.power(pre - test.Salary,2));

mse_null = np.sum(np.power(test.Salary - test.Salary.mean(),2));

reg = lm.Ridge(alpha = np.power(10,10));
reg.fit(train[cols],train.Salary);

pre = reg.predict(test[cols]);
mse = np.sum(np.power(pre - test.Salary,2));

reg = lm.Ridge(alpha = 0);
reg.fit(train[cols],train.Salary);

pre = reg.predict(test[cols]);
mse = np.sum(np.power(pre - test.Salary,2));

lbd = np.linspace(-2,10,num=100);
lbd = np.power(10,lbd);

reg = lm.RidgeCV(alphas = lbd, cv = 10);
reg = reg.fit(train[cols],train.Salary);
print(reg.alpha_);

pre = reg.predict(test[cols]);
mse = np.sum(np.power(pre - test.Salary,2));

best = reg.alpha_;
reg = lm.Ridge(alpha = best);
reg.fit(hitters_stand[cols],hitters_stand.Salary);
print(reg.coef_);


# Lasso

df_sm = pd.DataFrame();
sm_lasso = sm.OLS(train.Salary,train[['dummy'] + cols]);
for i in np.linspace(-2,10,num=100):
	lbd = np.full(20,np.power(10,i));
	lbd[0] = 0;
	df_sm.loc[i,'lambda'] = np.power(10,i);
	df_sm.loc[i,'reg'] = sm_lasso.fit_regularized(alpha = lbd, L1_wt = 1);

df_skl = pd.DataFrame();
for i in np.linspace(-2,10,num=100):
	lbd = np.power(10,i);
	df_skl.loc[i,'lambda'] = np.power(10,i);
	df_skl.loc[i,'reg'] = lm.Lasso(alpha = lbd).fit(train[cols],train.Salary);

lbd = np.linspace(-2,3,num=100);
lbd = np.power(10,lbd);

reg = lm.LassoCV(alphas = lbd, cv = 10);
reg = reg.fit(train[cols],train.Salary);
print(reg.alpha_);

pre = reg.predict(test[cols]);
mse = np.sum(np.power(pre - test.Salary,2));


# PCR

pc = skld.PCA(n_components = 3);
skl_pc = pc.fit_transform(hitters_norm[cols]);
skl_pc = pd.DataFrame(skl_pc);

sm_pc = smpca.PCA(hitters_norm[cols], ncomp = 3);
sm_pc = sm_pc.factors;

#hitters = hitters.reset_index(drop = True);
skl_pc = skl_pc.reset_index(drop = True);
sm_pc = sm_pc.reset_index(drop = True);

skl_pc['dummy'] = 1;
sm_pc['dummy'] = 1;

skl_res = sm.OLS(hitters.Salary,skl_pc).fit();
sm_res = sm.OLS(hitters.Salary,sm_pc).fit();
print(skl_res.summary());
print(sm_res.summary());

tr = pd.DataFrame();
kf = ms.KFold(n_splits=10, shuffle = True);
j = 0;
for traini, testi in kf.split(hitters_norm):
	res = pd.DataFrame();
	train = hitters_norm.iloc[traini];
	test = hitters_norm.iloc[testi];
	pca = smpca.PCA(train[cols],standardize=False, demean=False, normalize=False);
	sm_pc = pca.factors;
	sm_pc['dummy'] = 1;
	c = sm_pc.columns.tolist();
	c = c[-1:] + c[:-1];
	sm_pc = sm_pc[c];
	for i in range(1,len(cols) + 1):
		t1 = pd.DataFrame(test[cols].dot(pca.loadings).iloc[:,:i]);
		t1['dummy'] = 1;
		tr.loc[j,i] = np.sum(np.power(sm.OLS(train.Salary,sm_pc.iloc[:,:i+1]).fit().predict(t1)-test.Salary,2));
	j += 1;
print(tr.mean());

# PLS

tr = pd.DataFrame();
kf = ms.KFold(n_splits=10, shuffle = True);
j = 0;
for traini, testi in kf.split(hitters_norm):
	res = pd.DataFrame();
	train = hitters_norm.iloc[traini];
	test = hitters_norm.iloc[testi];
	for i in range(1,len(cols) + 1):
		reg = cd.PLSRegression(n_components = i);
		reg.fit(train[cols],train.Salary);
		tr.loc[j,i] = np.sum(np.power(reg.predict(test[cols])[0]-test.Salary,2));
	j += 1;

print(tr.mean());



