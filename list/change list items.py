thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) # To change the value of a specific item, refer to the index number.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist) # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon".

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # Change thChange the second value by replacing it with two new values.

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist) # Change the second and third value by replacing it with one value.

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) # To insert a new list item, without replacing any of the existing values, we can use the insert() method.

