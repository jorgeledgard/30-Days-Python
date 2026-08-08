# We use input() to get the month
season = input("Enter the month we are in: ")

# We use conditionals to get the season we are in
if season in ["December", "January", "February"]:
    print("We are in Winter")
elif season in ["March", "April", "May"]:
    print("We are in Spring")
elif season in ["June", "July", "August"]:
    print("We are in Summer")
elif season in ["September", "October", "November"]:
    print("We are on Autumn")
else:
    print("Enter a month, no other value")