balance = 500  

while True:  
    print(f"\nYour current balance is: ${balance}")  
    amount = int(input("Enter withdrawal amount (or 0 to exit): "))  

    if amount == 0:  # Exit condition  
        print("Thank you for using the ATM!")
        break  
    elif amount > balance:  
        print("Insufficient funds! Try again.")  
    elif amount <= balance:  # This condition is now combined  
        balance -= amount  
        print(f"Withdrawal successful! New balance: ${balance}")  

    # Check if balance is now zero after a successful withdrawal  
    if balance == 0:  
        print("\nYour balance is empty. Thank you for using the ATM!")  
        break  # Explicitly breaking out when balance is 0  