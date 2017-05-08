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
def func1(a,b):
    def inner_func(x):
        return x*x
    return inner_func(a) + inner_func(b) , inner_func(a)

#we can put inmutable or other data structures when building a function
def list_grow(x, list=[]):
    list.append(x)
    return list

def add_mean(x, *data):
    return x + sum(data)/float(len(data))

#Arbitrary number of keyword arguments
#kwargs is a dict of the keyword args passed to the function
def print_keyword_args(**kwargs):
    for key, value in kwargs.iteritems():
        print "%s = %s" % (key, value)

print_keyword_args(first_name="John", last_name="Doe")
#also used in dictionry
kwargs = {'first_name': 'Bobby' , 'last_name' : 'Smith'}
print_keyword_args(x=[1,2,3], y=[3,3,0])

#---------------------METHODS,FUNCTIONS AND ATTRIBUTES RELATED TO FUNCTION OBJECTS--------------------------#
#METHOD : it is a function wich is a member of a class
class apple:
    def my_method(self):
        print "I am an apple"

apple = apple()
apple.my_method() #prints "I am an apple"

#RECURSIVE FUNCTIONS
#Recursion is a common technique in computer science where a function calls itself

#Here sum_fact is basically inside the function and it operates

def sum_fact(n):
    if n != 0:
        return n + sum_fact(n-1)
    else:
        return 1

def fibbonacci(n):
    if n >= 2:
        else:
    return 1

def factorial(n):
    assert n > 0
    if n != 0:
        return n * factorial(n-1)
    else:
        return 1

#Assigning a function to a variable
#It is great when you want to refactor

def sq(x): return x*x
square = sq


#Anonymous function : the lambda keyword
#lambda function are short one-line functions that have no name.
#They can contain only one statement so for instance the if, for and while are not allowed

#lambda is an expression whereas def is a statement
product = lambda x,y: x*y

def sum_surf(n):
    return 3,14 + n

sum_surf2 = lambda n: 3,14 + n
surf = sum_surf2
