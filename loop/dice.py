import random  

# Initialize the player's score and create a list to keep track of rolls  
score = 0  
rolls = []  

# Display a welcome message to the player and explain the game goal  
print("Welcome to the game!")  
print("Instructions for the player: Reach a score of 50 to win the game.")   

# Start a loop that continues until the player's score reaches 50  
while score < 50:  
    input("Press Enter to roll the die.")  
    die = random.randint(1, 6)  
    score += die  # Update the player's score with the result of the roll  
    rolls.append(die)  # Keep track of each roll by adding it to the rolls list  

    print(f"You rolled a {die}.") 
    print(f"Your total score is now {score}.")  

# Once the loop ends, the player has reached or exceeded a score of 50  
print("Congratulations, you reached or exceeded a score of 50!")   

# Ask if the player wants to see the history of rolls  
show_history = input("Do you want to see the history of your rolls? (yes/no): ").strip().lower()  

# Display the history if player asks for it  
if show_history == 'yes':  
    print("History of your rolls:")  
    for index, roll in enumerate(rolls, start=1):  
        print(f"Roll {index}: {roll}")  
else:  
    print("Thanks for playing!")  