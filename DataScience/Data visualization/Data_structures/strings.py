#----------------------STRINGS----------------------------------------#
# strings are inmutable sequence of characters
text = 'The surface of the circle is 2 pi R ='
text2 = "The surface of the circle is 2 pi R="
text = '''The surface of the circle is 2 pi R'''


#--------------------Formatter---------------------------------#
# % sign lets you produce formatted output also with .format()
"{a}!={b}".format(a=2, b=1)

#Operators
# + and * can be used in strings
# > , >= , == , <= , < and !=

#Translate and replace
fruit_store = 'We have a wonderful apple offer today for 23 cents'
#Replace parts of the strings
text.replace('apple', 'pear', 1)
#remove some specific characters
text.translate(None, 'aeiou')
#separate a string with respect to a single separator
text.partition('wonderful')
#Break a large string down into smaller strings
text3 = text.split("")
#Removes all whitespace at the start and the end, including spaces, tabs, newlines and carriage returns
text3 = text.strip()
