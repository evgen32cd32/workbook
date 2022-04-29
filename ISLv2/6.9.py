import numpy as np;
import pandas as pd;
import sklearn.linear_model as lm;
from sklearn.decomposition import PCA;
from sklearn.model_selection import KFold;
import sklearn.cross_decomposition as cd;

college = pd.read_csv('~/Downloads/datasets/College.csv');
college = college.iloc[:,1:];
college = pd.get_dummies(college,drop_first = True);


# (a)
train = college.sample(frac=0.5);
test = college.loc[~college.index.isin(train.index)];


# (b)
linear = lm.LinearRegression().fit(train.iloc[:,1:],train.Apps);
lmse = np.sum(np.power(linear.predict(test.iloc[:,1:]),2));


# (c)
train_norm = train.copy();
train_norm.iloc[:,1:] = (train_norm.iloc[:,1:] - train.iloc[:,1:].mean())/train.iloc[:,1:].std();
test_norm = test.copy();
test_norm.iloc[:,1:] = (test_norm.iloc[:,1:] - train.iloc[:,1:].mean())/train.iloc[:,1:].std();
lbd = np.power(10,np.linspace(-5,3,num=100));

ridge = lm.RidgeCV(alphas = lbd, cv = 10).fit(train_norm.iloc[:,1:],train.Apps)
rmse = np.sum(np.power(ridge.predict(test_norm.iloc[:,1:]),2));


# (d)
lasso = lm.LassoCV(alphas = lbd, cv = 10).fit(train_norm.iloc[:,1:],train.Apps)
lamse = np.sum(np.power(lasso.predict(test_norm.iloc[:,1:]),2));


# (e)
pca_tr = PCA();
pca = pd.DataFrame(pca_tr.fit_transform(train_norm.iloc[:,1:]));

mse = {};
reg = lm.LinearRegression();
kf = KFold(n_splits=10, shuffle = True);
for i in range(1,pca.shape[1]+1):
	mse[i] = [];
	for tri,tsti in kf.split(pca):
		tr = pca.iloc[tri,:i];
		tst = pca.iloc[tsti,:i];
		ytr = train_norm.Apps.iloc[tri];
		ytst = train_norm.Apps.iloc[tsti];
		reg.fit(tr,ytr);
		mse[i].append(np.sum(np.power(reg.predict(tst) - ytst,2)));

mse = pd.DataFrame(mse);

reg.fit(pca,train.Apps);
pcatst = test_norm.iloc[:,1:].dot(pca_tr.components_.transpose());
pcamse = np.sum(np.power(reg.predict(pcatst) - test.Apps,2));


# (f)
mse = pd.DataFrame();
kf = KFold(n_splits=10, shuffle = True);
j = 0;
for tri,tsti in kf.split(train_norm):
	tr = train_norm.iloc[tri];
	tst = train_norm.iloc[tsti]
	for i in range(1,18):
		reg = cd.PLSRegression(n_components = i);
		reg.fit(tr.iloc[:,1:], tr.Apps);
		mse.loc[j,i] = np.sum(np.power(reg.predict(tst.iloc[:,1:]).transpose()[0] - tst.Apps,2));
	j += 1;

reg = cd.PLSRegression(n_components = 14);
reg.fit(train_norm.iloc[:,1:],train_norm.Apps);
plsmse = np.sum(np.power(reg.predict(test_norm.iloc[:,1:]).transpose()[0] - test_norm.Apps,2));

