
# "99 bottles of beer on the wall using a while loop"

bottles = 99
# For bottle 99 to 2
while bottles > 2:
    print(bottles, "bottles of beer on the wall")
    print(bottles, "bottles of beer")
    print("Take one down, pass it around.")
    bottles -= 1
    print(bottles, "bottles of beer on the wall!")
    print("   ")


# To go from 2 bottles to 1
if bottles == 2:
    print(bottles, "bottles of beer on the wall")
    print(bottles, "bottles of beer")
    print("Take one down, pass it around.")
    bottles -= 1
    print(bottles, "bottle of beer on the wall!")
    print("   ")

# From 1 bottle to 0
if bottles == 1:
    print(bottles, "bottle of beer on the wall")
    print(bottles, "bottle of beer")
    print("Take one down, pass it around.")
    print("No bottles of beer on the wall... sad. :(")
    print("   ")
