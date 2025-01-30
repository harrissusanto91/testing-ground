import random  

# add your comment here (explain what we are doing here)
score = 0  
rolls = []  

# add your comment here (explain what we are doing here)
print("wellcome message to player")
print("instruction for the player what is the goal of the game") 


# add your comment here (explain what is this section do)
while score < 50:  
    input("instruction to player how to roll")
    die = random.randint(1, 6)
    score += die  # add your comment here  
    rolls.append(die)  # add your comment here  

    print(f"show the result of your dice with f string method") 
    print(f"show the result of total score with f string method") 

# add your comment here  (explain what is this section do)
print("congratulation message")
print(f"show the result of total score with f string method")  
print(f"show the all of your roll with f string method")
