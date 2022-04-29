import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;
import sklearn.discriminant_analysis as da;
import sklearn.neighbors as knn;
import sklearn.naive_bayes as nb;

auto = pd.read_csv('~/Downloads/datasets/Auto.csv',na_values='?');
auto = auto.dropna();

#(a)
auto["mpg01"] = 0;
auto.loc[auto.mpg > auto.mpg.median(), "mpg01"] = 1;

#(b)
pd.plotting.scatter_matrix(auto);
plt.show();

cols = auto.columns.tolist()[1:-2];
fix, ax = plt.subplots(2,4);

i = 0;
j = 0;
for c in cols:
	auto.boxplot(c,"mpg01",ax[i][j]);
	j+=1;
	if j == 4:
		i+=1;
		j = 0;

plt.show()

#(c)
n = auto.shape[0]/2;
train = auto.loc[:n];
test = auto.loc[n:];

#(d)
colsv = cols[1:-1];
lda = da.LinearDiscriminantAnalysis();
lda.fit(train[colsv],train.mpg01);
prlda = lda.predict(test[colsv]);
print(pd.crosstab(prlda,test.mpg01));
print(np.mean(prlda == test.mpg01));

#(e)
qda = da.QudraticDiscriminantAnalysis();
qda.fit(train[colsv],train.mpg01);
prqda = qda.predict(test[colsv]);
print(pd.crosstab(prqda,test.mpg01));
print(np.mean(prqda == test.mpg01));

#(f)
log = smf.logit(formula='mpg01 ~ ' + ' + '.join(colsv),data=train).fit();
print(log.summary());
prlog = pd.DataFrame({'prob':log.predict(test)});
prlog["pred"] = 0;
prlog.loc[prlog.prob > 0.5, "pred"] = 1;
print(pd.crosstab(prlog.pred,test.mpg01));
print(np.mean(prlog.pred == test.mpg01));

#(g)
naive = nb.GaussianNB();
naive.fit(train[colsv],train.mpg01);
prnaive = naive.predict(test[colsv]);
print(pd.crosstab(prnaive,test.mpg01));
print(np.mean(prnaive == test.mpg01));

#(h)
kn = [];
prkn = [];
for k in range(1,7):
	kn.append(knn.KNeighborsClassifier(k));
	kn[k-1].fit(train[colsv],train.mpg01);
	prkn.append(kn[k-1].predict(test[colsv]));
	print(pd.crosstab(prkn[k-1],test.mpg01));
	print(np.mean(prkn[k-1] == test.mpg01));
