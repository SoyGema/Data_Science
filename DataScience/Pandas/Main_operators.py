
import pandas as pd
import datetime
import time 

#df ---> dataframe
#'time_column' ---> column that have dates 

#Transform dates into readable formats

df['time_column']=df['time_column'].apply(lambda x: datetime.strptime(x,'%b-%Y'))

#Group the data taking two columns and count it 

status_data = df.groupby(['column_1'])['column_2'].count()

#Transform data into float

df['column_1']=df['column_2'].astype(float)
