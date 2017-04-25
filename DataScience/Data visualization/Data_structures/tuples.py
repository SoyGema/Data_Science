#Tuples are heterogeneous data structures(entries have different meanings),
#while lists are homogeneous sequences.
#Tuples are inmutable and have structure, lists have order

apple_tuple = (23, 45, 89)
#tuples can be created without parenthesis
apple_tupple = 23, 45, 89
#for concatenate tuples
pear_tupple = 13, 49, 54
apple_tupple += pear_tupple

#Methods
#index; find occurence of a value
#count; count the number of occurence of a value
#how many times an element is in a list and where it is placed
fruits.count('apple')
fruits.index('apple')

#Value of tuples
#faster than lists
#protect the data wich is inmutable
#tuples can be used as keys on dictionaries

#tuples as key/value pairs to build dictionaries
fruit_store = dict([('apple', 23), ('watermelon', 34), ('strawerry', 78)])
#you can call to the key
fruit_store['apple']

#signing multiple values
(apple,watermelon,pear) = (23, 43, 56)
#Tuple unpacking : extract tuple elements
store1 = (45, 42, 46)
apple, pear, watermelon = store1

#convert a tuple into a string
str(fruits)
