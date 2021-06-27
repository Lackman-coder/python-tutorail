# boolen means True or False checking method:

print(10 > 9)
print(10 == 9)
print(10 < 9) # checking this print True or False.

print(bool("Hello"))
print(bool(20)) # The bool() function allows you to evaluate any value, and give you True or False in return,

x = "Hello"
y = 15

print(bool(x))
print(bool(y)) # another bool type from variable.

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])# this one True boolen. 

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({}) # this one False boolen.

def myFunction() :
  return False

print(myFunction()) # this method function return True or False.

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") # another function boolen method.

x = 200
print(isinstance(x, int)) # Check if an object is an integer or not in boolen using builind "isinstance".