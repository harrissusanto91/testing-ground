class Room:  
    def __init__(self, name, description, choices, is_win=False):  
        self.name = name  
        self.description = description  
        self.choices = choices  
        self.is_win = is_win  # Indicates if this room is a winning room  

    def display(self):  
        print(f"\n--- {self.name} ---")  
        print(self.description)  
        print("What would you like to do?")  
        for index, (option_text, _) in self.choices.items():  
            print(f"{index}: {option_text}")  

def main():  
    # Define the rooms  
    entrance_hall = Room(  
        name="Entrance Hall",  
        description="You are in a grand entrance hall. There are doors to the north and east.",  
        choices={  
            1: ("Go north to the Mysterious Chamber.", "mysterious_chamber"),  
            2: ("Go east to the Library.", "library"),  
        }  
    )  

    mysterious_chamber = Room(  
        name="Mysterious Chamber",  
        description="You find yourself in a dimly lit chamber. Shadows flicker on the walls.",  
        choices={  
            1: ("Examine the flickering shadows.", None),  
            2: ("Go back to the Entrance Hall.", "entrance_hall"),  
            3: ("Exit through a hidden door to the south.", "treasure_room"),  
        }  
    )  

    library = Room(  
        name="Library",  
        description="You enter a dusty library filled with ancient tomes. A ladder leads up to a loft.",  
        choices={  
            1: ("Climb the ladder to the loft.", "loft"),  
            2: ("Read one of the tomes.", None),  
            3: ("Go back to the Entrance Hall.", "entrance_hall"),  
        }  
    )  

    loft = Room(  
        name="Loft",  
        description="You are now in a dusty loft filled with old furniture. There is a window with a view outside.",  
        choices={  
            1: ("Look out the window.", None),  
            2: ("Search the furniture for hidden items.", None),  
            3: ("Climb back down to the Library.", "library"),  
        }  
    )  

    treasure_room = Room(  
        name="Treasure Room",  
        description="Congratulations! You have found the Treasure Room filled with gold and jewels!",  
        choices={  
            1: ("Take the treasure and win!", None),  
        },  
        is_win=True  
    )  

    # A lookup dictionary for room transitions  
    rooms = {  
        "entrance_hall": entrance_hall,  
        "mysterious_chamber": mysterious_chamber,  
        "library": library,  
        "loft": loft,  
        "treasure_room": treasure_room,  
    }  

    # Start the game in the Entrance Hall  
    current_room_key = "entrance_hall"  
    current_room = rooms[current_room_key]  

    while True:  
        current_room.display()  
        choice = input("Enter the number of your choice (or 'exit' to leave): ")  
        if choice.lower() == 'exit':  
            print("Thank you for playing!")  
            break  
        
        # Handle the player's choice  
        next_room = handle_choice(current_room, choice, rooms)  
        
        # Check if next_room is None or if it's the winning room  
        if next_room is None:  
            print("Nothing happened. Try something else.")  
        elif next_room.is_win:  
            print(f"You won the game by reaching the {next_room.name}!")  
            break  
        else:  
            current_room = next_room  # Update the current room  

def handle_choice(room, choice, rooms):  
    try:  
        option_text, next_room_key = room.choices[int(choice)]  
        if next_room_key is not None:  
            return rooms[next_room_key]  # Return the next room  
        return None  # No room transition  
    except (ValueError, KeyError):  
        print("Invalid choice! Please try again.")  
        return None  # Return None for invalid choice  

if __name__ == "__main__":  
    main()