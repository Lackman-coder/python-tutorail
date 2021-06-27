# lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
# The expression is executed and the result is returned:

x = lambda a : a + 10
print(x(5)) # Add 10 to argument a, and return the result.

x = lambda a, b : a * b
print(x(5, 6)) # Multiply argument a with argument b and return the result.

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) # Summarize argument a, b, and c and return the result.

def myfunc(n):
  return lambda a : a * n # The power of lambda is better shown when you use them as an anonymous function inside another function.

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) # Use that function definition to make a function that always doubles the number you send in.

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11)) # use the same function definition to make both functions, in the same program.

