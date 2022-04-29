import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;

rng = np.random.default_rng();
x = rng.standard_normal(100);

eps = rng.normal(0,0.25,100);

y = -1 + 0.5 * x + eps;

plt.plot(x,y,'o');
plt.show();

X = pd.DataFrame(data=x,columns=["x"]);
X["dummy"] = 1;

reg = sm.OLS(y,X);
result = reg.fit();
print(result.summary());

sm.graphics.plot_fit(result,0,vlines = False);
plt.show();

X["x2"] = X["x"]**2;
reg = sm.OLS(y,X);
result = reg.fit();
print(result.summary());

eps = rng.normal(0,0.8,100);

y = -1 + 0.5 * x + eps;

X = pd.DataFrame(data=x,columns=["x"]);
X["dummy"] = 1;

reg = sm.OLS(y,X);
result = reg.fit();
print(result.summary());

sm.graphics.plot_fit(result,0,vlines = False);
plt.show();
