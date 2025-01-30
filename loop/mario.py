# Get valid height from user
while True:
    try:
        height = int(input("Height: "))
        if 1 <= height <= 8:
            break
    except ValueError:
        pass  # Ignore non-integer inputs

# Print the double pyramid
for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i + "  " + "#" * i)