import pandas
import numpy
import data_sanitizer
import get_unique
import country_analysis

netflix_titles_filepath = 'netflix_titles.csv'

def get_netflix_catalogue_dataframe():
    '''
        Returns netflix titles as a pandas dataframe.
    '''
    return pandas.DataFrame(pandas.read_csv(netflix_titles_filepath))

if __name__ == "__main__":
    data_set =  get_netflix_catalogue_dataframe()
    data_sanitizer.handle_null_values(data_set) 
    unique_genres = get_unique.genres(data_set)
    unique_countries = get_unique.countires(data_set)
  
    country_analysis = country_analysis.CountryAnalysis(unique_countries, unique_genres, data_set)
    pop_movie_genre = country_analysis.analyse('Movie')
    pop_series_genre = country_analysis.analyse('TV Show')
    


