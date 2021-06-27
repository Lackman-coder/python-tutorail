# set

'''Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.
Once a set is created, you cannot change its items, but you can add new items. '''

thisset = {"apple", "banana", "cherry"} # Sets are unordered, so you cannot be sure in which order the items will appear.
print(thisset)  # this set method.

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset) # Duplicate values will be ignored,set not allow duplicate value two times or more.

thisset = {"apple", "banana", "cherry"}
print(len(thisset)) # To determine how many items a set has, use the len() method.

set1 = {"apple", "banana", "cherry"} # Set items can be of any data type.
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} # String, int and boolean data types.
set1 = {"abc", 34, True, 40, "male"} # A set can contain different data types.

myset = {"apple", "banana", "cherry"}
print(type(myset)) # What is the data type of a set?

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset) # It is also possible to use the set() constructor to make a set.