# Creating a Function
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
  print("Hello from a function") # In Python a function is defined using the (def) keyword.

my_function() # for calling function to work.

"""Arguments:

Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses.
You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). 
When the function is called, we pass along a first name, 
which is used inside the function to print the full name: check below how working """

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus") #this function expect 1 argument to make multi output.

""" Number of Arguments:

By default, a function must be called with the correct number of arguments.
Meaning that if your function expects 2 arguments, 
you have to call the function with 2 arguments,not more, and not less. """

def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes") # This function expects 2 arguments, and gets 2 arguments.

"""Arbitrary Arguments, *args

If you do not know how many arguments that will be passed into your function, 
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly"""

def my_function(*kids): # Arbitrary Arguments are often shortened to (*args) in Python documentations.
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") # If the number of arguments is unknown, add a * before the parameter name.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") # You can also send arguments with the key = value syntax.
                                                                  # This way the order of the arguments does not matter.

def my_function(**kid): # Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes") # If the number of keyword arguments is unknown, add a double ** before the parameter name.

def my_function(country = "Norway"): # The following example shows how to use a default parameter value.
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function("abu dhabi")
my_function("Brazil") # If we call the function without argument, it uses the default value.

""" Passing a List as an Argument

You can send any data types of argument to a function (string, number, list, dictionary etc.), 
and it will be treated as the same data type inside the function."""

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits) #  if you send a List as an argument, it will still be a List when it reaches the function.

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9)) # To let a function return a value, use the return statement.

def myfunction():
  pass # to avoid getting error using pass.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse").
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\n\nRecursion Example Results")
tri_recursion(6)

