import random  

# Initialize the score and an empty list to track rolls  
score = 0  
rolls = []  
print("Welcome to the Dice Rolling Game!")  
print("Roll the dice and try to reach a score over 100 to win!")  

# Game loop  
while score <= 100:  
    input("Press Enter to roll the dice...")  # Wait for the user to roll the dice  
    
    # Roll two dice  
    die1 = random.randint(1, 6)  # Roll the first die  
    die2 = random.randint(1, 6)  # Roll the second die  
    
    # Calculate the total score from the two dice  
    roll_total = die1 + die2  
    score += roll_total  # Update the total score  
    
    # Append the roll result to the rolls list  
    rolls.append((die1, die2))  # Save the result as a tuple for each roll  

    print(f"You rolled a {die1} and a {die2}.")  
    print(f"Current score: {score}")  

# Announce win when score exceeds 100  
print("\nCongratulations! You rolled over 100!")  
print(f"Final score: {score}")  

# Display all rolls  
print("\nHere are the rolls that got you to victory:")  
for i, (d1, d2) in enumerate(rolls, start=1):  
    print(f"Roll {i}: {d1} + {d2} = {d1 + d2}")