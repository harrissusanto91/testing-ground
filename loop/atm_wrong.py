balance = 500

while balance > 0:  # Condition directly in while
    print(f"\nYour current balance is: ${balance}")
    amount = int(input("Enter withdrawal amount (or 0 to exit): "))

    if amount == 0:
        print("Transaction canceled. Thank you for using the ATM!")
        break

    if amount > balance:
        print("Insufficient funds! Try again.")
    else:
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance}")

print("\nThank you for using the ATM!")