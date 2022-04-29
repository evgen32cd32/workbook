import numpy as np;
import pandas as pd;
import statsmodels.formula.api as smf;
import sklearn.model_selection as ms;
import matplotlib.pyplot as plt;

weekly = pd.read_csv('~/Downloads/datasets/Weekly.csv');
weekly['Direction_int'] = 0;
weekly.loc[weekly.Direction == 'Up', 'Direction_int'] = 1;

#(a)
res = smf.logit('Direction_int ~ Lag1 + Lag2',data=weekly).fit();

#(b)
res0 = smf.logit('Direction_int ~ Lag1 + Lag2',data=weekly.drop([0])).fit();

#(c)
prob = res0.predict(weekly.iloc[[0]]);

#(d)
err = 0;
for i in range(weekly.shape[0]):
	resi = smf.logit('Direction_int ~ Lag1 + Lag2',data=weekly.drop([i])).fit();
	prob = resi.predict(weekly.iloc[[i]]).iloc[0];
	pred = 1 if prob > 0.5 else 0;
	err += int(pred != weekly.Direction_int.iloc[i]);

print(err);
