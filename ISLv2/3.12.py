import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;

rng = np.random.default_rng();
x = rng.standard_normal(100);
x = x / np.sqrt(np.sum(x**2));
y = 2 * x + rng.standard_normal(100);
y = y / np.sqrt(np.sum(y**2));

reg = sm.OLS(y,x);
result = reg.fit();
print(result.summary());

reg2 = sm.OLS(x,y);
result2 = reg2.fit();
print(result2.summary());
