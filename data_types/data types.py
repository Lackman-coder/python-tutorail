"""
Text Type: 	str
Numeric Types: 	int, float, complex
Sequence Types: 	list, tuple, range
Mapping Type: 	dict
Set Types: 	set, frozenset
Boolean Type: 	bool
Binary Types: 	bytes, bytearray, memoryview """

x = 5
y = "good"
c = 1.5
d = 3j
e = [1,2,3,4,5]
f = ("g","d","k")
h = {"a","c","v"}
j = frozenset({"apple", "banana", "cherry"})
l = {"name" : "John", "age" : 36}
m = True
i = range(5)
v = b"Hello"
n = bytearray(5)
z = memoryview(bytes(5))
print(type(x))
print(type(y))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(h))
print(type(j))
print(type(l))
print(type(m))
print(type(i))
print(type(v))
print(type(n))
print(type(z))
