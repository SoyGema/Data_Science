
import pandas as pd
import datetime
import time 

#df ---> dataframe
#'time_column' ---> column that have dates 

#Transform dates into readable formats

df['time_column']=df['time_column'].apply(lambda x: datetime.strptime(x,'%b-%Y'))

#Group the data taking two columns and count it 

status_data = df.groupby(['column_1'])['column_2'].count()

#Transform data into float // int

df['column_1']=df['column_1'].astype(float)
df['column_1']=df['column_1'].astype(int)

#Sum the elements of a column

total_column_sum = df['column_1'].sum()

#Count the number of categories inside a column of a dataset 

df['column'].value_counts()

#Mean of the elements of a column

total_column_mean = df['column_1'].mean()

#Max of the elements of a column

total_column_mean = df['column_1'].max()

#Count of unique elements in a column

df['column_1'].nunique()

#Select certain rows from a column in a dataset 
# values are inside the column, are values of the row

row_value_selected = ['value_1', 'value_2', 'value_3']
dataset_columns = df.loc[df['column_1'].isin(row_value_selected)]

#Select a value from a row in a column and show as type 

df['column_1']=(df['column_1']=='value').astype(int)

#Convert a dataframe column into a list 

list_name = df['column_1'].values.tolist()

#Create a new dataset joining different datasets 

dataset_new = pd.concat([ dataset_1, dataset_2, dataset_3, dataset_4, dataset_n], axis=1)

#Delete a column from a dataset

dataset.drop('column_name', axis = 1, inplace= True)

#Operate a column of a dataset_1 and create a new column in another dataset_2

dataset2['new_name'] = dataset1['numerical_column'] - np.array([2])



