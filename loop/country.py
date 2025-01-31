while True:  
    # Ask the user for the highest leadership position  
    answer = input("What is the highest leadership position? ")

    # Determine the correct response and provide feedback  
    if answer == "king":  
        print("Correct! A king is a hereditary leader, often having significant ceremonial authority.")  
    elif answer == "president":  
        print("Correct! A president is typically an elected head of state in a republic.")  
    elif answer == "prime minister":  
        print("Correct! A prime minister is usually the head of government in a parliamentary system.")  
    else:  
        print("Incorrect. The highest leadership position can be 'king', 'president', or 'prime minister'.")  

    # Ask if the user wants to try again  
    restart = input("Do you want to try again? (yes/no): ").strip().lower()  
    if restart != 'yes':  
        print("Thanks for playing!")  
        break  