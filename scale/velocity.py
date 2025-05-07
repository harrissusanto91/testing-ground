import calculator

def main():
    print("""
Welcome to the Velocity Calculator!

We'll calculate velocity using the formula:
velocity = distance / time
""")

    distance = float(input("Enter distance (meters): "))
    time = float(input("Enter time (seconds): "))

    velocity = calculator.division(distance, time)

    if isinstance(velocity, float):
        print(f"Velocity is: {velocity} m/s")
    else:
        print(velocity)  # This prints the error message

if __name__ == "__main__":
    main()
