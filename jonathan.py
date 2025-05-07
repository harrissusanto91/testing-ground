#import libraries
import os, re, random
from random import randint

#DICES ART

number1 = """
_____________
|            |
|            |
|     ()     |
|            |
|____________|
"""

number2 = """
_____________
|            |
|  ()        |
|            |
|        ()  |
|____________|
"""

number3 = """
_____________
|            |
|  ()        |
|     ()     |
|        ()  |
|____________|
"""

number4 = """
_____________
|            |
|  ()    ()  |
|            |
|  ()    ()  |
|____________|
"""

number5 = """
_____________
|            |
|  ()    ()  |
|     ()     |
|  ()    ()  |
|____________|
"""

number6 = """
_____________
|            |
|  () () ()  |
|            |
|  () () ()  |
|____________|
"""

#SAVING VARIABLES
rollhistoryoption = False
rollamountoption = False
autoexitoption = False
diceamount = 10

while True : #MAIN MENU

    #RESET VARIABLES
    dices = [number1, number2, number3, number4, number5, number6]
    rollhistory = []
    i = 0

    os.system('cls')
    print(f"""
    ░█████╗░░█████╗░░█████╗░██╗░░░░░  ██████╗░██╗░█████╗░███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
    ██╔══██╗██╔══██╗██╔══██╗██║░░░░░  ██╔══██╗██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
    ██║░░╚═╝██║░░██║██║░░██║██║░░░░░  ██║░░██║██║██║░░╚═╝█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
    ██║░░██╗██║░░██║██║░░██║██║░░░░░  ██║░░██║██║██║░░██╗██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
    ╚█████╔╝╚█████╔╝╚█████╔╝███████╗  ██████╔╝██║╚█████╔╝███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
    ░╚════╝░░╚════╝░░╚════╝░╚══════╝  ╚═════╝░╚═╝░╚════╝░╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

    1. Play
    2. Settings
    3. Exit
    """)

    choice = int(input("Enter a number to select : ")) #PROMPT USER

    if choice == 1 : #DICE GAME
        while i <= diceamount :

            os.system('cls')
            print(f"Press Enter to roll the dice")

            if rollamountoption : #CHECK IF ROLLAMOUNTOPTION IS TRUE
                print(f"You have {diceamount - i} rolls left.")

            if rollhistoryoption : #CHECK IF ROLLHISTORYOPTION IS TRUE
                print(f"Roll history : {rollhistory}")

            roll = randint(0, 5)
            i = i + 1
            rollhistory.append(roll + 1)

            input(dices[roll])

        if autoexitoption :
            break

    elif choice == 2 : #SETTINGS
        
        os.system('cls')
        diceamount = int(input("Enter how many times you want to roll the dice (default is 10) : "))
        
        rollamountoption = input("Do you want to show the remaining rolls you have (yes/no) : ").strip().lower() #ROLL AMOUNT
        if rollamountoption == "yes" :
            rollamountoption = True

        elif rollamountoption == "no" :
            rollamountoption = False

        rollhistoryoption = input("Do you want to show the roll history (yes/no) : ").strip().lower() #ROLL HISTORY

        if rollhistoryoption == "yes" :
            rollhistoryoption = True

        elif rollhistoryoption == "no" :
            rollhistoryoption = False

        autoexitoption = input("Do you want to automatically exit once all rolls are used (yes/no) : ").strip().lower() #AUTO EXIT PROGRAM

        if autoexitoption == "yes" :
            autoexitoption = True

        elif autoexitoption == "no" :
            autoexitoption = False


    elif choice == 3 : #EXIT THE PROGRAM
        break

#Error handler
    else :  
        print("Not a valid option")

#end program
os.system('cls')
print("Thanks for playing!")    