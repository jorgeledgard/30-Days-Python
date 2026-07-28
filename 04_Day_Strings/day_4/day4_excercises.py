# Excercise 1
a = "Thirty"
b = "Days"
c = "Of"
d = "Python"
print(f"{a} {b} {c} {d}")

# Excercise 2
e = "Coding"
f = "For"
g = "All"
print(f"{e} {f} {g}")

# Excercise 3
company = "Coding For All"

# Excercise 4
print(company)

# Excercise 5
print(len(company))

# Excercise 6
print(company.upper())

# Excercise 7
print(company.lower())

# Excercise 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Excercise 9
print(company[0:6])

# Escercise 10
print(company.startswith("Coding"))

# Excercise 11
print(company.replace("Coding", "Python"))

# Excercise 12
comp = "Python for Everyone"
print(comp.replace("Everyone", "All"))

# Excercise 13
print(company.split(" "))

# Excercise 14
apps = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(apps.split(","))

# Excercise 15
print(company[0]) # C

# Excercise 16
print(company.rindex("l")) # 13

# Excercise 17
print(company[10]) # A space " "

# Excercise 18
pfe = "Python for Everyone"

# Excercise 19
cdf = "Coding For All"

# Excercise 20
print(cdf.index("C")) # 0

# Excercise 21
print(cdf.index("F")) # 7

# Excercise 22
cfap = "Coding For All People"
print(cfap.rfind("l")) # 19

# Escercise 23
large_string = "You cannot end a sentence with because because because is a conjunction"
print(large_string.index("because")) # 31

# Excercise 24
print(large_string.rindex("because")) # 47

# Excercise 25
print(large_string.replace(" because because because", ""))

# Excercise 26
print(large_string.find("because")) # 31

# Excercise 27
print(large_string.replace(" because because because", "")) # Its the same from excercise 25 idk why

# Excercise 28
print(cdf.startswith("Coding"))

# Excercise 29
print(cdf.endswith("coding"))

# Excercise 30
_cdf_ = " Coding For All "
print(cdf.strip(" "))

# Excercise 31
var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"
print(var1.isidentifier()) # False
print(var2.isidentifier()) # True

# Excercise 32
list_1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
js_1 = " ".join(list_1)
print(js_1)

# Excercise 33
print("I am enjoying this challenge. \nI just wonder what is next.")

# Excercise 34
print("Name\t\tAge\tCountry\tCity") # Its ugly, but is what I can do:) PD: I dont have internet in this moment to search more, sorry:(
print("Asabeneh\t250\tFinland\tHelsinki") 

# Excercise 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with {radius} is {area}")

# Excercise 36
m = 8
n = 6
print(f"{m} + {n} = {m + n}")
print(f"{m} - {n} = {m - n}")
print(f"{m} * {n} = {m * n}")
print(f"{m} / {n} = {m / n:.2f}")
print(f"{m} % {n} = {m % n}")
print(f"{m} // {n} = {m // n}")
print(f"{m} ** {n} = {m ** n}")