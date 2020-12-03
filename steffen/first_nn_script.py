#%% Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction import text 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
#%% Reading CSV file, creating & transforming X data
netflix_data=pd.read_csv("file1.csv")

smaller_data = netflix_data.copy()

y = smaller_data.listed_in
X = [','.join((a, d, r, t)) for a,d,r,t in zip(smaller_data.director, smaller_data.cast, smaller_data.rating, smaller_data.title)]

# Custom stop words for the CountVectorizer to ignore while transforming.
customStopWords=['no cast', 'no director', 'movies', 'tv shows', 'international', 'comedies']
add_stop_words = text.ENGLISH_STOP_WORDS.union(customStopWords)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1000) 
matrix = CountVectorizer(
    tokenizer=lambda row: [x.strip() for x in row.split(',') if x != ''], 
    stop_words=add_stop_words)

x_train_fit = matrix.fit_transform(X_train)
x_test_fit = matrix.transform(X_test)

#print(smaller_data.listed_in)
#print(matrix.get_feature_names())

#%% Transform y data
y_train_fit = matrix.fit_transform(y_train)
y_test_fit = matrix.transform(y_test)

# Printing out all genres in the y data
for i in matrix.get_feature_names():
    print(i)

#print(matrix.get_feature_names())
#print(x_train_fit.toarray())
#%% NN algorithm
hidden_layer1 = 1000 #round(x_train_fit.shape[1]*(2/3) + y_train_fit.shape[1])

# Small datetime to check when ML started
datetime_object = datetime.datetime.now()
print("Begin ML: ", datetime_object)

clf = MLPClassifier(hidden_layer_sizes=(hidden_layer1 ),
                    solver='adam', verbose=True, 
                    random_state=1, max_iter=50) 

clf.fit(x_train_fit, y_train_fit)
y_pred = clf.predict(x_test_fit)
print(accuracy_score(y_test_fit, y_pred))
# cm = confusion_matrix(y_test_fit, y_pred)
# print(cm)
clf_score = clf.score(x_test_fit, y_test_fit)
print("clf_score:", clf_score)

# Small datetime to check when ML stopped
datetime_object = datetime.datetime.now()
print("End ML: ", datetime_object)
# %%
# overfitting?
# loss function

# TODO: split words in summary/title better
# TODO: Take "TV Shows" out of data?
# TODO: remove actors that only plays in one movie


# %%
