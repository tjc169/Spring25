side_length = int(input(f"Enter the length of the sides of the square:"))
radius = int(input(f"Enter the radius of the circle: "))


def square(side):
    return side * side


def circle(radius):
    return 3.14 * radius


print(f"\nThe area of the square is", square(side_length), "square units.")
print(f"\nThe area of the circle is", circle(radius), "square units.")
