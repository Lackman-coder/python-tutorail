thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"] # You can access the items of a dictionary by referring to its key name, inside square brackets.
print(x) 

x = thisdict.get("model") # There is also a method called get() that will give you the same result.
x = thisdict.keys() # The keys() method will return a list of all the keys in the dictionary.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
} # Add a new item to the original dictionary, and see that the keys list gets updated as well
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change 

car1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car1.values() # The values() method will return a list of all the values in the dictionary.
print(x) #before the change
car1["year"] = 2020
print(x) #after the change 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values() # Make a change in the original dictionary, and see that the values list gets updated as well.
print(x) #before the change
car["year"] = 2020
print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values() # Add a new item to the original dictionary, and see that the values list gets updated as well.
print(x) #before the change
car["color"] = "red"
print(x) #after the change 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items() # The items() method will return each item in a dictionary, as tuples in a list.
print(x) #before the change
car["year"] = 2020
print(x) #after the change 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items() # Add a new item to the original dictionary, and see that the items list gets updated as well.
print(x) #before the change
car["color"] = "red"
print(x) #after the change

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") # To determine if a specified key is present in a dictionary use the in keyword.

 