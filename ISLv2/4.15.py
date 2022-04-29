import pandas as pd;
import statsmodels.api as sm;
import statsmodels.formula.api as smf;
import matplotlib.pyplot as plt;
import numpy as np;
import sklearn.discriminant_analysis as da;
import sklearn.neighbors as knn;
import sklearn.naive_bayes as nb;

def Power():
	print(np.power(2,3));

def Power2(x, a):
	print(np.power(x,a));

def Power3(x, a):
	return np.power(x, a);

x = np.linspace(1,10,1000);
y = Power3(x, 2);
fig = plt.figure();
#ax = fig.add_axes([0.1,0.1,0.9,0.9]);
ax = fig.add_subplot();
ax.plot(x,y);
ax.set_yscale('log');
plt.show();

