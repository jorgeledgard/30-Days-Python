# Excercise 1 
empty = []

# Excercise 2
countries = ["Mexico", "Spain", "Egypt", "Japan", "Australia"]

# Excercise 3
print(len(countries)) # 5

# Excercise 4
print(countries[0]) # Mexico
print(countries[2]) # Egypt
print(countries[-1]) # Australia

# Excercise 5
mixed_data_types = ["Jorge", 19, 184, "Alone:(", "Mexico"]

# Excercise 6
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Excercises 7
print(it_companies)

# Excercise 8
print(len(it_companies)) # 7

# Excercise 9
print(it_companies[0]) # Facebook
print(it_companies[3]) # Apple
print(it_companies[-1]) # Amazon

# Excercise 10
it_companies[0] = "Meta" # Replace Facebook for Meta
print(it_companies)

# Excercise 11
it_companies.append("Facebook") # Add Facebook
print(it_companies)

# Excercise 12
it_companies.insert(4, "Nvidia") # Add Nvidia in the middle 
print(it_companies)

# Excercise 13
it_companies[4] = it_companies[4].upper() # NVIDIA
print(it_companies)

# Excercise 14
result = "#; ".join(it_companies)
print(result)

# Excercise 15
exist = "IBM" in it_companies # True
print(exist)

# Excercise 16
it_companies.sort()
print(it_companies)

# Excercise 17
it_companies.reverse()
print(it_companies)

# Excercise 18
print(it_companies[0:3])

# Excercise 19
print(it_companies[-3:])

# Excercise 20
print(it_companies[4])

# Excercise 21
del it_companies[0]
print(it_companies)

# Excercise 22
del it_companies[3:5]
print(it_companies)

# Excercise 23
del it_companies[-1]
print(it_companies)

# Excercise 24
it_companies.clear()
print(it_companies)

# Excercise 25
del it_companies

# Excercise 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# Excercise 27
# Joining lists of Excercise 26
both_ends = front_end + back_end
# Copy join list
full_stack = both_ends.copy()
print(full_stack)
# Adding Python and SQL
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)