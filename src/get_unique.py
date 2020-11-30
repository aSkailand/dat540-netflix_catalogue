import pandas
import numpy

def genres(dataset):
    genres_list = dataset.listed_in.tolist()
    return get_unique(genres_list)

def countires(dataset):
    countries_list = dataset.country.tolist()
    return get_unique(countries_list)
    
def get_unique(data_list):
    unique_list = []
    for entry in data_list:
        entry = entry.split(", ")
        for e in entry:
            e = e.replace(',', '') 
            unique_list.append(e)
    return numpy.unique(unique_list)