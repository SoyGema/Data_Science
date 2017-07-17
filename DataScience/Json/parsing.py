#Transform json files into readable formats with python

#Import ijson library
import ijson

#Read file 
filename = "name.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'path')
    columns = list(objects)
print(columns[0])

#Get the column names
column_names = [col["fieldName"] for col in columns]
column_names


good_columns = [
    "column_1", 
    "column_2", 
    "column_3", 
]

#Make an empty list and fill it with the data coming from column_1, column_2, column_3
data = []
with open(filename, 'r') as f:
    objects = ijson.items(f, 'data.item')
    for row in objects:
        selected_row = []
        for item in good_columns:
            selected_row.append(row[column_names.index(item)])
        data.append(selected_row)

#See how it is going on
data[0]

#Convert it into Pandas
import pandas as pd
stops = pd.DataFrame(data, columns=good_columns)
