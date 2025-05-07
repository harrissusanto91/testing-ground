import greeting

def main():
    name = input("What's your name? ")
    hour_input = input(f"{name}, what time is it now? My clock is not working. (format hh) ")

    try:
        hour = int(hour_input)
    except ValueError:
        print("Invalid hour. Please enter a number like 08 or 14.")
        return

    if hour < 0 or hour > 24:
        print("That's not a valid time. Please enter a number between 0 and 24.")
        return

    if 5 <= hour <= 11:
        message = greeting.good_morning(name)
    elif 12 <= hour <= 17:
        message = greeting.good_afternoon(name)
    elif 18 <= hour <= 22:
        message = greeting.good_evening(name)
    else:
        message = "You should be sleeping!"

    print(f"{message} Thank you for your assistance. Appreciate it.")

if __name__ == "__main__":
    main()
