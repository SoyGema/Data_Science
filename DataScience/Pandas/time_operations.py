
## Operations with dates 


column_date = data['timestamp']
data['@timestamp'].head()


# Apply lambda function to datetime to extract only day-month 
data['@timestamp'].apply(lambda x: x[5:10])
column_date.apply(lambda x: x[5:10])

#Sort the dataframe by date
data.index = data['timestamp']
data.sort_index()
