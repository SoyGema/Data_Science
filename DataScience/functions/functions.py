##------------------------FUNCTIONS-----------------------##
#definition
#we use the keyword def and the statements afterwards
#functiona are objects so you can assign a function to a variable name


def sum(a,b):
    from math import fsum
    return a + b
#we call the function  by putting variables -arguments- in this case 2 and 3
#here a and b are the parameters and must be provided before the arguments
sum(2,3)

#you can use the parameters as a dictionary and call it with * and the function as
param = {'a':2,'b':2,}
sum(**param)

#you can write a function on a single line if the block statement is a simple compound statement
def sum(a,b): return a + b

#we dont need to return something necessarily
i = 0
def increment():
    global i
    i += 1

#Interesting : functions might be nested . Just call in the return for the funtion inside the variable
