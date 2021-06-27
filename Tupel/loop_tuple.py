# You can loop through the tuple items by using a for loop.

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) # Iterate through the items and print the values.

thistuple = ("apple", "banana", "cherry") # Use the range() and len() functions to create a suitable iterable.
for i in range(len(thistuple)):
  print(thistuple[i]) # Print all items by referring to their index number.

thistuple = ("apple", "banana", "cherry") # You can loop through the list items by using a while loop.
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1  # Print all items, using a while loop to go through all the index numbers.
