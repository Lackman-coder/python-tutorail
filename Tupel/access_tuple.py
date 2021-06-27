thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) # You can access tuple items by referring to the index number, inside square brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) # Negative indexing means start from the end.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) # You can specify a range of indexes by specifying where to start and where to end the range.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # This example returns the items from the beginning to, but NOT included, "kiwi".

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # This example returns the items from "cherry" and to the end.

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) # This example returns the items from index -4 (included) to index -1 (excluded).

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") # To determine if a specified item is present in a tuple use the in keyword.
  