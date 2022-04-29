import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;
import sklearn.discriminant_analysis as da;
import sklearn.neighbors as knn;
import sklearn.naive_bayes as nb;

weekly = pd.read_csv('~/Downloads/datasets/Weekly.csv');

weekly["Direction_int"] = 0;
weekly.loc[weekly.Direction == "Up", "Direction_int"] = 1;

#(a)
pd.plotting.scatter_matrix(weekly);
plt.show();

print(weekly.corr());

#(b)
cols = weekly.columns.tolist()[1:-3];
reg = smf.logit(formula='Direction_int ~ ' + ' + '.join(cols), data=weekly);
result = reg.fit();
print(result.summary());

#(c)
pr = pd.DataFrame({'prob':result.predict()});
pr["pred"] = 0;
pr.loc[pr.prob > 0.5, "pred"] = 1;
ct = pd.crosstab(pr.pred,weekly.Direction_int);
print(ct);
print(np.mean(pr.pred == weekly.Direction_int));

#(d)
train = weekly.loc[weekly.Year < 2009];
test = weekly.loc[weekly.Year >= 2009];

reg1 = smf.logit(formula='Direction_int ~ Lag2', data=train);
result1 = reg1.fit();
print(result1.summary());

pr1 = pd.DataFrame({'prob':result.predict(test)});
pr1["pred"] = 0;
pr1.loc[pr1.prob > 0.5, "pred"] = 1;
print(pd.crosstab(pr1.pred,test.Direction_int));
print(np.mean(pr1.pred == test.Direction_int));

#(e)
lda = da.LinearDiscriminantAnalysis();
lda.fit(train.Lag2.array.reshape(-1,1),train.Direction_int);
prlda = lda.predict(test.Lag2.array.reshape(-1,1));
print(pd.crosstab(prlda,test.Direction_int));
print(np.mean(prlda == test.Direction_int));

#(f)
qda = da.QuadraticDiscriminantAnalysis();
qda.fit(train.Lag2.array.reshape(-1,1),train.Direction_int);
prqda = qda.predict(test.Lag2.array.reshape(-1,1));
print(pd.crosstab(prqda,test.Direction_int));
print(np.mean(prqda == test.Direction_int));

#(g)
knn1 = knn.KNeighborsClassifier(1);
knn1.fit(train.Lag2.array.reshape(-1,1),train.Direction_int);
prknn1 = knn1.predict(test.Lag2.array.reshape(-1,1));
print(pd.crosstab(prknn1,test.Direction_int));
print(np.mean(prknn1 == test.Direction_int));

#(h)
naive = nb.GaussianNB();
naive.fit(train.Lag2.array.reshape(-1,1),train.Direction_int);
prnaive = naive.predict(test.Lag2.array.reshape(-1,1));
print(pd.crosstab(prnaive,test.Direction_int));
print(np.mean(prnaive == test.Direction_int));

#(i)
ct = {'log':[pd.crosstab(pr1.pred,test.Direction_int),np.mean(pr1.pred == test.Direction_int)],
	'lda':[pd.crosstab(prlda,test.Direction_int),np.mean(prlda == test.Direction_int)],
	'qda':[pd.crosstab(prqda,test.Direction_int),np.mean(prqda == test.Direction_int)],
	'knn1':[pd.crosstab(prknn1,test.Direction_int),np.mean(prknn1 == test.Direction_int)],
	'naive':[pd.crosstab(prnaive,test.Direction_int),np.mean(prnaive == test.Direction_int)]};
for a in ct:
	print(a + ' ' + str(ct[a][1]));
	print(ct[a][0]);
	print('\n');

