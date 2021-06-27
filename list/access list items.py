thislist = ["apple", "banana", "cherry"]
print(thislist[1]) # for accessing list items. start from first item first item means (0).

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) # accessing negetive items in list. -negetive start from last item.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # this one specify the items you want.(it will leave last value item.)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) # This example returns the items from the beginning to, but NOT including, "kiwi".

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) # This example returns the items from "cherry" to the end,bcoz cherry start from 2 position.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) # This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") # Check if "apple" is present in the list,To determine if a specified item is present in a list use the in keyword.

