# Input: Get the character's stats  
print("You can distribute a maximum of 20 points among the three stats.")  
dex = int(input("Enter your Dexterity stat (max total stat is 20): "))  
con = int(input("Enter your Constitution stat (max total stat is 20): "))  
intelligence = int(input("Enter your Intelligence stat (max total stat is 20): "))  

# Calculate total of stats  
total_stats = dex + con + intelligence  

# Validate that the total stats do not exceed 20  
if total_stats > 20:  
    print(f"Invalid input! The total of your stats is {total_stats:.2f}. Please ensure the sum does not exceed 20.")  
else:  
    # Determine the job based on the highest valid stat  
    if dex > con and dex > intelligence:  
        job = "Archer"  
    elif con > dex and con > intelligence:  
        job = "Swordsman"  
    elif intelligence > dex and intelligence > con:  
        job = "Mage"  
    else:  
        job = "None — it seems your stats are balanced! You could be versatile in many roles."  

    # Output: Print the chosen job  
    print(f"Based on your stats, you should be a: {job}")