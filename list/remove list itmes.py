thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) # The remove() method removes the specified item.

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist) # The pop() method removes the specified index.

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) # If you do not specify the index, the pop() method removes the last item.

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) # The del keyword also removes the specified index.

thislist1 = ["apple", "banana", "cherry"]
del thislist1

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) # The clear() method empties the list.