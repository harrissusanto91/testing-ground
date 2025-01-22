class Room:  
    def __init__(self, name, description):  
        self.name = name  
        self.description = description  
        self.connections = []  # Store connected rooms as a list  

    def add_connection(self, room):  
        """Connect this room to another room."""  
        self.connections.append(room)  

    def get_description(self):  
        """Return the description of the room."""  
        return f"{self.name}: {self.description}"  

class Game:  
    def __init__(self):  
        # Create all rooms in a clearly defined order  
        self.starting_room = Room("Starting Room", "You wake up in a room with two doors.")  
        self.garden_room = Room("Garden", "A beautiful garden filled with flowers.")  
        self.cave_room = Room("Cave", "A dark and scary cave.")  
        self.dining_room_instance = Room("Dining Room", "You enter a large dining room with a long table.")  
        self.kitchen_room = Room("Kitchen", "The kitchen is filled with the smell of freshly baked bread.")  
        self.pond_room = Room("Pond", "A serene pond surrounded by lush greenery.")  
        self.balcony_room = Room("Balcony", "A balcony overlooking a beautiful landscape.")  
        self.crypt_room = Room("Crypt", "A dark, dusty crypt filled with old tombs.")  

        # Explicitly define connections right after each room creation  
        self.starting_room.add_connection(self.garden_room)       # Starting Room <-> Garden  
        self.starting_room.add_connection(self.cave_room)         # Starting Room <-> Cave  
        self.starting_room.add_connection(self.dining_room_instance) # Starting Room <-> Dining Room  

        self.garden_room.add_connection(self.starting_room)       # Garden <-> Starting Room  
        self.garden_room.add_connection(self.pond_room)           # Garden <-> Pond  

        self.cave_room.add_connection(self.starting_room)         # Cave <-> Starting Room  
        self.cave_room.add_connection(self.crypt_room)            # Cave <-> Crypt  

        self.dining_room_instance.add_connection(self.starting_room) # Dining Room <-> Starting Room  
        self.dining_room_instance.add_connection(self.kitchen_room)  # Dining Room <-> Kitchen  

        self.kitchen_room.add_connection(self.dining_room_instance) # Kitchen <-> Dining Room  
        self.kitchen_room.add_connection(self.balcony_room)        # Kitchen <-> Balcony  

        self.pond_room.add_connection(self.garden_room)            # Pond <-> Garden  
       
        self.balcony_room.add_connection(self.kitchen_room)        # Balcony <-> Kitchen  

        self.crypt_room.add_connection(self.cave_room)             # Crypt <-> Cave  

        # Start at the starting room  
        self.current_room = self.starting_room  

    def play(self):  
        while True:  
            # Describe the current room  
            print(self.current_room.get_description())  
            print("Connections:", end=' ')  

            # Show available connections  
            connections = [connected_room.name for connected_room in self.current_room.connections]  
            print(", ".join(connections))  

            # Get user input  
            choice = input("Which room do you want to go to? ").strip().lower()  

            # Navigate based on user choice  
            room_found = False  
            for conn in self.current_room.connections:  
                if conn.name.lower() == choice:  
                    self.current_room = conn  
                    room_found = True  
                    break  
            
            if not room_found:  
                print("You can't go that way!")  

# Start the game  
if __name__ == "__main__":  
    game = Game()  # Create a new game instance  
    game.play()    # Start the game