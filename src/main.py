import pandas
import numpy
import data_sanitizer
import get_unique
import gender_analysis

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
    data_set =  get_netflix_catalogue_dataframe()
    data_sanitizer.handle_null_values(data_set) 
    unique_genres = get_unique.genres(data_set)
    unique_countries = get_unique.countires(data_set)

    names = get_names_dataframe()
    gender_analysis.analyse(names, data_set)


