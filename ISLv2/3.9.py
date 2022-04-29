import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;

auto = pd.read_csv('~/Downloads/datasets/Auto.csv', na_values = '?');
auto = auto.dropna();

#(a)
pd.plotting.scatterplot_matrix(auto);
plt.show();

#(b)
corr = auto.drop(columns=["name"]).corr();
print(corr);

#(c)
allcols = auto.columns.tolist()[1:-1];
reg = smf.ols(formula='mpg ~ ' + ' + '.join(allcols), data = auto);
result = reg.fit();
print(result.summary());

#(d)
sm.graphics.plot_partregress_grid(result);
plt.show();

sm.graphics.influence_plot(result);
plt.show();

plt.plot(result.predict(),result.resid_pearson,'o');
plt.show();

#(e)
allinters = [];
for i in range(0,len(allcols)):
	for j in range(i+1,len(allcols)):
		allinters += [allcols[i]+':'+allcols[j]];
reg = smf.ols(formula='mpg ~' + ' + '.join(allcols) + ' + ' + ' + '.join(allinters),data = auto);
result = reg.fit();
print(result.summary());







