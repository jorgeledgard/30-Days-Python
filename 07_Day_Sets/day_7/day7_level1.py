# Set we will be using
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Excercise 1
print(len(it_companies)) # 7

# Excercise 2
it_companies.add("Twitter")
print(it_companies)

# Excercise 3
it_companies.update(["Meta", "X", "Nvidia"])
print(it_companies)

# Excercise 4
it_companies.remove("Facebook")
print(it_companies)

# Excercise 5
it_companies.discard("Intel") # It works even if the item doesnt exist
print("Below its gonna be an error: ")
it_companies.remove("Huawei") # Works only with the items that exists if it doesnt exist then it says its an error