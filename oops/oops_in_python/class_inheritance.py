# Python Inheritance
"""Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class."""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() # Create a class named Person, with firstname and lastname properties, and a printname method.

class Student(Person):
    pass # Create a class named Student, which will inherit the properties and methods from the Person class.
x = Student("Mike", "Olsen")
x.printname() # Use the Student class to create an object, and then execute the printname method.

class Student(Person): # Add the __init__() function to the Student class
  def __init__(self, fname, lname):
    #add properties etc. 
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
    pass

class Student(Person): # Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) # Python also has a super() function that will make the child class inherit all the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019 # Add a property called graduationyear to the Student class.

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019) # Add a year parameter, and pass the correct year when creating objects.

class Student(Person): # Add a method called welcome to the Student class.
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 

