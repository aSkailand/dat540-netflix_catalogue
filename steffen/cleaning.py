#%%
import numpy as np
import pandas as pd


netflix_data=pd.read_csv("../netflix_titles.csv", skipinitialspace=True)
cleaning_data = netflix_data.copy()
cleaning_data.director.fillna("No Director", inplace=True)
cleaning_data.cast.fillna("No Cast", inplace=True)
cleaning_data.dropna(subset=["date_added", "rating"], inplace=True)

indexNames = cleaning_data.listed_in[cleaning_data.listed_in == 'Movies'].index
indexNames2 = cleaning_data.listed_in[cleaning_data.listed_in == 'TV Shows'].index
indexNames3 = cleaning_data.listed_in[cleaning_data.listed_in == ''].index
cleaning_data.drop(indexNames , inplace=True)
cleaning_data.drop(indexNames2 , inplace=True)
cleaning_data.drop(indexNames3 , inplace=True)
cleaning_data.dropna(subset=["listed_in", "rating", "title"], inplace=True)

print(cleaning_data.shape)

## Change and refine genres.
replacements = {
        "Anime Features":"Anime",
        "Anime Series":"Anime",
        "Children & Family Movies": "Kids",
        "Classic & Cult": "Classic, Cult",
        "Classic Movies": "Classic",
        "Crime TV Shows": "Crime",
        "Cult Movies": "Cult",
        "International Movies": "International",
        "Docuseries": "Documentaries",
        "Kids' TV": "Kids",
        "Korean TV Shows": "International",
        "Romantic Movies": "Romantic",
        "Romantic TV Shows": "Romantic",
        "Stand-Up Comedy & Talk Shows": "Comedies",
        "Stand-Up Comedy": "Comedies",
        "TV Action & Adventure": "Action & Adventure",
        "TV Comedies": "Comedies",
        "TV Dramas": "Dramas",
        "TV Horror": "Horror",
        "Horror Movies": "Horror",
        "TV Mysteries": "Mysteries",
        "TV Sci-Fi & Fantasy": "Sci-Fi & Fantasy",
        "TV Thrillers": "Thrillers",
        "Cult TV": "Cult",
        "International TV Shows": "International",
    }    


cleaning_data.listed_in = cleaning_data.listed_in.replace(replacements, regex=True)

#%% Check for duplicates

# Get a Boolean indexer for duplicates.
def has_duplicates(listObj):
    return len(listObj) != len(set(listObj))

duplicated_set = set()
for index, item in enumerate(cleaning_data.listed_in):
    lst = item.split(',')
    if has_duplicates(lst):
        string = ','.join(lst)
        duplicated_set.add(string)

dicts = {}
for item in duplicated_set:
    lst = item.split(',')
    string = ','.join(lst)
    not_dup = ','.join(set(lst))
    dicts[string] = not_dup
    cleaning_data.listed_in = cleaning_data.listed_in.replace(dicts, regex=True)

print(dicts)

#%%
duplicated_set = set()
for index, item in enumerate(cleaning_data.listed_in):
    lst = item.split(',')
    if has_duplicates(lst):
        string = ','.join(lst)
        duplicated_set.add(string)

print(duplicated_set)
#%%

cleaning_data.to_csv('file1.csv') 



# %%
