# Local Scope
"""
A variable created inside a function belongs to the local scope of that function,
and can only be used inside that function."""

def myfunc():
  x = 300
  print(x)

myfunc() # A variable created inside a function is available inside that function.

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc() # The local variable can be accessed from a function within the function.

x = 300
def myfunc():
  print(x)
myfunc()
print(x) # A variable created outside of a function is global and can be used by anyone.

x = 300
def myfunc():
  x = 200
  print(x)
myfunc()
print(x) # The function will print the local x, and then the code will print the global x.

def myfunc():
  global x
  x = 300
myfunc()
print(x) # If you use the global keyword, the variable belongs to the global scope.

x = 300
def myfunc():
  global x
  x = 200
myfunc()
print(x) # To change the value of a global variable inside a function, refer to the variable by using the global keyword.
