#  Tuples are unchangeable, or immutable,but You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x) # Convert the tuple into a list to be able to change it.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) # Convert the tuple into a list, add "orange", and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry") # You cannot remove items in a tuple.
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y) # but, Convert the tuple into a list, remove "apple", and convert it back into a tuple.

thistuple = ("apple", "banana", "cherry") # The del keyword can delete the tuple completely..
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists