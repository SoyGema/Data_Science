
import pandas as pd
import datetime
import time 

#df ---> dataframe
#'time_column' ---> column that have dates 

#Open .csv file and transform it into pandas readable format

pd.read_csv('.csv')

#Open .json file and transform it into pandas readable format 

pd.read_json('.json')

#General info

df.info()

#Describe mean, min-max and relevant %s

df.describe()

#Transform dates into readable formats

df['time_column']=df['time_column'].apply(lambda x: datetime.strptime(x,'%b-%Y'))

#Order the dataset by dates

df.sort_values(by = 'date_column')

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

#Min date

min(df['date_colum'])

#Max date

max(df['date_column'])

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

#Convert a list into a dataframe

df_new = pd.DataFrame(np.array(list_name).reshape(len(list_name), 1))

#Create a new dataset joining different datasets 

df_new = pd.concat([ df_1, df_2, df_3, df_4, df_n], axis=1)

#Delete a column from a dataset

df.drop('column_name', axis = 1, inplace= True)

#Operate a column of a dataset_1 and create a new column in another dataset_2

df_2['new_name'] = df_1['numerical_column'] - np.array([2])

#Rename header

df.columns.values[1] = "new_name"

#Pandas to csv -out.csv file will be 

df.to_csv('out.csv')

#Convert categorical features into numerical digits in an array 

array = pd.factorize(df['column_name'])[0]

# Null count in a given column

column = df['column_name']
column.isnull().sum()

#Correlation identification

df.rank()
df.corr('column_name')

#Concatenate two dataframes df1 and df2 having equal number of rows 

pd.concat([df1,df2], axis=1)

