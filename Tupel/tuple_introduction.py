# tuple ()

"""
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets."""

thistuple = ("apple", "banana", "cherry")
print(thistuple) # this is tuple method.

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) # Tuples allow duplicate values.

thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) # To determine how many items a tuple has, use the len() function.

thistuple = ("apple",)
print(type(thistuple)) # One item tuple, remember the comma,

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) # if without , in end of tuple items python think its a string for variable.

tuple1 = ("apple", "banana", "cherry") # Tuple items can be of any data type.
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False) # String, int and boolean data types.

tuple1 = ("abc", 34, True, 40, "male") # A tuple with strings, integers and boolean values.

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # this check the type of tuple..

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple) # Using the tuple() method to make a tuple.
