import pandas

class DirectorClassification:
    def __init__(self, directors, genres, data_set):
        self.directors = directors
        self.genres = genres
        self.data_set = data_set
        self.director_genre_dataframe = pandas.DataFrame()

    def get_director_genre_dataframe(self):
        return self.director_genre_dataframe

    def set_director_genre_dataframe(self, director_genre_dataframe):
        self.director_genre_dataframe = director_genre_dataframe

    def populate_director_genre_dataframe(self):
        max = 0 
        maxdir = ''
        directors_dataframe = pandas.DataFrame(0, columns = self.directors, index = self.genres)
        for director in directors_dataframe:
            # Finds the most frequent director.
            # Ignore unknown director.
            if (director == 'Unknown director'):
                break
            temp_df = self.data_set.loc[self.data_set.director.str.contains(director)]['listed_in']
            temp_count = temp_df.shape[0]
            if(temp_count > max):
                maxdir = director
                max = temp_count

            # Populates the director dataframe with count for each genre    
            for listed_in_list in temp_df:
                for genre in self.genres:
                    if genre in listed_in_list.split(','):
                        
                        directors_dataframe[director].loc[genre] += 1.0
                       
        return directors_dataframe
                