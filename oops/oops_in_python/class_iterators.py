# Python Iterators
"""
An iterator is an object that contains a countable number of values.
An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
Technically, in Python, an iterator is an object which implements the iterator protocol,
 which consist of the methods __iter__() and __next__().
 Lists, tuples, dictionaries, and sets are all iterable objects. 
 They are iterable containers which you can get an iterator from."""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit)) # Return an iterator from a tuple, and print each value.

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit)) # Strings are also iterable objects, containing a sequence of characters.

mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x) # We can also use a for loop to iterate through an iterable object.

mystr = "banana"
for x in mystr:
  print(x) # Iterate the characters of a string.

"""The __iter__() method acts similar, you can do operations (initializing etc.),
but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence. """

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter)) # Create an iterator that returns numbers, 
                    #starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)

'''The example above would continue forever if you had enough next() statements,
 or if it was used in a for loop.
To prevent the iteration to go on forever, we can use the StopIteration statement.
In the __next__() method, we can add a terminating condition to raise an error 
if the iteration is done a specified number of times '''

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x) # Stop after 20 iterations
