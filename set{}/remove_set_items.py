thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # To remove an item in a set, use the remove(), or the discard() method.

# Note: If the item to remove does not exist, remove() will raise an error.

thisset = {"apple", "grape", "cherry"}
thisset.discard("grape")
print(thisset) # Remove "banana" by using the discard() method.

thisset1 = {"apple", "banana", "cherry"}
x = thisset1.pop()
print(x)
print(thisset1) # Remove the last item by using the pop() method.

# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # The clear() method empties the set.

thisset2 = {"apple", "banana", "cherry"}
del thisset2
print(thisset2) # The del. keyword will delete the set completely it will give error bcoz full set deleted..
                # so cannot makeoutput..