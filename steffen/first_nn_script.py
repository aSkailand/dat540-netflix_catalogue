#%%
import tensorflow as tf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from itertools import chain
from collections import Counter

import datetime

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import text 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

netflix_data=pd.read_csv("netflix_titles.csv", skipinitialspace=True)
#netflix_data.director.fillna("No Director", inplace=True)
#netflix_data.cast.fillna("No Cast", inplace=True) # feil?
#netflix_data.country.fillna("Country Unavailable", inplace=True)
#netflix_data.dropna(subset=["date_added", "rating", "director", "cast"], inplace=True)


## Change and refine genres.
replacements = {
        "Comedy": "Comedies",
        " & ": ",",
        ", ": ",",
        "'": "",
        ":": "",
        ".": "",
        " ": ","
    }    
replacements_title= {
        " ": ","
    }   

smaller_data = netflix_data.copy()
smaller_data.dropna(subset=["date_added", "rating", "director", "cast"], inplace=True)

smaller_data.listed_in = smaller_data.listed_in.str.strip().replace(replacements, regex=True)
smaller_data.title = smaller_data.title.str.strip().replace(replacements, regex=True)

word_freq = smaller_data.title.str.lower().str.split(expand=True).stack().value_counts()
title_stopwords = word_freq[word_freq.gt(100)].index

y = smaller_data.listed_in
X = [','.join((a, d, r, t)) for a,d,r,t in zip(smaller_data.director, smaller_data.cast, smaller_data.rating, smaller_data.title)]
#X = smaller_data.title
my_additional_stop_words=['no cast', 'no director', 'international', 'movies', 'stand-up', 
                            'tv', 'shows', 'movie']
add_stop_words = text.ENGLISH_STOP_WORDS.union(my_additional_stop_words)
add_stop_words = add_stop_words.union(title_stopwords)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1000) # random_state=1000 ???
matrix = CountVectorizer(tokenizer=lambda x: x.split(','), stop_words=add_stop_words)
x_train_fit = matrix.fit_transform(X_train)
x_test_fit = matrix.transform(X_test)

print(smaller_data.listed_in)

#print(matrix.get_feature_names())
#%%

y_train_fit = matrix.fit_transform(y_train)
y_test_fit = matrix.transform(y_test)

#print(matrix.get_feature_names())
#print(x_train_fit.toarray())
#%%
hidden_layer1 = 1000 #round(x_train_fit.shape[1]*(2/3) + y_train_fit.shape[1])

datetime_object = datetime.datetime.now()
print("Begin ML: ", datetime_object)


clf = MLPClassifier(hidden_layer_sizes=(hidden_layer1 ),
                    solver='adam', verbose=True, 
                    random_state=1, max_iter=50) #tol=0.00000001,max_iter=1000,

clf.fit(x_train_fit, y_train_fit)
y_pred = clf.predict(x_test_fit)
print(accuracy_score(y_test_fit, y_pred))
# cm = confusion_matrix(y_test_fit, y_pred)
# print(cm)
clf_score = clf.score(x_test_fit, y_test_fit)
print("clf_score:", clf_score)

print(X_train)

datetime_object = datetime.datetime.now()
print("End ML: ", datetime_object)
# %%
# overfitting?
# loss function

# TODO: split words in summary/title better
# TODO: Take "TV Shows" out of data?

