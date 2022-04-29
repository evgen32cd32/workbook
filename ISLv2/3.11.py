import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;

rng = np.random.default_rng();
x = rng.standard_normal(100);
y = 2 * x + rng.standard_normal(100);

reg = sm.OLS(y,x);
result = reg.fit();
print(result.summary());

reg2 = sm.OLS(x,y);
result2 = reg2.fit();
print(result2.summary());

t = np.sqrt(result.nobs - 1) * np.sum(x*y) / np.sqrt(np.sum(x**2)*np.sum(y**2) - np.power(np.sum(x*y),2));
print(t);

X = pd.DataFrame(data=x,columns=["x"]);
X["dummy"] = 1;
reg = sm.OLS(y,X);
result = reg.fit();
print(result.summary());

Y = pd.DataFrame(data=y,columns=["y"]);
Y["dummy"] = 1;
reg2 = sm.OLS(x,Y);
result2 = reg2.fit();
print(result2.summary());
