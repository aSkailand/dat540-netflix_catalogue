#%% Importing libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction import text 
from sklearn.metrics import classification_report, multilabel_confusion_matrix

#%% Reading CSV file, creating & transforming X data
def final_NN_model():
    netflix_data=pd.read_csv("cleaned_Netflix_for_NN.csv")
    smaller_data = netflix_data.copy()

    y = smaller_data.listed_in
    X = [','.join((d, c, r, t)) for d,c,r,t in zip(
                                                    smaller_data.director, 
                                                    smaller_data.cast, 
                                                    smaller_data.rating, 
                                                    smaller_data.title
                                                )]

    # Custom stop words for the CountVectorizer to ignore while transforming.
    customStopWords=['no cast', 'no director', 'movies', 'tv shows',
    'lgbtq movies', 'teen tv shows', 'cult'] 

    # Find all actornames that only appears once in the dataset
    customCastStopWords = smaller_data.cast.str.split(', ').explode().value_counts()[smaller_data.cast.str.split(', ').explode().value_counts() < 2].keys()
    customCastStopWords = [x.lower() for x in customCastStopWords] # Make all values lowercase

    # Add stopwords for vectorizer
    stop_words = text.ENGLISH_STOP_WORDS.union(customStopWords)
    stop_words = stop_words.union(list(customCastStopWords))

    # Split data into train and test data
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1000) 

    # Define the vectorizer algorithm
    matrix = CountVectorizer(
        tokenizer=lambda row: [x.strip() for x in row.split(',') if x != ''], 
        stop_words=stop_words)

    # Transform X data
    x_train_fit = matrix.fit_transform(X_train)
    x_test_fit = matrix.transform(X_test)
    # Transform y data
    y_train_fit = matrix.fit_transform(y_train)
    y_test_fit = matrix.transform(y_test)


    return x_train_fit, x_test_fit, y_train_fit, y_test_fit, matrix


#%% Get data
if __name__ == "__main__":
    x_train_fit, x_test_fit, y_train_fit, y_test_fit, matrix = final_NN_model()
    # Printing out all genres in the y data
    for i in matrix.get_feature_names():
        print(i)
#%% run model
    hidden_layer = 1000 

    # Small datetime to check when ML started
    datetime_object = datetime.datetime.now()
    print("Begin ML: ", datetime_object)

    clf = MLPClassifier(hidden_layer_sizes=(hidden_layer,hidden_layer ),
                        solver='adam', verbose=True, 
                        random_state=1, max_iter=50) 

    clf.fit(x_train_fit, y_train_fit)

    # Small datetime to check when ML stopped
    datetime_object = datetime.datetime.now()
    print("End ML: ", datetime_object)
    #%% Compute results

    y_pred = clf.predict(x_test_fit)

    print("Classification Report: \n", classification_report(y_test_fit,y_pred, target_names=list(matrix.get_feature_names())))

# %% Confusion Matrix

    cm = multilabel_confusion_matrix(y_test_fit, y_pred)
    print(cm)
# %% Plot Confusion Matrix
    labels = matrix.get_feature_names()

    def mutlilabel_cm_plot(confusion_matrix, axes, class_label, class_names, fontsize=14):

        df_cm = pd.DataFrame(
            confusion_matrix, index=class_names, columns=class_names,
        )

        try:
            heatmap = sns.heatmap(df_cm, annot=True, fmt="d", cbar=False, ax=axes)
        except ValueError:
            raise ValueError("Confusion matrix values must be integers.")
        heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=fontsize)
        heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=45, ha='right', fontsize=fontsize)
        axes.set_xlabel('True label')
        axes.set_ylabel('Predicted label')
        axes.set_title(class_label)

    fig, ax = plt.subplots(6, 4, figsize=(7, 12))
        
    for axes, cfs_matrix, label in zip(ax.flatten(), cm, labels):
        mutlilabel_cm_plot(cfs_matrix, axes, label, ["Y", "N"])

    fig.tight_layout()
    plt.show()  

# %% Save Machine Learning Model


    fileName = 'Final_NN_model2.sav'
    pickle.dump(clf, open(fileName, 'wb'))
# %% Load model and print report


    loaded_model = pickle.load(open(fileName, 'rb'))
    y_pred = loaded_model.predict(x_test_fit)

    print("Classification Report: \n", classification_report(y_test_fit,y_pred))
