# Program to draw a square of a given size

# Get input from user
size = int(input("Enter the size of the square: "))

# Draw the square
print("Output:")
# Top edge
print("* " * size)

# Middle part (sides only)
for i in range(size - 2):
    print("* " + "  " * (size - 2) + "*")

# Bottom edge (only if size > 1)
if size > 1:
    print("* " * size)