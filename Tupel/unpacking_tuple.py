fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red) # this is Unpacking a tuple method.

# If the number of variables is less than the number of values, you can add an * 
# to the variable name and the values will be assigned to the variable as a list:

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # Assign the rest of the values as a list called "red".

# If the asterix is added to another variable name than the last,
#  Python will assign values to the variable until the number of values left matches the number of variables left.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red) # Add a list of values the "tropic" variable.

