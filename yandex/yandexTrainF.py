import librosa;
from os import listdir;
import pandas as pd;
import numpy as np;

import sklearn.linear_model as lm;
import sklearn.discriminant_analysis as da;
from sklearn.neighbors import KNeighborsClassifier;

path = '/Users/evgeny/Downloads/train/';


wl = pd.DataFrame();
for f in listdir(path):
	if (f == 'targets.tsv'):
		a = 1;
	else:
		y, sr = librosa.load(path + f);
		df = pd.DataFrame(librosa.feature.melspectrogram(y=y, sr=sr));
		df = df.loc[:,df.sum() > 10];
		df = df.loc[df.transpose().sum() > 10, :];
		df = df.transpose().mean();
		df = (df - df.min())/(df.max() - df.min());
		df['name'] = f.split('.')[0];
		wl = pd.concat([wl,pd.DataFrame(df).transpose()],ignore_index = True);

wl = wl.fillna(0);
wl.index = wl.name;
wl = wl.drop(columns = ['name']);

cols = wl.columns.tolist();

f = open(path + 'targets.tsv','r');

for line in f.readlines():
	s = line.split();
	wl.loc[s[0],'y'] = int(s[1]);

a = np.linspace(-2,4,num=100);

lbd = np.power(10,a);
reg = lm.RidgeClassifierCV(alphas=lbd);


reg = da.QuadraticDiscriminantAnalysis();


reg = KNeighborsClassifier();

reg.fit(wl[cols],wl.y);

path = '/Users/evgeny/Downloads/test/';


wlt = pd.DataFrame();
for f in listdir(path):
	if (f == 'targets.tsv'):
		a = 1;
	else:
		y, sr = librosa.load(path + f);
		df = pd.DataFrame(librosa.feature.melspectrogram(y=y, sr=sr));
		df = df.loc[:,df.sum() > 10];
		df = df.loc[df.transpose().sum() > 10, :];
		df = df.transpose().mean();
		df = (df - df.min())/(df.max() - df.min());
		df['name'] = f.split('.')[0];
		wlt = pd.concat([wlt,pd.DataFrame(df).transpose()],ignore_index = True);


wlt = wlt.fillna(0);
wlt.index = wlt.name;
wlt = wlt.drop(columns = ['name']);

for c in cols:
	if not c in wlt.columns.tolist():
		wlt[c] = 0;



pred = reg.predict(wlt[cols]);

res = pd.DataFrame({'name':wlt.index,'pred':pred});

res.pred = res.pred.astype(int);

res.to_csv('/Users/evgeny/Downloads/targets.tsv',sep = '\t', header = False, index = False);


