# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:07:52 2020

@author: admin
"""

import seaborn as sns
sns.set()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
from sklearn.cluster import KMeans
data=pd.read_csv('Sentiments2.csv')

plt.scatter(data['neg'],data['pos'],marker='.')
plt.xlabel('Negative')
plt.ylabel('Posetive')
plt.show()


x=data[['neg','pos']].copy()
###########################################
kmeans=KMeans(3)
kmeans.fit(x)
clusters=x.copy()
list_comments=[]
clusters['cluster_pred']=kmeans.fit_predict(x)
for i in range(len(clusters['cluster_pred'])):
    #sentence=data.commentBody[i]
    dataframe ={}
    dataframe["Comment"] = data.Comment[i]
    dataframe["neg"] = data.neg[i]
    dataframe["pos"] = data.pos[i]
    val=clusters['cluster_pred'][i]
    if (val == 0):
            dataframe["cluster"] = "mixed"
    if (val == 1):
            dataframe["cluster"] = "mostly Positive"
    if (val == 2):
            dataframe["cluster"] = "revisit"
    list_comments.append(dataframe)
df = pd.DataFrame(list_comments)
df.to_csv("Kmeans2.csv")

plt.scatter(clusters['neg'],clusters['pos'],c=clusters['cluster_pred'],marker='.',cmap='spring')

plt.xlabel('Negative')
plt.ylabel('Positive')
plt.show()

