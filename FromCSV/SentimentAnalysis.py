# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 01:00:27 2020

@author: admin
"""

import nltk
import pandas
import csv
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
list_comments=[]
i=0
data = pandas.read_csv('samp.csv')
#sentences=list(data.commentBody) 
sid = SentimentIntensityAnalyzer()
#dataframe ={}
print(len(data))
for i in range(len(data)):
    #sentence=data.commentBody[i]
    dataframe ={}
    dataframe["Comment"] = data.commentBody[i]
    ss = sid.polarity_scores(data.commentBody[i])
    for k in sorted(ss):
        if (k == "neg"):
            dataframe["neg"] = ss[k]
        if (k == "neu"):
            dataframe["neu"] = ss[k]
        if (k == "pos"):
            dataframe["pos"] = ss[k]
    list_comments.append(dataframe)
    

df = pandas.DataFrame(list_comments)
df.to_csv("Sentiments.csv")
