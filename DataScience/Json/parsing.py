#Transform json files into readable formats with python

#Import ijson library
import ijson

#Read file 
filename = "name.json"
with open(filename, 'r') as f:
    objects = ijson.items(f, 'meta.view.columns.item')
    columns = list(objects)
