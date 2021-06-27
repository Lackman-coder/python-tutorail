a = 'hello' # single line string inside the single ('')quates.
print(a)

b = "world" # single line string in double ("")quarts.
print(b)

c = """ i am your frd
        python my frd
        love you python """ 
print(c)# this method call multiline string
        
d = "Hai , lackman"
print(d[8]) # Get the character at position 1 (remember that the first character has the position 0):

e = "hai , raku"
print(len(e)) # this method can find length of inputs.

txt = "The best things in life are free!"
print("free" in txt) # this method for find defined word and if have inside it will give boolen output(true or false).

txt1 = "The best things in life are free!"
if "free" in txt1:
  print("Yes, 'free' is present.") # this method for define if statment to get proper output

txt2 = " the best things sometimes happens"
if not "expensive" in txt2:
    print("txt2 inside no have expensive") # this  function for check whether needed thing have inside or not.