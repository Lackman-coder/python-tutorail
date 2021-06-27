fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

#  Without list comprehension you will have to write a for statement with a conditional test inside: 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "e" in x] # this method you write code in short form comprehension.

print(newlist) 

# these are some example of make decision in comprehension:
newlist = [x for x in fruits if x != "apple"] # Only accept items that are not "apple":
newlist = [x for x in fruits] # With no if statement:
newlist = [x for x in range(10)] # You can use the range() function to create an iterable:
newlist = [x for x in range(10) if x < 5] # Accept only numbers lower than 5:
newlist = [x.upper() for x in fruits] # Set the values in the new list to upper case:
newlist = ['hello' for x in fruits] # Set all values in the new list to 'hello'
newlist = [x if x != "banana" else "orange" for x in fruits] # Return "orange" instead of "banana".
