# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) # Sort the list alphabetical order.

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) # sort the list numarical order.

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) # To sort descending, use the keyword argument reverse = True and print reverse order.

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) # to sort reverse order in numarical.

# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first): 
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) # Sort the list based on how close the number is to 50.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) # By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) # So if you want a case-insensitive sort function, use str.lower as a key function.

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) # The reverse() method reverses the current sorting order of the elements.