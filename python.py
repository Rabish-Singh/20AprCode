from operator import truediv


print("test")
x = "global"

# python function
def myfunc():
  x = "local"
  print("Python is " + x)

myfunc()
print("testing")
x=10
print(x)
#data types in python
# 1 str 
x="hello world"
print(type(x))

# 2 int
x=20
print(type(x))

# 3 float
x=20.5
print(type(x))

# 4 complex
x=1j
print(type(x))

# 5 list
x=["apple","orange","banana","papaya"]
print(type(x))
print(x)

# 6 tuple
x=("apple","orange","banana","papaya")
print(type(x))
print(x)

# 7 range
x=range(7)
print(type(x))
print(x)

# 8 dict
x={"name":"rabish", "last name":"kumar"}
print(type(x))
print(x)

# 9 set
x={"apple","orange","banana","papaya"}
print(type(x))
print(x)

# 10 frozenset
x=frozenset({"apple","banana","guava","grapes"})
print(type(x))
print(x)

# 11 bool
x=True
print(type(x))
print(x)

# 12 bytes
x=b"hello"
print(type(x))
print(x)

# 13 bytearray
x=bytearray(5)
print(type(x))
print(x)

# 14 memoryview
x=memoryview(bytes(5))
print(type(x))
print(x)