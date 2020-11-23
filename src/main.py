import pandas

netflix_titles_filepath = 'netflix_titles.csv'

def get_netflix_catalogue_dataframe():
    '''
        Retruns netflix titiles as a pandas dataframe.
    '''
   return pandas.read_csv(netflix_titles_filepath)

if __name__ == "__main__":
    data_set =  get_netflix_catalogue_dataframe()
    print(data_set)