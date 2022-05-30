import numpy as np;
import pandas as pd;
import spacy;
import ru_core_news_md;
from sklearn.decomposition import PCA;



nlp = ru_core_news_md.load();

file  = open('/Users/evgeny/python/workbook/data/nlpSimTest.csv','r');

df = pd.DataFrame();

words = set();
text = [];

i = 0;
for line in file.readlines():
	df[i] = 0;
	for token in nlp(line):
		lem = token.lemma_;
		#if len(lem) < 2:
		#	continue;
		if lem not in words:
			df.loc[lem] = 0;
			words.add(lem);
		df.loc[lem,i] += 1;
	text.append(line);
	i += 1;


#tf
df = df/df.sum();
df = df.transpose();

#idf
df = df * np.log(len(df)/(df != 0).sum());


#SVD
pca = PCA(n_components=20);
svd = pd.DataFrame(pca.fit_transform(df)).transpose();


#distance
res = [];
for i in range(len(svd.columns)):
	for j in range(i):
		res.append([np.sqrt(np.power(svd[i] - svd[j],2).sum()),j,i]);

res = sorted(res,key=lambda x: x[0]);

ans = pd.DataFrame(res,columns=['distance','id1','id2']);
for i in range(len(ans)):
	ans.loc[i,'question1'] = text[ans.loc[i,'id1']];
	ans.loc[i,'question2'] = text[ans.loc[i,'id2']];


#разбить на пары
#res = pd.DataFrame();
#for i in range(len(svd.columns)):
#	res[i] = np.NaN;
#	res.loc[i] = np.NaN;
#	for j in range(i):
#		res.loc[i,j] = np.sqrt(np.power(svd[i] - svd[j],2).sum());
#		res.loc[j,i] = res.loc[i,j];
#ans = pd.DataFrame(columns=['distance','question1','question2']);
#rescp = res.copy();
#while len(rescp) > 1:
#	ri, ci = rescp.stack().idxmin();
#	ans.loc[len(ans),'distance'] = rescp.loc[ri,ci];
#	ans.loc[len(ans)-1,'question1'] = text[ri];
#	ans.loc[len(ans)-1,'question2'] = text[ci];
#	rescp = rescp.drop(index=[ri,ci],columns=[ri,ci]);

#ans.to_csv('/Users/evgeny/python/workbook/data/nlpSimTest_output.csv', sep = ';');
ans.to_excel('/Users/evgeny/python/workbook/data/nlpSimTest_output.xlsx',index=False);

file.close();
