import pandas
import data_sanitizer
import get_unique
import yrs_months
#import popular_genre

netflix_titles_filepath = 'netflix_titles.csv'

def get_netflix_catalogue_dataframe():
    '''
        Retruns netflix titles as a pandas dataframe.
    '''
    return pandas.DataFrame(pandas.read_csv(netflix_titles_filepath))

if __name__ == "__main__":
    data_set =  get_netflix_catalogue_dataframe()
    data_sanitizer.handle_null_values(data_set) 
    unique_genres = get_unique.genres(data_set)
    unique_countries = get_unique.countires(data_set)
    years_movies = get_unique.get_years(data_set,"Movie")
    #years = yrs_months.all_years(data_set)
    #print(years)
    #dates_netflix = get_unique.get_months_years(data_set)
    #print(years_movies)
    print(unique_genres)


