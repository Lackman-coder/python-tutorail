thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict) # Make a copy of a dictionary with the copy() method.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1969
}
mydict = dict(thisdict)
print(mydict) # Make a copy of a dictionary with the dict() function.

