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

#(b)
train = default.sample(frac=0.5);
test = default[~default.index.isin(train.index)];
pred = smf.logit(formula='default_int ~ income + balance', data=train).fit().predict(test);

pred = pd.DataFrame({'prob':pred});
pred['default'] = 'Yes';
pred.loc[pred.prob > 0.5, 'default'] = 'No';

print(np.sum(pred.default != test.default)/test.shape[0]);

#(d)
train = default.sample(frac=0.5);
test = default[~default.index.isin(train.index)];
pred = smf.logit(formula='default_int ~ income + balance + student', data=train).fit().predict(test);

pred = pd.DataFrame({'prob':pred});
pred['default'] = 'Yes';
pred.loc[pred.prob > 0.5, 'default'] = 'No';

print(np.sum(pred.default != test.default)/test.shape[0]);

