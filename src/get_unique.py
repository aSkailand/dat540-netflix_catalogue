import pandas
import numpy

def directors(dataset):
    directors_list = dataset.director.tolist()
    return get_unique(directors_list)

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

def get_years(dataset,movie_or_show):
    """
    Input params
    dataset: Should be the cleaned dataset (NaNs should be taken care of)
    movie_or_series: Specify "Movie" for movies or "TV Show" for shows.
    """
    new_df = dataset[dataset["type"] == movie_or_show]
    years_only = []
    for row in new_df["date_added"]:
        year = row[-4:] #Year is the last 4 chars in the date_added string
        if year != "dded": #In the case where the year is "Unknow date added"
            years_only.append(int(year))
    return years_only


def give_years(dates_dataset):
    for d in dates_dataset:
        print(d)
    return d

def get_months_years(dataset):
    dates_only = dataset[dataset.date_added != "Unknown date_added"].date_added
    dates_only["year"] = dates_only.apply(lambda x: x.split(', ')[-1]) #Lambda: Iterates though every entry. Splits by comma and extracts the last value (which is year)
    dates_only["month"] = dates_only.apply(lambda x: x.split(' ')[0]) #Split by whitespace and only keep the first "value", which is the month
    return dates_only
#def get_months_years