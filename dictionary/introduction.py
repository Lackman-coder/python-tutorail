# Dictionary

'''Dictionaries are used to store data values in key:value pairs.

   A dictionary is a collection which is ordered*, changeable and does not allow duplicates.
   Dictionaries are written with curly brackets, and have keys and values '''
   
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) # Create and print a dictionary.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)  # Duplicate values will overwrite existing values.
print(len(thisdict)) # To determine how many items a dictionary has, use the len() function.

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}  # The values in dictionary items can be of any data type.

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) # Print the data type of a dictionary.

