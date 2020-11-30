
class CountryAnalysis:
    def __init__(self, countries, genres, data_set, pop_genre_list = dict()):
        self.data_set = data_set
        self.countries = countries
        self.genres = genres
        self.pop_genre_list = pop_genre_list
        
    def get_pop_genre_list(self):
        return self.pop_genre_list

    def set_pop_genre_list(self, new_pop_genre_list):
        self.pop_genre_list = new_pop_genre_list

    def discard_type_from_genre(self, type):
        self.genres = list(self.genres)
        if type == 'Movie' and 'Movies' in self.genres:
            self.genres.remove('Movies')
        if type == 'TV Show' and 'TV Shows' in self.genres:
            self.genres.remove('TV Shows')
 
    def analyse(self, type):
        self.discard_type_from_genre(type)
        filter = self.data_set['type'] == type
        data = self.data_set.where(filter).dropna()
          
        pop_genre_country_dict = {}
        pop_genre = ''
        pop_count =  0
        for genre in self.genres:
            temp_max_count = data.loc[data['listed_in'].str.contains(genre, regex = True)]['listed_in'].count()
            pop_count = temp_max_count
            pop_genre = genre
            if (pop_count != 0):
                pop_genre_country_dict[pop_genre] =  pop_count

        print(pop_genre_country_dict)
        return pop_genre_country_dict



        

        