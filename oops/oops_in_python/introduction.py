class MyClass:
  x = 5  # Create a class named MyClass, with the class named x.

p1 = MyClass() # Create an object named p1, and print the value of x.
print(p1.x) 

# The __init__() Function
'''
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age) # Create a class named Person, use the __init__() function to assign values for name and age.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc() # Insert a function that prints a greeting, and execute it on the p1 object.

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc() # Use the words mysillyobject and abc instead of self.

p1.age = 40 # Set the age of p1 to 40
del p1.age  # Delete the age property from the p1 object.
del p1 # You can delete objects by using the del keyword.
pass # avoid getting error use pass.
