# List we will be using
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Using sort and finding max and min ages
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])

# Adding another min and max to the list
ages.insert(0, 19)
ages.insert(-1, 26)
print(ages)

# Finding de median
# We know the list and the medium ages are the index 6 and 7
print("Median range of ages are:", (ages[6] + ages[7]) / 2)

# Finding the average
# There are 19, 20, 22, 24, 25 and 26, we are gonna count each one and multiply it by the values list before 
avg = 19 * ages.count(19) + 20 * ages.count(20) + 22 * ages.count(22) + 24 * ages.count(24) + 25 * ages.count(25) + 26 * ages.count(26)
# We are gonna divide all of the above by len(ages)
print("The average age is:", avg / len(ages))

# Finding the range
rng = ages[-1] - ages[0]
print("The range fo the ages is:", rng)

# Comparing |min - avg| and |max - avg|
mini = ages[0]
maxx = ages[-1]
comp_1 = abs(mini - avg)
comp_2 = abs(maxx - avg)
print(comp_1)
print(comp_2)

# I dont have internet so Im gonna use the list in the last excercise
countries =  ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Finding the middle element 
print(countries[3]) # Its the index 3 because there is 7 items so the middle is 4 but in index is 3 nad its Finland
coun_1 = countries[0:4]
coun_2 = countries[4:7]
print(coun_1)
print(coun_2)

# Separate the first countries from the other 4
coun_oth = countries[0:3]
scandic_countries = countries[3:7]
print(coun_oth)
print(scandic_countries)