class Room:  
    """A class representing a room in the game."""  

    def __init__(self, name, description, choices=None):  
        self.name = name  
        self.description = description  
        self.choices = choices if choices else {}  

    def enter(self):  
        print(f"\nYou are in the {self.name}.")  
        print(self.description)  
        if self.choices:  
            print("What do you want to do?")  
            for i, option in enumerate(self.choices.keys(), 1):  
                print(f"{i}. {option}")  

class Game:  
    """The main game logic with branching paths."""  

    def __init__(self):  
        # Create rooms  
        self.start_room = Room("Starting Room", "You wake up in a mysterious room.", {  
            "Examine the room": self.examine_room,  
            "Open the door": self.open_door  
        })  
        self.current_room = self.start_room  # Set the current room to the starting room  

        # Additional rooms  
        self.left_path = Room("Garden", "You find yourself in a serene garden.", {  
            "Examine the fountain": self.examine_fountain,  
            "Pick a flower": self.pick_flower,  
            "Return to the hallway": self.go_back  
        })  
        self.right_path = Room("Cave", "You stand before a dark cave.", {  
            "Enter the cave": self.game_over,  
            "Run back to the hallway": self.go_back  
        })  

        self.good_ending = False  # Flag to track if the good ending condition is met  

    def examine_room(self):  
        # Logic for examining the room  
        print("You examine the room closely.")  
        print("You see some old furniture and a mysterious painting.")  
        # No transition needed, will return to this room again.  

    def open_door(self):  
        print("You open the door and see a hallway with two paths.")  
        choice = input("Which path do you want to take? (1 for left path, 2 for right path): ")  
        if choice == "1":  
            self.current_room = self.left_path  
        elif choice == "2":  
            self.current_room = self.right_path  
        else:  
            print("Invalid option, you hesitated and remain in the starting room.")  

    def examine_fountain(self):  
        print("You examine the fountain; it's beautiful and serene.")  
        # You can add more interactions here if needed.  

    def pick_flower(self):  
        print("You pick a flower from the garden. It's vibrant and has a pleasant scent.")  
        self.good_ending = True  # Set the good ending condition to True  
        print("You feel a sense of joy and accomplishment. This is a special moment!")  

    def go_back(self):  
        self.current_room = self.start_room  

    def game_over(self):  
        print("You were swallowed by the darkness of the cave. Game Over.")  
        exit(0)  # Exits the game  

    def play(self):  
        # Main game loop  
        while True:  
            self.current_room.enter()  # Call the enter method of the current room  
            choice = input("Choose an option: ")  
            options = list(self.current_room.choices)  

            if choice.isdigit() and 1 <= int(choice) <= len(options):  
                action = options[int(choice) - 1]  
                # Call the associated method for that action  
                self.current_room.choices[action]()  
            else:  
                print("Invalid choice. Please try again.")  
            
            # Check for the good ending  
            if self.good_ending and self.current_room == self.left_path:  
                print("Congratulations! You have found happiness in the garden. You live happily ever after!")  
                exit(0)  # Exits the game after achieving the good ending  

# Start the game  
if __name__ == "__main__":  
    game = Game()  
    game.play()