# Excercise 2
fruits = ("apple", "orange", "banana")
vegetables = ("tomato", "potato", "lettuce")
animal_products = ("meat", "chicken", "sausage")
food_stuff_tp = fruits + vegetables + animal_products

# Excercise 3
food_stuff_ls = list(food_stuff_tp)

# Excercise 4
print(food_stuff_tp[4]) # potato

# Excercise 5
print(food_stuff_ls[0:3]) # First three items
print(food_stuff_ls[-3:]) # Last three items

# Excercise 6
del food_stuff_tp # Delete the tuple

# Excercise 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)