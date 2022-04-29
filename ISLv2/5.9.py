import numpy as np;
import pandas as pd;
import statsmodels.formula.api as smf;
import sklearn.model_selection as ms;
import matplotlib.pyplot as plt;

boston = pd.read_csv('~/Downloads/datasets/Boston.csv');

#(a)
mu = boston.medv.mean();

#(b)
semu = boston.medv.std()/np.sqrt(boston.shape[0]);

#(c)
mean = [];
for b in range(1000):
	df = boston.sample(frac=1,replace=True);
	mean.append(df.medv.mean());

df = pd.DataFrame({'mean':mean});
print(df['mean'].std());

#(e)
med = boston.medv.median();

#(f)
medis = [];
for b in range(1000):
	df = boston.sample(frac=1,replace=True);
	medis.append(df.medv.median());

df = pd.DataFrame({'median':medis});
print(df['median'].std());

#(g)
q10 = boston.medv.quantile(q=0.1);

#(h)
q = [];
for b in range(1000):
	df = boston.sample(frac=1,replace=True);
	q.append(df.medv.quantile(q=0.1));

df = pd.DataFrame({'x':q});
print(df.x.std());
