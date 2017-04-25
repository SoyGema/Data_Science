list = ["apple","banana","strawerry"]
list2 = [2, 3, 4]

#Add elemnt to a list
list2.append(5)
list.append("watermelon")
#Add element in a list in a given possition
list2.insert(1, 3)
list.insert(2, "pear")
#Counts the number of times an element appears in a list


#Functions that are useful with lists
## filter()
## map()
## reduce()

#filter -- First we define a function
def f(x):
    return x % 2 != 0 and x % 3 != 0

#First we refine the function
filter(f, range(1, 25))

#lists to dictionary
key = ["apple", "banana", "strawerry"]
value = [2, 3, 4]

dictionary = dict(zip(keys, values))
 
#Difference between append() and extend()
#append() --- adds an object at the end of the list or even another list
#extend() ---

fruits = ['banana', 'apple', 'watermelon']
#add elements to the list
fruits.append('strawerry')
#add list of elements to the list
fruits.append(['pear','melon'])
#even more clean
fruits2 = ['pear','melon']
fruits.append(fruits2)


#extend is used for append the elements one by one of a given list rather
#the list itself
fruits.extend(fruits2)


#method index()
#it searches for an element in a list
fruits.index('apple')

#Operators in lists
# + is used as an extend
fruits += ['grapefruit']

#Slicing: access to a part of the list
#by default the first index is 0
fruits[:] #returns all list
fruits[2:] #from second element going beyond


#List compresenhesion
#straightfoward writting for loops in list data structures
pair_numbers = []
for i in range(10):
    if i % 2 ==0:
        pair_numbers.append(i)

pair_numbers = [i for i in range(10) if i % 2==0]

#how to copy a list
import copy
fruits_copy = copy.copy(fruits)
#when having nested objects, meaning a copy of a copy
fruits_cpoy = copy.deepcopy(fruits)
