thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict) # You can change the value of a specific item by referring to its key name.

thisdict1 =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.update({"year": 2020})
print(thisdict1) # Update the "year" of the car by using the update() method.

