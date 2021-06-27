thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) # To add an item to the end of the list, use the append() method.

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) # Insert an item as the second position.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) # Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple) # The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
print(thislist) # Add elements of a tuple to a list.
