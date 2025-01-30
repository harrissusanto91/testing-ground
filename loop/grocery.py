# Initial amount of money  
budget = 200000  
print(f"You have Rp {budget:,}")  # Format the budget with commas  

# Initialize an empty list to keep track of the items purchased  
purchased_items = []  
total_cost = 0  # To track the total cost of items  

# Begin the grocery shopping loop  
while True:  
    # Ask for the grocery item and its price  
    item = input("Enter the grocery item (or type 'done' to finish): ")  
    
    if item.lower() == 'done':  # Break the loop if the user is done  
        break  

    price = float(input(f"Enter the price of {item} (in Rp): "))  
    
    # Check if the price is within the budget  
    if total_cost + price <= budget:  
        purchased_items.append((item, price))  # Append tuple of item and price  
        total_cost += price  # Update total cost  
        remaining_budget = budget - total_cost  # Calculate remaining budget  
        print(f"You bought {item} for Rp {price:,}.")  # Format price with commas  
        print(f"Money left: Rp {remaining_budget:,}\n")  # Format remaining budget with commas  
    else:  
        print("You do not have enough money for that item. Please choose a different item.\n")  

# Final summary  
print("\nSummary of your purchases:")  
for item, price in purchased_items:  
    print(f"- {item}: Rp {price:,}")  # Format each purchased item price with commas  

print(f"\nTotal cost: Rp {total_cost:,}")  # Format total cost with commas  
print(f"Remaining money: Rp {budget - total_cost:,}")  # Format remaining money with commas