#key / value association data structure
# dictionaries are objects

fruit_store = {'fruit':'apple', 'prices':[23,56]}
#know key/values
fruit_store.keys()
fruit_store.values()

fruit_store.items()
fruit_store2 = fruit_stre.copy()
#to add another key/value
fruit_store2.setdefatult('pineapple',[23])

#Iterators over values, keys or items
[i for i in fruit_store2.itervalues()]
[i for i in fruit_store2.iterkeys()]
[i for i in fruit_store2.iteritems()]

#---------------STRINGS----------------------------------#
#Strings are inmutable sequence of characters
#come in simple, double or triple quotes
text = 'The surface of the circle is 2*pi*r2'
text2 = "The surface of the circle is 2*pi*r2"
text3 = '''The surface of the circle is 2*pi*r2'''

#Strings are inmutable. You can access but not change
text[0]

#Formatter
#It transforms the output into ASCII values
#the syntax is
#string % values

print("%s" % "fruits")

#Methods to query information
fruit_string = "This is a great fruit store. You have 23 apples, 67 bananas and 67 watermelons"
fruit_string.count('a')
