x = "awesome" # outside same name variable called global variable.

def myfunc():
  x = "fantastic" # same "x" is inside function called local variable.
  print("Python is " + x)

myfunc()

print("Python is " + x) 

# here we are define the name t as global veriable.
def myfunc():
  global t
  t = "good"
  
myfunc()

print("Python is " + t) 

e = "awesome"

def myfunc():
  global e
  e = "fantastic"

myfunc()

print("Python is " + e) 