# Arrays:
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable.

cars = ["Ford", "Volvo", "BMW"] # Create an array containing car names.
x = cars[0] # You refer to an array element by referring to the index number
cars[0] = "Toyota" # Modify the value of the first array item
v = len(cars) # Return the number of elements in the cars array.
print(v)
for x in cars:
  print(x) # You can use the for in loop to loop through all the elements of an array.

cars.append("Honda") # for adding to array use append.
cars.pop(1) # for remove second element.
cars.remove("Volvo") # You can also use the remove() method to remove an element from the array.
