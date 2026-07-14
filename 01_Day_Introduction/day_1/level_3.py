#Level 3
# 1 part: Examples of pyhton data types
# I will use _type() so that when you run the command you can see exactly the data type
print(type(19)) # My age
print(type(49.51))
print(type(1 + 2j))
print(type("Hello, world"))
print(type(True))
print(type([49, 51, 1863]))
print(type((3.14, 49.51, 1863.1864)))
print(type({3.14, 49.51, 1863.1864}))
print(type({'family':'country'}))

# 2 part: Find an euclidean distance between (2, 3) and (10, 8)
# Variables
x_1 = 2
y_1 = 3
x_2 = 10
y_2 = 8
# Do the formula of euclidean distance
result = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** (1/2)
print(result)