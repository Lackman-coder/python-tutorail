# Python For Loops

'''A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) # Print each fruit in a fruit list.

for g in "grape":
  print(g) # Even strings are iterable objects, they contain a sequence of characters.

fruits = ["apple", "banana", "cherry"]
for d in fruits:
  print(d)
  if d == "banana":
    break # With the break statement we can stop the loop before it has looped through all the items.

fruits = ["grape", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) # Exit the loop when x is "banana", but this time the break comes before the print.

fruits = ["watermeloon", "pappaya", "kiwi"]
for x in fruits:
  if x == "pappaya":
    continue
  print(x) # With the continue statement we can stop the current iteration of the loop, and continue with the next.

for x in range(6):
  print(x) # Using the range() function,starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

for x in range(2, 6):
  print(x) # Using the start parameter(2).end with(6).

for x in range(2, 20, 3):
  print(x) # Increment the sequence with 3 (default is 1).

for x in range(6):
  print(x)
else:
  print("Finally finished!") # The else keyword in a for loop specifies a block of code to be executed when the loop is finished.

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!") # Break the loop when x is 3, and see what happens with the else block.

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) # A nested loop is a loop inside a loop.
                #The "inner loop" will be executed one time for each iteration of the "outer loop".

for x in [0, 1, 2]:
  pass # for avoid error use pass bcoz for loop cannot leaveit empty.

