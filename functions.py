# Input side length of square
side_length = int(input(f"Enter the length of the sides of the square:"))

# Input radius of circle
radius = int(input(f"Enter the radius of the circle: "))

# Use functions to determine areas


def square(side):
    return side * side


def circle(radius):
    return 3.14 * radius


# Print results
print(f"\nThe area of the square is", square(side_length), "square units.")
print(f"\nThe area of the circle is", circle(radius), "square units.")
