import pandas as pd
import numpy as np


def genresOfMoviesSeries(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Returns a dataFrame where the genre of every movie/series is split into columns 
    where each row is related to its respective movie in netflix_titles.csv
    '''

    listed_in = df['listed_in']

    genres = listed_in.str.split(', ', expand = True)
    genres = genres.rename(columns = {0: 'genre1', 1: 'genre2', 2: 'genre3'})

    return genres


#### Find total occurence of each genre ####
# Need to do this to find which genres has a lot of data to work with.
def totalOccurenceOfGenres(df: pd.DataFrame) -> pd.Series:
    '''
    Returns a series containing the names of every
    genre, and how many times the genre occurs.
    '''
    genreOccurences = pd.Series(dtype='float64')
    
    for genre in df:
        column = df[genre].value_counts()
        genreOccurences = genreOccurences.add(column, fill_value = 0)
    genreOccurences = genreOccurences.sort_values(ascending = False)

    return genreOccurences


def moviesSeriesWithGenre(df: pd.DataFrame, genre_name: str) -> pd.DataFrame:
    '''
    Returns a dataFrame where only the series/movies
    having the given genre is contained.
    '''
    # Sets the value of every column containing genre_name == true
    rowsContainingGenre = (df == genre_name)

    # Sets every row having True in any of the columns equal to True.
    rowsContainingGenre = rowsContainingGenre.any(axis = 'columns')

    return df[rowsContainingGenre]