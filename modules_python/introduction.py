# What is a Module?

"""Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
Create a Module
To create a module just save the code you want in a file with the file extension .py"""

def greeting(name):
  print("Hello, " + name) # Save this code in a file named mymodule.py.

# Use a Module
'''Now we can use the module we just created, by using the import statement'''
import mymodule
mymodule.greeting("Jonathan") # mport the module named mymodule, and call the greeting function.

# The module can contain functions, as already described, 
# but also variables of all types (arrays, dictionaries, objects etc):
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}  # Save this code in the file mymodule.py
import mymodule
a = mymodule.person1["age"]
print(a) # Import the module named mymodule, and access the person1 dictionary.

# Re-naming a Module
'''You can create an alias when you import a module, by using the as keyword'''
import mymodule as mx
a = mx.person1["age"]
print(a) # Create an alias for mymodule called mx.

import platform # there are several built-in modules in Python, which you can import whenever you like.
x = platform.system()
print(x) # Import and use the platform module.

import platform # There is a built-in function to list all the function names (or variable names) in a module. The dir() function.
x = dir(platform)
print(x) # List all the defined names belonging to the platform module.
# Note: The dir() function can be used on all modules, also the ones you create yourself.

def greeting(name): # You can choose to import only parts from a module, by using the from keyword.
  print("Hello, " + name)
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
} # The module named mymodule has one function and one dictionary.
from mymodule import person1
print (person1["age"]) # Import only the person1 dictionary from the module.

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
#  Example: person1["age"], not mymodule.person1["age"]