# Declare variables
base = input("How long is the base of the rectangle?: ")
height = input("How long is the height?: ")

# Calculate the area
area = float(base) * float(height)
print("The area of the rectangle is", area, "m**2")

# Calculate perimeter
per = 2 * (float(base) + float(height))
print("The perimeter is:", per, "m")