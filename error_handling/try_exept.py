def get_int(prompt):
    while True:
        try:
            return (int(input(prompt)))
        except ValueError:
            pass

x = get_int("What's x? ")
print(f"x is {x}")