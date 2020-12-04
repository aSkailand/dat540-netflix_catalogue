import pandas
import numpy

def analyse(names, dataset):
    female_names = names.loc[names['gender'] == 'F'].iloc[:,0]
    male_names = names.loc[names['gender'] == 'M'].iloc[:, 0]
    netflix_casts = dataset['cast']
    first_name_occurences = []
    for cast in netflix_casts:
        if cast != 'Unknown cast':
            individuals = cast.split(',')
            for individual in individuals:
                first_name = individual.lstrip().split(' ', 1)[0]
                first_name_occurences.append(first_name)


    first_name_occurences = pandas.Series(first_name_occurences)
    males_in_netflix = 0
    females_in_netflix = 0
    idx = 0
    male_names_str = male_names.str
    female_names_str = female_names.str
    for name in first_name_occurences:
        males_in_netflix += male_names_str.count(name).sum()
        females_in_netflix += female_names_str.count(name).sum()
        idx += 1
        if idx % 100 == 0:
            print('males: ', males_in_netflix)
            print('females: ', females_in_netflix)
