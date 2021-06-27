thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) # Print all items in the list, one by one below.

thislist1 = ["apple", "banana", "cherry"]
for i in range(len(thislist1)): # Print all items by referring to their index number:
  print(thislist1[i])  # Use the range() and len() functions to create a suitable iterable.

thislist2 = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist2):
  print(thislist2[i])
  i = i + 1 # Print all items, using a while loop to go through all the index numbers.

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] # A short hand for loop that will print all items in a list.