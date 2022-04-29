import numpy as np;
import pandas as pd;
import statsmodels.formula.api as smf;
import sklearn.model_selection as ms;
import matplotlib.pyplot as plt;

#(a)
rng = np.random.default_rng();
x = rng.standard_normal(100);
y = x - 2 * x * x + rng.standard_normal(100);

#(b)
plt.plot(x,y,'o');
plt.show();

#(c)
err = [];
df = pd.DataFrame({'x':x,'y':y});
for k in range(1,5):
	cols = 'x';
	for i in range(1,k):
		cols += ' + np.power(x,' + str(i+1) + ')';
	mse = 0;
	for i in range(df.shape[0]):
		res = smf.ols(formula='y ~ ' + cols, data=df.drop([i])).fit();
		pre = res.predict(df.iloc[[i]]).iloc[0];
		mse += np.power(pre - df.y.iloc[i],2);
	err.append(mse/df.shape[0]);

print(err);

#(f)
for k in range(1,5):
	cols = 'x';
	for i in range(1,k):
		cols += ' + np.power(x,' + str(i+1) + ')';
	mse = 0;
	res = smf.ols(formula='y ~ ' + cols, data=df).fit();
	print(res.summary());

