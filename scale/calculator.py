def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def calculator():
    print("""
Welcome to the Calculator!

Select a mode:
1. Addition
2. Subtraction
3. Multiplication
4. Division
""")

    while True:
        mode = input("Enter the number of the mode you want (1-4): ")
        if mode in ["1", "2", "3", "4"]:
            break
        print("Invalid mode. Please enter a number between 1 and 4.")

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if mode == "1":
        result = addition(a, b)
    elif mode == "2":
        result = subtraction(a, b)
    elif mode == "3":
        result = multiplication(a, b)
    elif mode == "4":
        result = division(a, b)

    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()
