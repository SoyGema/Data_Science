
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

#Mean of the elements of a column

total_column_mean = df['column_1'].mean()

#Count of unique elements in a column

df['column_1'].nunique()

#Select certain rows from a column in a dataset 
# values are inside the column, are values of the row

row_value_selected = ['value_1', 'value_2', 'value_3']
dataset_columns = df.loc[df['column_1'].isin(row_value_selected)]

#Select a value from a row in a column and show as type 

df['column_1']=(df['column_1']=='value').astype(int)






