import pandas

def handle_null_values(data_set):
  '''
    Takes a dataframe containing netflix titles and handles entries in the dataframe that is null values.
    Director ==  null is set to: 'Unknown director'
    Cast == null is set to: 'Unknown cast'
    Country ==  null is set to: 'Unknown country'
    Date ==  null is set to: 'Unknown date'

  '''
  column_list = sorted(data_set)
  for column in column_list:
    column_data = data_set[column]
    for index, entry in enumerate(column_data):
       if (pandas.isnull(data_set.at[index, column])):
           data_set.at[index, column] = 'Unknown ' + column

  return data_set
