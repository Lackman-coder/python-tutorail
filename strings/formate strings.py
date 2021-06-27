age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) # this method take needed argument and insert inside the {here} and give output.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price)) # this method take needed argument and insert inside the {here} multiple.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price)) # this method You can use index numbers {0} to be sure the arguments are placed in the correct placeholders: