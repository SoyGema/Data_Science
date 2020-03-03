# SET

# Unordered collection of objects 
# can call hash()
# Inmutable
# Have unique elements
# Sets can contain strings, booleans, tuples

set([1,2,3])
{1,2,3}

# Return unique elements
set([1,1,2,2,3])  
{1, 2, 3}

# Always returns key but not value
set({"hello":5})  
{'hello'}


set(["foo","bar"]) 
{'bar','foo'}

# returns unordered sequence
set("hello")
{'e','h','l','o'}

# Union of sets
x1 = {'foo','bar','baz'}
x2 = {'baz','qux','quux'}
x3 = set(x1)
x4 = set(x2)

 x3 | x4

