import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;

auto = pd.read_csv('~/Downloads/datasets/Auto.csv', na_values = '?');
auto = auto.dropna();

reg = smf.ols(formula='mpg ~ horsepower', data=auto);
result = reg.fit();
print(result.summary());

a = pd.DataFrame({'horsepower':[98]});
pre = result.get_prediction(a);
print(pre.summary_frame());

sm.graphics.plot_fit(result,1,vlines=False);
plt.show();

sm.graphics.plot_regress_exog(result,'horsepower');
plt.show();
