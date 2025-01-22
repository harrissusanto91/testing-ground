class Room:  
    """A class representing different rooms in the game."""  
    def __init__(self, name, description, items=None):  
        self.name = name  
        self.description = description  
        self.items = items if items else []  
    
    def enter(self):  
        print(f"\nYou are in the {self.name}.")  
        print(self.description)  
        if self.items:  
            print("You see the following items:")  
            for item in self.items:  
                print(f"- {item}")  
        else:  
            print("The room is empty.")  

    def remove_item(self, item):  
        if item in self.items:  
            self.items.remove(item)  
            print(f"You picked up: {item}")  
            return item  
        else:  
            print("That item is not here.")  
            return None  


class Game:  
    """The main game logic."""  
    def __init__(self):  
        self.room = Room("Locked Room", "You woke up in a locked room.")  
        self.cabinet = Room("Cabinet", "A small wooden cabinet full of interesting items.", ["Flashlight", "Map"])  
        self.closet = Room("Closet", "A dark closet filled with clothes and some old boxes.", ["Key"])  
        self.current_area = self.room  
        self.inventory = []  

    def switch_area(self, area):  
        """Switch between the three areas."""  
        if area == "room":  
            self.current_area = self.room  
        elif area == "cabinet":  
            self.current_area = self.cabinet  
        elif area == "closet":  
            self.current_area = self.closet  
        else:  
            print("Invalid area. Choose room, cabinet, or closet.")  

    def play(self):  
        while True:  
            self.current_area.enter()  
            if isinstance(self.current_area, Room):  
                action = input("What would you like to do? (pick up [item], switch to [room|cabinet|closet], check inventory, unlock, exit): ")  

                if action.startswith("pick up "):  
                    item_name = action.split("pick up ")[-1]  
                    item = self.current_area.remove_item(item_name)  
                    if item:  
                        self.inventory.append(item)  
                
                elif action.startswith("switch to "):  
                    area_name = action.split("switch to ")[-1]  
                    self.switch_area(area_name)  

                elif action == "check inventory":  
                    print("Your inventory:", self.inventory)  
                
                elif action == "unlock":  
                    if "Key" in self.inventory and self.current_area == self.room:  
                        print("You unlocked the room using the key! You escape and win!")  
                        break  
                    else:  
                        print("You need the key from the closet to unlock this room.")  
                
                elif action == "exit":  
                    print("Thanks for playing!")  
                    break  

                else:  
                    print("Invalid action.")  


if __name__ == "__main__":  
    game = Game()  
    game.play()