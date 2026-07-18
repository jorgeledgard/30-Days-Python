# Fist we are going to calculate the intersections
y = 0
# Fist when y = 0 (intersection in the x axis)
x = (y + 2) / 2
print("Intersection in the x axis is:", x)
# Now when x = 0 (intersection in the y axis)
x = 0
y = 2*x - 2
print("Intersection in y axis is:", y)

# Now the slope with the points we already have (0, -2), (1, 0)
x_1 = 0
x_2 = 1
y_1 = -2
y_2 = 0
# Now we apply the formula
slope = (y_2 - y_1) / (x_2 - x_1)
print("The slope is:", slope)