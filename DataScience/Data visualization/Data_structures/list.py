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
 
