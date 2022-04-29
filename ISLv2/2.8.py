import pandas as pd;
import numpy as np;
import matplotlib.pyplot as plt;
from mpl_toolkits.mplot3d import Axes3D;

# (a)
college = pd.read_csv('~/Downloads/datasets/College.csv');

# (b)
college = college.rename(index={i : college.iat[i,0] for i in range(college.shape[0])});
college = college.iloc[:,1:];

# (c.1)
college.describe();

# (c.2)
college["Private_int"] = np.nan;
college.loc[college["Private"] == "Yes", "Private_int"] = 1;
college.loc[college["Private"] == "No", "Private_int"] = 0;
cols = college.columns.tolist();
cols = cols[-1:] + cols[1:-1] + cols[:1];
college = college[cols];

pd.plotting.scatter_matrix(college.iloc[:,0:10]);
plt.show();

# (c.3)
college[["Outstate","Private_int"]].boxplot(by = "Private_int");
plt.show();

# (c.4)
college["Elite"] = 0;
college.loc[college["Top10perc"] > 50, "Elite"] = 1;
college.loc[college["Elite"] == 1, :].shape;
college[["Outstate","Elite"]].boxplot(by = "Elite");
plt.show();

# (c.5)
college.hist();
plt.show();


