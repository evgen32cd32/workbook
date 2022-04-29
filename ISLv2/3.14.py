import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;

rng = np.random.default_rng();
x1 = rng.uniform(size=100);
x2 = 0.5 * x1 + rng.standard_normal(100)/10;
y = 2 + 2 * x1 + 0.3 * x2 +rng.standard_normal(100);

plt.plot(x1,x2,'o');
plt.show();

print(np.corrcoef(x1,x2));

X = pd.DataFrame(data={"y":y,"x1":x1,"x2":x2});

reg = smf.ols(formula='y ~ x1 + x2', data=X);
result = reg.fit();
print(result.summary());

reg2 = smf.ols(formula='y ~ x1', data=X);
result2 = reg2.fit();
print(result2.summary());

reg3 = smf.ols(formula='y ~ x2', data=X);
result3 = reg3.fit();
print(result3.summary());

X2 = pd.concat([X,pd.DataFrame(data={'y':[6],'x1':[0.1],'x2':[0.8]})],ignore_index=True);

reg = smf.ols(formula='y ~ x1 + x2', data=X2);
result = reg.fit();
print(result.summary());

reg2 = smf.ols(formula='y ~ x1', data=X2);
result2 = reg2.fit();
print(result2.summary());

reg3 = smf.ols(formula='y ~ x2', data=X2);
result3 = reg3.fit();
print(result3.summary());

sm.graphics.influence_plot(result);
plt.show();

plt.plot(result.predict(),result.resid_pearson,'o');
plt.show();
