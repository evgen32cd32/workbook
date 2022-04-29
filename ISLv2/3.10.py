import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;

carseats = pd.read_csv('~/Downloads/datasets/Carseats.csv');

reg = smf.ols(formula='Sales ~ Price + Urban + US', data=carseats);
result = reg.fit();
print(result.summary());

reg2 = smf.ols(formula='Sales ~ Price + US', data=carseats);
result2 = reg2.fit();
print(result2.summary());

print(sm.stats.anova_lm(result2,result));

sm.graphics.influence_plot(result2);
plt.show();

plt.plot(result2.predict(),result2.resid_pearson,'o');
plt.show();
