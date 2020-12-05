#import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from itertools import chain
from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression as lm

netflix_data=pd.read_csv("netflix_titles.csv")
netflix_data.director.fillna("No Director", inplace=True)
netflix_data.cast.fillna("No Cast", inplace=True)
netflix_data.country.fillna("Country Unavailable", inplace=True)
netflix_data.dropna(subset=["date_added", "rating"], inplace=True)

smaller_data = netflix_data.head(1000).copy()
y = smaller_data.listed_in
X = smaller_data.cast

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1000) # random_state=1000 ???
matrix = CountVectorizer(tokenizer=lambda x: x.split(','))
x_train_fit = matrix.fit_transform(X_train)
x_test_fit = matrix.transform(X_test)

y_train_fit = matrix.fit_transform(y_train)
y_test_fit = matrix.transform(y_test)

print(x_train_fit.shape)
print(x_test_fit.shape)
print(y_train_fit.shape)
print(y_test_fit.shape)
model=lm().fit(x_train_fit,y_train_fit)
#print(model.score(x_test_fit,y_test_fit))
#predictions=model.predict(x_test_fit)

#plt.scatter(y_test,predictions)