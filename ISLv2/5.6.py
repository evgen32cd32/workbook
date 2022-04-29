import numpy as np;
import pandas as pd;
import statsmodels.formula.api as smf;
import sklearn.model_selection as ms;
import matplotlib.pyplot as plt;

default = pd.read_csv('~/Downloads/datasets/Default.csv');

default['default_int'] = 0;
default.loc[default.default == 'No', 'default_int'] = 1;

#(a)
result = smf.logit(formula='default_int ~ income + balance', data=default).fit();
print(result.summary());

#(b - c)
est = pd.DataFrame({'Intercept':[],'income':[],'balance':[]});
for b in range(1000):
	params = smf.logit(formula='default_int ~ income + balance', data=default.sample(frac=1,replace=True)).fit().params;
	est = pd.concat([est,pd.DataFrame(params).transpose()],ignore_index=True);

print(est.describe());
