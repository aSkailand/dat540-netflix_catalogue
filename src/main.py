# Modules
import pandas
import numpy
import data_sanitizer
import get_unique
import genre_analysis
import gender_analysis

# Files 
netflix_titles_filepath = 'netflix_titles.csv'
names_gender_filepath = 'name_gender.csv'

def get_netflix_catalogue_dataframe():
    '''
        Returns netflix titles as a pandas dataframe.
    '''
    return pandas.DataFrame(pandas.read_csv(netflix_titles_filepath))

def get_names_dataframe():
    '''
        Return names as a pandas dataframe.
    '''
    return pandas.DataFrame(pandas.read_csv(names_gender_filepath))

if __name__ == "__main__":
    
    # Data set containing netflix catalogue data.
    data_set =  get_netflix_catalogue_dataframe()
    
    # Handling null values, assigning "Unknown {column name}" to null values.
    data_sanitizer.handle_null_values(data_set) 
    
    # Numpy.ndarray containing unique genres.
    unique_genres = get_unique.genres(data_set)
    
    # Numpy.ndarray containing unique countries.
    unique_countries = get_unique.countires(data_set)

    # Nupmy.ndarray containing unique directors.
    unique_directors = get_unique.directors(data_set)

    # Analysing genrer representation in netflix catalogue.
    genre_analysis = genre_analysis.GenreAnalysis(unique_countries, unique_genres, data_set)
    
    # Dictionary containing populare movie genre and count of that genre
    pop_movie_genre = genre_analysis.analyse('Movie')

    # Dictionary containing populare movie genre and count of that genre
    pop_series_genre = genre_analysis.analyse('TV Show')
    
    # DataFrame series containing male and female names.
    names = get_names_dataframe()

    if (input('analyse gender representation? *takes up to 10 minutes* hit: [y]') == 'y'):
        gender_analysis.analyse(names, data_set)



