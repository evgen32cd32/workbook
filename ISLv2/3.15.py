import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;

boston = pd.read_csv('~/Downloads/datasets/Boston.csv');
boston = boston.iloc[:,1:];

cols = boston.columns.tolist()[1:];

reg = [];
result = [];
for i in range(len(cols)):
	reg.append(smf.ols(formula='crim ~ '+cols[i],data = boston));
	result.append(reg[i].fit());
	print(result[i].summary());

fig, ax = plt.subplots(3,4);
for i in range(3):
	for j in range(4):
		sm.graphics.plot_fit(result[i+j*3],1,ax=ax[i,j],vlines = False);
		ax[i,j].set_title(cols[i+j*3]);

plt.show();

regA = smf.ols(formula='crim ~ ' + ' + '.join(cols), data = boston);
resultA = regA.fit();
print(resultA.summary());


fig, ax = plt.subplots(3,4);
for i in range(3):
	for j in range(4):
		sm.graphics.plot_fit(resultA,1+i+j*3,ax=ax[i,j],vlines = False);
		ax[i,j].set_title(cols[i+j*3]);

plt.show();

x = [r.params[1] for r in result];
y = resultA.params[1:];
plt.plot(x,y,'o');
plt.show();


reg2 = [];
result2 = [];
for i in range(len(cols)):
	reg2.append(smf.ols(formula='crim ~ '+cols[i] + ' + np.power(' + cols[i] + ',2) + np.power(' + cols[i] + ',3)',data = boston));
	result2.append(reg2[i].fit());
	print(result2[i].summary());

fig, ax = plt.subplots(3,4);
for i in range(3):
	for j in range(4):
		sm.graphics.plot_fit(result2[i+j*3],1,ax=ax[i,j],vlines = False);
		ax[i,j].set_title(cols[i+j*3]);

plt.show();

