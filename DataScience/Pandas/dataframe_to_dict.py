
#Funtion that transform a pandas dataframe column into a dictionary 

def df_to_dict():
   bigdict = df_dataframe['column']
    b = bigdict.to_dict()

    b.values()
    cleanedList = [x for x in b.values() if str(x) !='nan']
    return cleanedList

df_to_dict() 
cleanedList = df_to_dict()
