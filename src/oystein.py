import pandas
import numpy
import seaborn as sns
import matplotlib.pyplot as plt

def movies_series_release(dataset):
    plt.figure(figsize = (35,6))
    sns.countplot(x='release_year',data = dataset, hue='type')
    plt.show()
