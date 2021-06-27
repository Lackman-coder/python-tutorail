# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or 
# ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) # Loop through the set, and print the values.

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # Check if "banana" is present in the set. boolen based type output.

