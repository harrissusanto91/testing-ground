balance = 500

while balance > 0:  # Loop only while there is money left
    print(f"\nYour current balance is: ${balance}")
    amount = int(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient funds! Try again.")
    else:
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance}")

print("\nYour balance is empty. Thank you for using the ATM!")