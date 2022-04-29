import numpy as np;
import pandas as pd;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import sklearn.model_selection as ms;
import itertools as it;
import multiprocessing as mp;

def valid_best_subset(input):
	hitters = pd.read_csv('~/Downloads/datasets/Hitters.csv');
	hitters = hitters.dropna();
	
	hitters["dummy"] = 1;
	
	hitters["League_int"] = 0;
	hitters.loc[hitters.League == 'N', "League_int"] = 1;
	hitters["Division_int"] = 0;
	hitters.loc[hitters.Division == 'W', "Division_int"] = 1;
	hitters["NewLeague_int"] = 0;
	hitters.loc[hitters.NewLeague == 'N', "NewLeague_int"] = 1;
	
	cols = hitters.columns.tolist();
	cols.remove('Salary');
	cols.remove('League');
	cols.remove('Division');
	cols.remove('NewLeague');
	cols.remove('dummy');
	res = pd.DataFrame({});
	train = hitters.iloc[input[0]];
	test = hitters.iloc[input[1]];
	for i in range(1,len(cols)+1):
		rss = np.Inf;
		for subcols in it.combinations(cols,i):
			rssc = np.linalg.lstsq(hitters[['dummy']+list(subcols)],hitters.Salary,rcond=None)[1][0];
			if rssc < rss:
				rss = rssc;
				newc = list(subcols);
		pred = smf.ols(formula='Salary ~ ' + ' + '.join(newc),data=train).fit().predict(test);
		res.loc[0,i] = np.sum(np.power(pred - test.Salary,2));
	return res;

if __name__ == '__main__':
	hitters = pd.read_csv('~/Downloads/datasets/Hitters.csv');
	hitters = hitters.dropna();
	
	results = [];
	
	with mp.Pool(mp.cpu_count()) as pool:
		kf = ms.KFold(n_splits=10, shuffle = True);
		results.append(pool.map(valid_best_subset,kf.split(hitters)));
	
	#print(results);
	df = pd.concat(results[0],ignore_index=True);
	print(df);
	print(df.mean());
