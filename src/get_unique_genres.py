import pandas

def get_unique_genres(dataset):
    genres_list = dataset.listed_in.tolist()
    genres_split_unique = []
    for genre in genres_list:
        genre = genre.split(", ")
        for g in genre:
            if g not in genres_split_unique:
                genres_split_unique.append(g)
    print(genres_split_unique)

